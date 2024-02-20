from collections import Counter
import string

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
        return None
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return None

def preprocess_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()
    return text

def word_frequency_analysis(text):
    words = text.split()
    word_count = Counter(words)
    sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
    return sorted_word_count

def main():
    file_path = input("Введіть шлях до текстового файлу: ")
    text = read_file(file_path)

    if text is not None:
        preprocessed_text = preprocess_text(text)
        word_frequency = word_frequency_analysis(preprocessed_text)

        print("Частота вживання слів:")
        for word, count in word_frequency.items():
            print(f"{word}: {count}")

if __name__ == "__main__":
    main()
