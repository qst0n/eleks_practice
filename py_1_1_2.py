def fibonacci(n):
  a_n = 0
  a_0 = 0
  a_1 = 1

  if n < 0:
    print("Введіть додатне число для знаходження числа Фібоначчі.")

  elif n == 1 or n == 2:
    return 1
    
  elif n >= 0:
    for _ in range(n - 1):
        a_n = a_0 + a_1
        a_0 = a_1
        a_1 = a_n
    return a_n
  
index = int(input("Введіть індекс числа Фібоначчі, якого ви хочете знайти:\n"))

print(f"Число з індексом {index} у списку Фібоначчі це : {fibonacci(index)}.")
