#Create a marks percentage calculator:
#Ask user to input marks for 5 subjects (input as strings), Convert them to integers
#Calculate the total and percentage
#Print percentage along with a grade: A (90+), B (80-89), C (70-79), Fail (<70)

subject1 = int(input("Please enter your subject 1 marks: "))
subject2 = int(input("Please enter your subject 2 marks: "))
subject3 = int(input("Please enter your subject 3 marks: "))
subject4 = int(input("Please enter your subject 4 marks: "))
subject5 = int(input("Please enter your subject 5 marks: "))

total_marks = subject1 + subject2 + subject3 + subject4 + subject5
percentage = (total_marks / 500) * 100

# Grade calculation
if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "Fail"
else:
    grade = "Fail"

# Print result (outside if-else)
print(f"\nTotal Marks: {total_marks}")
print(f"Your Percentage is: {percentage:.2f}%")
print(f"Your Grade is: {grade}")
