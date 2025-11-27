import sys

if len(sys.argv) == 6:
    marks = list(map(float, sys.argv[1:6]))
    print("User provided marks:")
else:
    marks = [85, 90, 78, 88, 92]
    print("No input given - using default marks:")

avg = sum(marks) / 5

print("Average Marks:", avg)

if avg >= 90:
    grade = "A"
elif avg >= 75:
    grade = "B"
elif avg >= 60:
    grade = "C"
elif avg >= 40:
    grade = "D"
else:
    grade = "Fail"

print("Grade:", grade)
