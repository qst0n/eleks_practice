def calculate_pascal_row(row_number):
    row = [1]

    for i in range(1, row_number + 1):
        
        new_element = row[i - 1] * (row_number - i + 1) // i
        row.append(new_element)

    return row

def print_pascal_row(row_number):
    if row_number < 0:
        print("Номер рядка повинен бути не менше 0.")
        return

    row = calculate_pascal_row(row_number)
    print(f"Рядок трикутника Паскаля №{row_number}: {row}")


try:
    row_number_input = int(input("Введіть номер рядка трикутника Паскаля: "))
    print_pascal_row(row_number_input)
except ValueError:
    print("Будь ласка, введіть ціле число.")
