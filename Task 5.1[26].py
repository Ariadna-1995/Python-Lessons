#5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b. 
#Разрешается использовать только операцию умножения. Циклы использовать нельзя
#Примеры/Тесты:
#<function_name>(2,0) -> 1
#<function_name>(2,1) -> 2
#<function_name>(2,3) -> 8
#<function_name>(2,4) -> 16
def Number_Degree(a, b):
    if b == 0: 
        return 1
    result = Number_Degree(a,b-1) * a
    return result
print(Number_Degree(2,0))
print(Number_Degree(2,1))
print(Number_Degree(2,3))
print(Number_Degree(2,4))