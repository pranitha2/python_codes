n = int(input("enter a number : "))
mul = 1

while n != 0:

    res = n % 10

    mul = mul * res

    n = n // 10

print(mul)
