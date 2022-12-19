def fact_number(number):
    num = 1
    for i in range(number + 1):
        yield f"{i}! = {num}"
        num *= i + 1
for el in fact_number(int(input("enter factorial number: "))):
    print(el)