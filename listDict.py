phoneList = []

phoneList.append(['Bob','555-1234'])
phoneList.append(['Jane','432-7890'])
phoneList.append(['Chris','653-9283'])
phoneList.append(['Jill','103-4583'])
phoneList.append(['Wendy','849-4638'])
phoneList.append(['Marvin','757-4537'])

print(phoneList)

def findNumber(name):
    for each in phoneList:
        if each[0] == name:
            return each[1]
        
print(findNumber('Bob'))        
        
phoneDict = {}

phoneDict['Bob'] = '555-1234'
phoneDict['Jane'] = '432-78904'
phoneDict['Chris'] = '653-9283'
phoneDict['Jill'] = '103-4583'
phoneDict['Wendy'] = '849-4638'
phoneDict['Marvin'] = '757-4537'

print(phoneDict)
print(phoneDict['Jill'])
    