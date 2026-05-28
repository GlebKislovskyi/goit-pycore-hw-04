from pathlib import Path

def get_cats_info(path):
    # checking for existing file and early return if not exist
    file = Path(path)
    if not file.exists():
        return None

    with open(path, mode='r', encoding="utf-8", errors="strict") as fh:
        formatted_list = []
        # checking case if lines have \n and filtering empty lines
        cats = [el.strip() for el in fh.readlines() if el.strip()]

        # handle empty file
        if not cats:
            return None

        for cat in cats:
            parts = cat.split(",")
            # validate that we have all required fields
            if len(parts) >= 3:
                id, name, age = parts[0].strip(), parts[1].strip(), parts[2].strip()
                formatted_list.append({"id": id, "name": name, "age": age})

        return formatted_list if formatted_list else None


cats_info = get_cats_info("goit-pycore-hw-04/cats_file.txt")
print(cats_info)
