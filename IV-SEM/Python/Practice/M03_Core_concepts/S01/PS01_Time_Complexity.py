def LinearSearch(elements, target):
    for i in range(len(elements)):
        if elements[i] == target:
            return i    
    return -1
print(LinearSearch([12, 45, 78, 69, 32], 12)) 
print(LinearSearch([12, 45, 78, 69, 32], 32))
print(LinearSearch([12, 45, 78, 69, 32], 78))