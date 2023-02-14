#5.2[28]: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Циклы использовать нельзя
#Примеры/Тесты:
#<function_name>(0,0) -> 0
#<function_name>(0,2) -> 2
#<function_name>(3,0) -> 3
def Sum_Number(a, b):
    if a == 0:
        return b
    return Sum_Number(a-1, b+1)
print(Sum_Number(0,0))
print(Sum_Number(0,2))
print(Sum_Number(3,0))


   