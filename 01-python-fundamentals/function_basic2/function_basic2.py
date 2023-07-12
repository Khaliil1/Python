def  down(num):
    countDown = []

    for i in range(num, -1, -1):

        countDown.append(i)
    return countDown
print(down(10))


def printReturn(list):

    print(list[0])

    return list[1]

print (printReturn([10,100]))


def length(list):

    print(list[0])

    return len(list)
print(length([10,100,1]))


def valueLength(length,value):
    new_list = []
    for i in range(length):
        new_list.append(value)
    return new_list
print(valueLength(3,8))