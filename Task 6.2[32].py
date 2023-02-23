#6.2[32]: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, 
#вычисляющую элемент по номеру строки и столбца, т.е. функцию двух аргументов. 
#Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
#Нумерация строк и столбцов идет с единицы.
def print_operation_table(operation, num_rows = 6, num_cols = 6) -> None: 
    print('    ', end=' ')
    for i in range(1, num_cols + 1):
        print(str(i).rjust(4), end= ' ')
    print()
    print('_' *16)
    for i in range(1, num_rows + 1): 
        print(i, '|', end= ' ')
        for j in range(1, num_cols + 1): 
            print(str(operation(i,j)).rjust(4), end= ' ')
        print()
print(print_operation_table(lambda x, y: x**y, 4, 4))