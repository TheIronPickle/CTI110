#Miguel Davis
#10/22/2024
#P2HW2
#Grades entered in a list
#Pseudocode / detail algorithm 
# input modules 1-6 test results as a list "grades"
# calculate sum and average, display after lowest and highest grade


grades = []

print("Enter grade for Module 1:", end=" ")
grade = float(input())
grades.append(grade)

print("Enter grade for Module 2:", end=" ")
grade = float(input())
grades.append(grade)

print("Enter grade for Module 3:", end=" ")
grade = float(input())
grades.append(grade)

print("Enter grade for Module 4:", end=" ")
grade = float(input())
grades.append(grade)

print("Enter grade for Module 5:", end=" ")
grade = float(input())
grades.append(grade)

print("Enter grade for Module 6:", end=" ")
grade = float(input())
grades.append(grade)

lowest_grade = min(grades)
highest_grade = max(grades)
sum_grades = sum(grades)
average = sum_grades / len(grades)

print("\n" + "-" * 12 + " Results " + "-" * 12)
print(f"{'Lowest grade:':<15} {lowest_grade:>6.1f}")
print(f"{'Highest grade:':<15} {highest_grade:>6.1f}")
print(f"{'Sum of grades:':<15} {sum_grades:>6.1f}")
print(f"{'Average:':<15} {average:>6.2f}")
print("-" * 31)