def string_alternative(word):
    list1 = []
    list2 = []
    list1 = word.split(" ")
    # print(list1)
    for i in list1:
        # print(i)
        str1 = ''
        for j in range(len(i)):
            if j % 2 == 0:
                str1 += i[j]
        list2.append(str1)
    return list2
if __name__=='__main__':
    W = input("Enter a word..")
    x = string_alternative(W)
    print(x)
