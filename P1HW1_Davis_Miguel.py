# Miguel Davis
# 10/4/2024
# P1HW1
# Calculator for exponents, addition and subtraction

print("-----Calculating Exponents----")
print()

b = int(input("Enter an integer as the base value: "))
e = int(input("Enter an integer as the exponent: "))

z = pow(b, e)
print()
print(b, "raised to the power of", e, "is", z, "!!")


print("-----Addition and Subtraction----")
print()

i = int(input("Enter a starting integer: "))
a = int(input("Enter an integer to add: "))
s = int(input("Enter an integer to subtract: "))

q = i + a - s
print()
print(i, "+ ", a, "-", s, "is equal to", q)


