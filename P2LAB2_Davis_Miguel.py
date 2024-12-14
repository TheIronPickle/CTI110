#Miguel Davis
#10/13/2024
#P2LAB2
#Car mileage calculator

Car_Models = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

print(Car_Models.keys())

vehicle = input("Enter a vehicle to see its MPG: ")
mpg = Car_Models.get(vehicle)

print(f"The {vehicle} gets {mpg} mpg.")
miles = float(input("How many miles will you drive the {vehicle}? "))
gallons_needed = miles / mpg
print(f"{gallons_needed:.2f} gallons of gas are needed to drive the {vehicle} {miles} miles.")
