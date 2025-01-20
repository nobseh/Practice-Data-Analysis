numList = [1,2,3,3,4,6,3,2], [10,12,15,17,40,30,23], [9,5,7,4,2,6,8,4]

def duplicateSearch(numList):
    for i in range(len(numList)):
        for j in range(i+1, len(numList)):
            if num[i] == num[j]:
                return True
    return False

for num in numList:
    result = duplicateSearch(num)
    print(f'List {num} has duplicate: {result}')

