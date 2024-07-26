def get_cats_info(path):
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                id, name, age = line.strip().split(',')

                cats_info.append({
                    "id": id,
                    "name": name,
                    "age": int(age)
                })
    except FileNotFoundError:
        print(f"File at {path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return cats_info

cats = get_cats_info('cats.txt')
for cat in cats:
    print(cat)