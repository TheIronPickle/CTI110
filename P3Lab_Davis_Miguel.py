#Miguel Davis
#10/22/2024
#P3Lab
#Calculating efficient change

# Get dollar amount from user
amount = float(input("Enter the amount of money as a float: $"))

# Check for zero amount
if amount == 0:
    print("Error: Amount cannot be zero")
else:
    # Convert to cents (integer)
    cents = int(amount * 100)

    # Initialize dictionary for currency units
    currency = {
        "dollar": 100,
        "quarter": 25,
        "dime": 10,
        "nickel": 5,
        "penny": 1
    }

    # Initialize dictionary for plural forms
    plurals = {
        "dollar": "dollars",
        "quarter": "quarters",
        "dime": "dimes",
        "nickel": "nickels",
        "penny": "pennies"
    }

    # Calculate and display results
    remaining = cents
    output = []

    for unit, value in currency.items():
        count = remaining // value
        if count > 0:
            # Choose singular or plural form
            unit_name = unit if count == 1 else plurals[unit]
            output.append(f"{count} {unit_name}")
            remaining = remaining % value

    # Print results
    print(" ".join(output))