def insertionSort(list):
    for index in range(1,len(list)):
        savedValue = list[index]
        currentPosition = index
        
        while currentPosition > 0 and list[currentPosition-1] > savedValue:
            list[currentPosition] = list[currentPosition-1]
            currentPosition -= 1
            
        list[currentPosition] = savedValue
        
    return list

print(insertionSort([5,4,8,2,7,10,6,-3]))
print(insertionSort([1,2,3,4,5,6,7,8,9,10]))