# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

def func(chislo, stepen):
    if stepen == 1:
        return chislo
    return chislo * func(chislo, stepen - 1)

chislo = int(input('Введите число\n'))
stepen = int(input('Введите степень числа\n'))
print(func(chislo, stepen))