# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12


n = int(input('Введите кол-во элементов первого множества: '))
m = int(input('Введите кол-во элементов второго множества: '))

first = set()
for i in range(n):
    first.add(int(input("Введите элемент первого множества: ")))
second = set()
for i in range(m):
    second.add(int(input("Введите элемент второго множества: ")))
result = first & second

newResult = list(result)
newResult.sort()

# for i in first:
#     for j in second:
#         if i == j:
#             result.append(i)

# newResult = set(result)
# newResult = list(newResult)
# newResult.sort()

print(*newResult)

