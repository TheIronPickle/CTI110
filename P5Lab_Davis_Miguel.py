#Miguel Davis
#11/17/2024
#P5Lab
#Self-Checkout



import random

def disperse_change(amount):
    if amount == 0:
        print("No change due")
        return
    
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

    print("Change due:", " ".join(output))

def main():
    # Generate random purchase amount
    purchase_amount = round(random.uniform(0.01, 100.00), 2)
    print(f"Purchase total: ${purchase_amount:.2f}")
    
    # Get payment from user
    while True:
        try:
            payment = float(input("Enter payment amount: $"))
            if payment < purchase_amount:
                print(f"Insufficient payment. Please enter at least ${purchase_amount:.2f}")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid dollar amount.")
    
    # Calculate change
    change = round(payment - purchase_amount, 2)
    
    # Display change and break it down into denominations
    if change > 0:
        print(f"Change due: ${change:.2f}")
        disperse_change(change)
    else:
        print("Exact payment received - no change due")

# Run the program
if __name__ == "__main__":
    main()