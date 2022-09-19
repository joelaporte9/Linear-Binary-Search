import random

# Ask user for for array length and number to seach for

arraySize = int(input("Enter size of the array: "))
numberSearch = int(input("Enter number to search for: "))

# Linear Search 
# Big O for linear search O(n)

def linearSearch(arrayList, number):
    print("_____________________")
    print("    LINEAR SEARCH     ")
    linCount = 0
    for i in range(len(arrayList)):
        linCount += 1 
        if arrayList[i] == number:
            # Returns found number you asked to seach for  
            print (f'Found {number}')
            return (f'Linear Search for {number} took {linCount} steps!')

    print ('Not found!')
    return (f'Linear Search for {number} took {linCount} steps!')

# Binary Search 
# Big O for Binary Search O(log n)

def binarySeach(arrayList, number):
    print("_____________________")
    print("    BINARY SEARCH    ")

# Sorts random array

    arrayList.sort()

# Start Binary Search
    low = 0 
    high = len(arrayList) -1
    mid = 0 
    binCount = 0
    
    while(low <= high):
        binCount += 1
        mid = (low + high) // 2
        if (number ==  arrayList[mid]):
            # Returns found number you asked to seach for  
            print (f'Found {number}')
            return (f'Binary Search for {number} took {binCount} steps!')

        elif(number < arrayList[mid]):
            high = mid - 1   
        else:
            low = mid + 1 

    # Prints the number of loops it took to find the number 
    
    print ('Not found!')
    return (f'Binary Search for {number} took {binCount} steps!')

# Creates random array from inputed integer 

def getRandomArray(number):
    print("_____________________")
    print("    RANDOM ARRAY     ")
    array = []
    for x in range (number):
        array.append(random.randrange(0, number))
        
    return array

# Converts the array size to a list to be printed out 

arrayList = getRandomArray(arraySize)

# Prints random array

print(arrayList)

# Prints the results of the linear and binary search

print(linearSearch(arrayList, numberSearch))
print(binarySeach(arrayList, numberSearch))



