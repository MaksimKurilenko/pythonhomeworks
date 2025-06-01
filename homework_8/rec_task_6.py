def find_files_by_ext(ext, tree):
    found_files = []

    for key, value in tree.items():
        if isinstance(value, dict):

            found_files.extend(find_files_by_ext(ext, value))
        elif isinstance(value, list):

            for filename in value:
                if filename.endswith(f".{ext}"):
                    found_files.append(filename)

    return found_files
