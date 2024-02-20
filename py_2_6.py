import json

class Person:
    def __init__(self, name, birth_year, mother=None, father=None):
        self.name = name
        self.birth_year = birth_year
        self.mother = mother
        self.father = father
        self.siblings = []
        self.children = []

def create_person():
    name = input("Введіть ім'я особи: ")
    birth_year = input("Введіть рік народження особи: ")
    return Person(name, birth_year)

def add_child(mother, father, child):
    if mother:
        mother.children.append(child)
        mother.siblings.extend(sibling for sibling in mother.children if sibling != child)
    if father:
        father.children.append(child)
        father.siblings.extend(sibling for sibling in father.children if sibling != child)

def add_sibling(existing_person, new_sibling):
    existing_person.siblings.append(new_sibling)
    new_sibling.siblings.append(existing_person)

def add_parents(child, family):
    mother_name = input("Введіть ім'я матері: ")
    father_name = input("Введіть ім'я батька: ")

    mother = next((person for person in family if person.name == mother_name), None)
    father = next((person for person in family if person.name == father_name), None)

    if mother is None:
        mother = create_person()
        family.append(mother)

    if father is None:
        father = create_person()
        family.append(father)

    child.mother = mother
    child.father = father

    mother.children.append(child)
    father.children.append(child)

    mother.siblings.extend(sibling for sibling in mother.children if sibling != child)
    father.siblings.extend(sibling for sibling in father.children if sibling != child)

def display_tree(person, level=0):
    print("  " * level + f"{person.name} ({person.birth_year})")
    for sibling in person.siblings:
        display_tree(sibling, level)
    for child in person.children:
        display_tree(child, level + 1)

def save_tree_to_file(person, filename):
    tree_data = {"name": person.name,
                 "birth_year": person.birth_year,
                 "siblings": [save_tree_to_file(sibling, None) for sibling in person.siblings],
                 "children": [save_tree_to_file(child, None) for child in person.children]}
    if filename:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(tree_data, file, ensure_ascii=False, indent=4)
    return tree_data

def load_tree_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    return load_person_from_data(data)

def load_person_from_data(data):
    person = Person(data["name"], data["birth_year"])
    person.siblings = [load_person_from_data(sibling_data) for sibling_data in data["siblings"]]
    person.children = [load_person_from_data(child_data) for child_data in data["children"]]
    return person

def main():
    print("Вас вітає програма для побудови сімейного дерева!")

    family = []

    while True:
        print("\nМеню:")
        print("1. Додати дитину")
        print("2. Додати брата/сестру")
        print("3. Додати батьків")
        print("4. Вивести дерево на екран")
        print("5. Зберегти дерево у файл")
        print("6. Завантажити дерево з файлу")
        print("7. Вийти")

        choice = input("Оберіть опцію (1-7): ")

        if choice == "1":
            child = create_person()
            add_child(None, None, child)
            family.append(child)
            print(f"{child.name} додано до сімейного дерева.")
        elif choice == "2":
            existing_sibling_name = input("Введіть ім'я існуючого брата/сестри: ")
            existing_sibling = next((sibling for sibling in family if sibling.name == existing_sibling_name), None)
            if existing_sibling:
                new_sibling = create_person()
                add_sibling(existing_sibling, new_sibling)
                family.append(new_sibling)
                print(f"{new_sibling.name} додано як брат/сестра для {existing_sibling.name}.")
            else:
                print(f"Брата/сестри {existing_sibling_name} не знайдено.")
        elif choice == "3":
            child_name = input("Введіть ім'я дитини, для якої додаються батьки: ")
            child = next((c for c in family if c.name == child_name), None)
            if child:
                add_parents(child, family)
                print(f"Батьки для {child.name} успішно додані.")
            else:
                print(f"Дитини {child_name} не знайдено.")
        elif choice == "4":
            print("\nСімейне дерево:")
            for person in family:
                if person.mother is None and person.father is None:
                    display_tree(person)
        elif choice == "5":
            filename = input("Введіть ім'я файлу для збереження дерева: ")
            save_tree_to_file(family[0], filename)
            print(f"Дерево збережено у файл {filename}.")
        elif choice == "6":
            filename = input("Введіть ім'я файлу для завантаження дерева: ")
            family.clear()
            family.append(load_tree_from_file(filename))
            print(f"Дерево завантажено з файлу {filename}.")
        elif choice == "7":
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
