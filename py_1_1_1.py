def reverse_file(input_path, output_path):
    try:
        # Відкриваємо вхідний файл для читання з кодуванням utf-8
        with open(input_path, 'r', encoding='utf-8') as input_file:
            # Читаємо вміст файлу
            content = input_file.read()

            # Записуємо вміст у зворотньому порядку
            reversed_content = content[::-1]

            # Відкриваємо вихідний файл для запису з кодуванням utf-8
            with open(output_path, 'w', encoding='utf-8') as output_file:
                # Записуємо зворотній вміст у вихідний файл, видаляючи порожній рядок перед текстом
                output_file.write(reversed_content.strip())

        print("Успішно виконано. Зміст файлу збережено у зворотньому порядку.")
    
    except FileNotFoundError:
        print(f"Помилка: Файл '{input_path}' не знайдено.")
    
    except Exception as e:
        print(f"Виникла помилка: {str(e)}")


# Приклад використання
input_file_path = input("Введіть шлях до вхідного файлу: ")
output_file_path = input("Введіть шлях до вихідного файлу: ")

reverse_file(input_file_path, output_file_path)
