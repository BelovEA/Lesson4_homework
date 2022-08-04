from sys import argv
def wages():
    try:
        prod_hour, value_hour, prem = argv
        print(f"Заработная плата сотрудника - {(prod_hour * value_hour) +prem}")
    except ValueError:
        print("Введите 3 числа(целое или вещественное), а не строку!")

