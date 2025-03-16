def get_cats_info(path):
    cats_list = []
    
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(",")
                    cats_list.append({"id": cat_id, "name": name, "age": age})
                except ValueError:
                    print(f"Помилка у рядку: {line.strip()}")

        return cats_list

    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return None
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return None

cats_info = get_cats_info("cats.txt")

if cats_info:
    for cat in cats_info:
        print(cat)
