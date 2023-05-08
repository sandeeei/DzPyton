# Задача 26:  Посчитать факториал (произведение 1 до N) 

# ЧЕРЕЗ РЕКУРСИЮ и 
# без циклов

N = int(input("Введите число:  "))
def faktor(N):
    
    if N==1:
        return 1
    return N*faktor(N-1)
print(faktor(N))