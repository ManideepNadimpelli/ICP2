N = input("Enter number of students..")
list1 = []
for i in range(int(N)):
    W = input("Enter weight of students..")
    list1.append(int(W))
out = [round(a*0.6) for a in list1]
print("Weights of students", out)
