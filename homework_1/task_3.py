latin_char = input("Please enter a latin character = ").lower()
n_value = int(input("Please enter a numeric value = "))
alphabeth = list("abcdefghijklmnopqrstuvwxyz")
for element in alphabeth:
    if latin_char == element:
        index_char = alphabeth.index(latin_char)
        new_index = (index_char + n_value) % len(alphabeth)
        print("Your new character = ", alphabeth[new_index])
