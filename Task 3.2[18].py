#3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X. 
#Пользователь вводит это число с клавиатуры, список можно считать заданным. 
#Введенное число не обязательно содержится в списке.
#Примеры/Тесты:
#Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
#Output: 2
#Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9
list_1 = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
X = int(input('Введите число: '))
i = 0
minimal_difference = abs(X - list_1[i])
for i in range (len(list_1)):
    if abs(X-list_1[i]) <= minimal_difference:
        minimal_difference = abs(X-list_1[i])
        adjacent_number = list_1[i]
print(adjacent_number)
    

    