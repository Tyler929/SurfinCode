def fact(b):
    a = 1
    for i in range(1,b+1):
        a = a * i
    return a
b = 3
number = fact(b)
print(number)
