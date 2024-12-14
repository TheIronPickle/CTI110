# Miguel Davis
# 10/4/2024
# P1HW1
# Calculator for exponents, addition and subtraction

print("-----Calculating Exponents----")
print()

base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))

power = pow(base, exponent)
print()
print(base, "raised to the power of", exponent, "is", power, "!!")


print("-----Addition and Subtraction----")
print()

integer = int(input("Enter a starting integer: "))
add = int(input("Enter an integer to add: "))
sub = int(input("Enter an integer to subtract: "))

ans = integer + add - sub
print()
print(i, "+ ", add, "-", sub, "is equal to", ans)


