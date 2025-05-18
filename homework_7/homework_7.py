import requests
from bs4 import BeautifulSoup
import csv
import time
import os

INPUT_FILE = "countries.txt"
OUTPUT_FILE = "countries_data.csv"
CACHE_DIR = "cache"


def clean_text(text):
    return text.split("[")[0].replace(",", "").replace("\xa0", " ").strip()


def fetch_wikipedia_page(country):
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)

    filename = os.path.join(CACHE_DIR, f"{country.replace(' ', '_')}.html")

    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()

    url = f"https://en.wikipedia.org/wiki/{country.replace(' ', '_')}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        html = response.text
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)
        time.sleep(1)
        return html
    except Exception as e:
        print(f"[!] Failed to fetch {country}: {e}")
        return None


def extract_info(html, country):
    try:
        soup = BeautifulSoup(html, "html.parser")
        infobox = soup.find("table", {"class": "infobox"})
        if not infobox:
            raise ValueError("No infobox found.")

        capital = area = population = "N/A"

        rows = infobox.find_all("tr")
        for i, row in enumerate(rows):
            header = row.find("th")
            value_cell = row.find("td")

            if not header or not value_cell:
                continue

            label = header.get_text().strip().lower()

            if "capital" in label and capital == "N/A":
                capital = clean_text(value_cell.get_text())

            elif "area" in label and "total" in label and area == "N/A":
                area_text = clean_text(value_cell.get_text())
                if "km" in area_text:
                    area = area_text.split("km")[0].strip()

            elif "population" in label and population == "N/A":
                population = clean_text(value_cell.get_text())

        return capital, area, population
    except Exception as e:
        print(f"[!] Error extracting info for {country}: {e}")
        return "N/A", "N/A", "N/A"


def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        countries = [line.strip() for line in f if line.strip()]

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["country", "city", "area", "population"])

        for country in countries:
            print(f"Processing: {country}")
            html = fetch_wikipedia_page(country)
            if html:
                capital, area, population = extract_info(html, country)
                writer.writerow([country, capital, area, population])


if __name__ == "__main__":
    main()
