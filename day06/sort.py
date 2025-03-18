studentMarks = []
s1 = int(input("Enter Marks : "))
studentMarks.append(s1)
s2 = int(input("Enter Marks : "))
studentMarks.append(s2)

s3 = int(input("Enter Marks : "))
studentMarks.append(s3)

s4 = int(input("Enter Marks : "))
studentMarks.append(s4)

s5 = int(input("Enter Marks : "))
studentMarks.append(s5)

studentMarks.sort()

print(studentMarks)

print(sum(studentMarks))

print(len(studentMarks))

print(sum(studentMarks) / len(studentMarks))
