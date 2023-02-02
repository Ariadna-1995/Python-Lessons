#1.1[2]. Найдите сумму цифр трехзначного числа. 
#Используйте f-строки чтобы оформить красивый вывод
num = int(input('Введите трехзначное число: '))
num = abs(num)
sum_digits = 0 
while num > 0:
    sum_digits = sum_digits + num % 10
    num = num//10
print(f'Сумма цифр трехзначного числа равна {sum_digits}')

#(*) Усложнение. Решите для числа произвольной разрядности: 
#произвольное количество цифр в числе.
num = int(input('Введите число: '))
num = abs(num)
sum_digits = 0 
while num > 0:
    sum_digits = sum_digits + num % 10
    num = num//10    
print(f'Сумма цифр числа равна {sum_digits}')


