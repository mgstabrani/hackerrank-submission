n = int(input())
for i in range(n):
    grade = int(input())
    if(grade % 5 > 2 and grade >= 35):
        grade += 5 - (grade % 5)
    print(grade)