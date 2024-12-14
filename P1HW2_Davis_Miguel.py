# Miguel Davis
# 10/4/2024
# P1HW1
# Calculator for exponents, addition and subtraction

print("This program calculates and displays travel expenses")

b = int(input("Enter Budget: $"))
dest = str(input("Enter your travel destination: "))
gas = int(input("How much do you think you will spend on gas? $"))
hot = int(input("Approximately, how much will you need for accomodation/hotel? $"))
food = int(input("Last, how much do you need for food? $"))
bal = b - gas - hot - food

print()
print("------------Travel Expenses------------")
print("Location: ", dest)
print("Initial Budget: ", b)
print()
print("Fuel: $", gas)
print("Accomodation: $", hot)
print("Food: $", food)
print()
print("Remaining Balance: $", bal)
