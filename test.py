def swap(a: int, b: int) -> tuple:
    a = a^b
    b = a^b
    a = a^b
    return (a,b)

num1 = 4
num2 = 6
print(num1, num2)
num1, num2 = swap(num1, num2)
print(num1, num2)
