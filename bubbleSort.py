def bubbleSort(list):
    for passing in range(len(list)-1,0,-1):
        for index in range(passing):
            if list[index] > list[index+1]:
                list[index],list[index+1] = list[index+1],list[index]
                
                

list = [5,4,8,2,7,10,6,-3]

bubbleSort(list)
print(list)