from functools import reduce
def my_func(prev_el, el):
    return prev_el * el
el_list = [el for el in range(100, 1001, 2)]
print(reduce(my_func, el_list))