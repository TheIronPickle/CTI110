# Miguel Davis
# 10/22/2024
# P2HW1
# Calculator for exponents, addition and subtraction

print("This program calculates and displays travel expenses")

budget = float(input("Enter budget: $"))
dest = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? $"))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? $"))
food = float(input("Last, how much do you need for food? $"))


total_expenses = gas + accommodation + food
remaining_budget = budget - total_expenses


print("\n" + "-" * 12 + "Travel Expenses" + "-" * 12)
print(f"Location: {' ' * (32 - len('Location: '))} {dest}")
print(f"Initial Budget: {' ' * (32 - len('Initial Budget: '))} ${budget:.2f}")
print(f"Fuel: {' ' * (32 - len('Fuel: '))} ${gas:.2f}")
print(f"Accommodation: {' ' * (32 - len('Accommodation: '))} ${accommodation:.2f}")
print(f"Food: {' ' * (32 - len('Food: '))} ${food:.2f}")
print("-" * 40)
print()
print(f"Remaining Balance: ${remaining_budget:.2f}")
