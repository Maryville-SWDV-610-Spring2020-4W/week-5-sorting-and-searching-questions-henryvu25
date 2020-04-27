def bubbleSorted(list):
    swap = True
    passing = len(list)-1
    
    while passing > 0 and swap:
        swap = False
        for index in range(passing):
            if list[index] > list[index+1]:
                swap = True
                list[index],list[index+1] = list[index+1],list[index]
        passing -= 1
    return list

print(bubbleSorted([5,4,8,2,7,10,6,-3]))
print(bubbleSorted([1,2,3,4,5,6,7,8,9,10]))
