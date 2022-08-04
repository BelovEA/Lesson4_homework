from random import randint #используем модуль randint для выборки чисел
my_list = [randint(0, 15) for _ in range(15)] #создаём переменную my_list, поместим туда выборку чисел с помощью модуля randint
print(my_list)
my_dict = {i: 0 for i in my_list} #формируем словарь каждого элемента данного списка, т.к. ключи уникальны
for i in my_list: #создаём for для подсчёта кол-ва одинаковых элементов
    my_dict[i] += 1 #подсчёт элемента внутри цикла
print([i for i in my_dict if my_dict[i] == 1]) #создаём генератор с выводом только для уникальных элементов
