# Miguel Davis
# 10/22/2024
# P3HW1
# This program takes a number grade, determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list
print()

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

#determine lowest, highest , sum and average for grades

lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

print('\n' + '-' * 12 + 'Results' + '-' * 12)
print(f"Lowest grade: {lowest}")
print(f"Highest grade: {highest}")
print(f"Sum of grades: {total}")
print(f"Average grade: {average:.2f}")

print('-' * 32)

#determine letter grade for average
if average >= 90: 
    print('Your grade is: A')
else:
    if average > 80:
        print('Your grade is: B')
    else:
        if average > 70:
            print('Your grade is: C')
        else:
            if average > 60:
                print('Your grade is: D')
            else:
                print('Your grade is: F') 

