#1.3[6]. Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
#Вам требуется написать программу, которая проверяет счастливость билета.
num = int(input('Введите номер билета '))
summa1 = num // 100000 + num // 10000 % 10 + num // 1000 % 10
summa2 = num // 100 % 10 + num // 10 % 10 + num % 10
if summa1 == summa2:
    print('yes')
else:
    print('no')

#(*) Усложнение. Вывод результат на экран сделайте одной строкой(только один print), 
#для этого используйте тернарный оператор
num = int(input('Введите номер билета '))
summa1 = num // 100000 + num // 10000 % 10 + num // 1000 % 10
summa2 = num // 100 % 10 + num // 10 % 10 + num % 10
print('yes' if summa1 == summa2 else 'no')