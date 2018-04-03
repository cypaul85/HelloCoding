def CustomSort(array):
    i = 0
    j = len(array)-1
    counter = 0

    while j>i:
        while array[i]%2==0:
            i+=1
        
        while array[j]%2==1:
            j-=1
        
        if i>j:
            break
        
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
        counter += 1
    return array, counter
    
print(CustomSort([3,4,5,6,7,8,9,10]))