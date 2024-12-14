#Miguel Davis
#11/2/2024
#P4Lab2
#Multiplication table

while True:
    # Get user input
    number = int(input("Enter a positive integer: "))
    
    # Check if number is negative
    if number < 0:
        print("This program does not handle negative numbers.")
    else:
        # Display multiplication table using for loop
        print(f"\nMultiplication table for {number}:")
        for i in range(1, 13):
            print(f"{number} x {i} = {number * i}")
    
    # Ask if user wants to continue
    choice = input("\nDo you want to run the program again? (yes/no): ").lower()
    if choice != "yes":
        break

print("Exiting program...")
input("Press Enter to close...")