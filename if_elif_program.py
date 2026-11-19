print("===== STUDENT GRADE CALCULATOR =====")

name = input("Enter student name: ")

maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))
computer = int(input("Enter Computer marks: "))
social = int(input("Enter Social marks: "))

total = maths + science + english + computer + social
percentage = total / 5

print("\n===== RESULT =====")
print("Student Name:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")

if percentage >= 90:
    print("Grade: A+")
    print("Remarks: Outstanding Performance!")

elif percentage >= 80:
    print("Grade: A")
    print("Remarks: Excellent Work!")

elif percentage >= 70:
    print("Grade: B")
    print("Remarks: Very Good!")

elif percentage >= 60:
    print("Grade: C")
    print("Remarks: Good!")

elif percentage >= 50:
    print("Grade: D")
    print("Remarks: Average Performance")

elif percentage >= 35:
    print("Grade: E")
    print("Remarks: Just Passed!")

else:
    print("Grade: F")
    print("Remarks: Failed. Need More Practice!")

if min(maths, science, english, computer, social) < 35:
    print("Status: FAIL (Failed in at least one subject)")
else:
    print("Status: PASS")