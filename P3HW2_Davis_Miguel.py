#Miguel Davis
#11/2/2024
#CT110 P3HW2
#This program calculates pay based onhours worked and pay rate given.

# Get employee information from user
employee_name = input("Enter employee name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter hourly pay rate: $"))

# Calculate overtime hours and pay 
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours_worked

# Calculate overtime and regular pay
overtime_pay = overtime_hours * (pay_rate * 1.5)
regular_pay = regular_hours * pay_rate

# Calculate gross pay
gross_pay = regular_pay + overtime_pay

# Display information in format
print("\n" + "-" * 65)
print(f"Employee Name: {employee_name}")
print("Hours Worked   Pay Rate   Overtime   Overtime Pay   RegHour Pay   Gross Pay")
print("-" * 65)
print(f"{hours_worked:^11.2f}  ${pay_rate:^7.2f}  {overtime_hours:^8.2f}  ${overtime_pay:^10.2f}  ${regular_pay:^10.2f}  ${gross_pay:^8.2f}")