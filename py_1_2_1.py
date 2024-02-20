def merge_and_sort_arrays(*arrays):
  result = []

  # Об'єднання всіх масивів в один
  for array in arrays:
      result.extend(array)

  # Видалення дублікатів та чисел, які кратні 5
  result = list(set(result))
  result = [num for num in result if num % 5 != 0]

  # Сортування масиву
  result.sort()

  return result

# Приклад використання програми
array1 = [3, 8, 12, 5, 10]
array2 = [7, 2, 15, 5, 9]
array3 = [1, 6, 11, 20]

result_array = merge_and_sort_arrays(array1, array2, array3)

print("Результуючий масив:", result_array)
