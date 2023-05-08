# Задача 26:  Посчитать 
# треугольное число (сумма чисел от 1 до N) для числа N 
# ЧЕРЕЗ РЕКУРСИЮ и 
# без циклов

N = int(input("Введите число:  "))
def faktor(N):
    
    if N==1:
        return 1
    return N+faktor(N-1)
print(faktor(N))