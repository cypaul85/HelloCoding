def sum(arr):
    total = 0
    for i in arr:
        total += i
    return total

def count(list):
    #print(list)

    if list == []:
        return 0
    return list[0] + count(list[1:])

def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

def min(list):
    if len(list) == 2:
        return list[0] if list[0] < list[1] else list[1]
    
    sub_min = min(list[1:])

    return list[0] if list[0] < sub_min else sub_min


print(max([1, 2, 3, 14, 5, 6, 7, 8, 9, 10]))
print(min([1, 2, 3, 14, 5, 6, 7, 8, 9, 10]))
print(count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(sum([1,2,3,4]))