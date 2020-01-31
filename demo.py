moredata = "yes"
Sum = 0.0
COUNT = 0
while moredata[0] == 'y':
    x = int(input("Enter a number>>"))
    Sum = Sum + x
    COUNT = COUNT +1
    moredata = input("Do you have any number?yes/no")
    print("The average number is ", Sum / COUNT)
