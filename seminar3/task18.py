# Задача 18: Требуется найти в массиве A[1..N] самый близкий
# по величине элемент к заданному числу X. Пользователь
# в первой строке вводит натуральное число N – количество 
# элементов в массиве. В последующих  строках записаны N целых 
# чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5
n=abs(int(input("Введите кольчество чисел в массиве: ")))
from random import randint
A = [randint(1,n) for i in range(n)]
x= int(input("Введите искомый элемент: "))
print(A)

m = min(A, key=lambda b: abs(b-x))
print(m)