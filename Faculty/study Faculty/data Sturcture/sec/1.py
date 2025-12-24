n = int(input("Number of Subjects , its hours = 3: "))
gpa = 0
for i in range(n):
    mark = int(input(f"Your mark in subject{i+1} "))
    if mark >= 96:
        gpa += 4

    elif 96 > mark >= 92:
        gpa += 3.7

    elif 92 > mark >= 88:
        gpa += 3.4

    elif 88 > mark >= 84:
        gpa += 3.2

    elif 84 > mark >= 80:
        gpa += 3

    elif 80 > mark >= 76:
        gpa += 2.8

    elif 76 > mark >= 72:
        gpa += 2.6

    elif 72 > mark >= 68:
        gpa += 2.4

    elif 68 > mark >= 64:
        gpa += 2.2

    elif 64 > mark >= 60:
        gpa += 2

    elif 60 > mark >= 55:
        gpa += 1.5

    elif 55 > mark >= 50:
        gpa += 1

    else:
        gpa += 0

print("your gpa = ", gpa/n)
