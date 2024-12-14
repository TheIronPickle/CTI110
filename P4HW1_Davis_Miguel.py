#Miguel Davis
#11/10/2024
#P4HW1
#Score calculator

#Initialize student score list
student_scores = []

#Get number of scores to enter
num_scores = int(input("How many scores do you want to enter? "))

#Collect and validate scores
for i in range(num_scores):
   while True:
       try:
           score = float(input(f"Enter score #{i + 1}: "))
           if 0 <= score <= 100:
               student_scores.append(score)
               break
           else:
               print("Invalid score! Please enter a score between 0 and 100.")
       except ValueError:
           print("Invalid input! Please enter a numeric value.")

#Calculate statistics
lowest_score = min(student_scores)

#Create modified list without lowest score
modified_scores = student_scores.copy()
modified_scores.remove(lowest_score)

#Calculate average of modified list
average = sum(modified_scores) / len(modified_scores)

#Display results
print('\n' + '-' * 12 + 'Results' + '-' * 12)
print(f"Lowest score entered: {lowest_score}")
print(f"\nScores after dropping lowest score: {modified_scores}")
print(f"Average of scores: {average:.2f}")

#Determine letter grade
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
print('-' * 35)