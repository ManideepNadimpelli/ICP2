infile = open("C:\\Users\\nadim\\try.txt", 'r')
line = infile.readline()
count = 0
op = {}
while line != "":
    for word in line.split():
        if word in op:
            op[word] = op[word] + 1
        else:
            op[word] = count + 1
    line = infile.readline()
print(op)
outfile = open('out.txt', 'w')
outfile.write(str(op))
outfile.close()