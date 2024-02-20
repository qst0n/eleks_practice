import re

def count_word_occurrences(word, mode, file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            if mode == 1:
                occurrences = content.lower().count(word.lower())
            elif mode == 2:
                # Використовуємо регулярний вираз для знаходження окремих слів
                words = re.findall(r'\b\w+\b', content.lower())
                occurrences = sum(1 for w in words if w == word.lower())
            else:
                print("Невірний режим роботи. Використовуйте 1 або 2.")
                return  # Завершує виконання функції в разі невірного режиму

            print(f"Слово '{word}' згадане {occurrences} разів.")
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")


word_to_search = input("Введіть слово для пошуку: ")
mode_to_use = int(input("Виберіть режим (1 або 2): "))
file_path_input = input("Введіть шлях до текстового файлу: ")

count_word_occurrences(word_to_search, mode_to_use, file_path_input)
