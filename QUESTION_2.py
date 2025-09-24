## program to determine grade based on numeric score
score = float(input("Enter your score: "))

# Determine the grade based on the score
if 80 <= score <= 100:
    grade = "A"
elif 70 <= score <= 79:
    grade = "B"
elif 60 <= score <= 69:
    grade = "C"
elif 50 <= score <= 59:
    grade = "D"
elif 0 <= score <= 49:
    grade = "F"
else:
    grade = "Invalid score"
    # print out corresponding grade
print("Your grade is:", grade)