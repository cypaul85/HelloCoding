def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        
        less = [i for i in arr[1:] if i< pivot]
        greater = [i for i in arr[1:] if i > pivot]

        return quickSort(less)+[pivot]+quickSort(greater)

print(quickSort([10,5,2,3]))

arr = [1,2,3,4,5,6,7,8,9,10]

less = [element for element in arr[5:] if element > 2]
print(less)