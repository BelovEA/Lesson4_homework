compr = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_compr = [compr[el] for el in range(1, len(compr)) if compr[el] > compr[el - 1]]
print(new_compr)
