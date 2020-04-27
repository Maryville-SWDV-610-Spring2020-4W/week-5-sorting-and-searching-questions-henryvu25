def selectionSort(list):
    for lastIndex in range(len(list)-1,0,-1):
        positionOfMax = 0
        for index in range(1,lastIndex+1):
            if list[index]>list[positionOfMax]:
                positionOfMax = index
        
        if positionOfMax != lastIndex:
            temp = list[lastIndex]
            list[lastIndex] = list[positionOfMax]
            list[positionOfMax] = temp
        
    return list

print(bubbleSorted([5,4,8,2,7,10,6,-3]))
print(selectionSort([1,2,3,4,5,6,7,8,9,10]))