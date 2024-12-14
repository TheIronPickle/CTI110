#Miguel Davis
#11/10/2024
#P4HW2
#Pay calculator

#Initialize running totals
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

while True:
    #Get employee name and establish "done" as sentinel
    employee_name = input("\nEnter employee name (or 'Done' to finish): ")
    
    #Check for sentinel value to end program
    if employee_name.lower() == 'done':
        break
        
    #Get employee pay information
    hours_worked = float(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter hourly pay rate: $"))
    
    #Calculate overtime hours and pay
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours_worked
    
    #Calculate pays for this employee
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay
    
    #Update running totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1
    
    #Display individual employee information
    print("\n" + "-" * 65)
    print(f"Employee Name: {employee_name}")
    print("Hours Worked   Pay Rate   Overtime   Overtime Pay   RegHour Pay   Gross Pay")
    print("-" * 65)
    print(f"{hours_worked:^11.2f}  ${pay_rate:^7.2f}  {overtime_hours:^8.2f}  ${overtime_pay:^10.2f}  ${regular_pay:^10.2f}  ${gross_pay:^8.2f}")

#After loop ends, display final totals
print("\n" + "=" * 50)
print("FINAL TOTALS")
print("=" * 50)
print(f"Total Number of Employees: {employee_count}")
print(f"Total Overtime Pay: ${total_overtime_pay:,.2f}")
print(f"Total Regular Pay: ${total_regular_pay:,.2f}")
print(f"Total Gross Pay: ${total_gross_pay:,.2f}")