infile = open("C:\\Users\\nadim\\try.txt", 'r')
sum = 0.0
count = 0
line = infile.readline()

while line !="":
    sum = sum + int(line)
    count = count +1
    line = infile.readline()
print("The avg number is ", sum / count)


