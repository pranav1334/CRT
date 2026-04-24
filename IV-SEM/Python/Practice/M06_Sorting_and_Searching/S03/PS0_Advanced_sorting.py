#merge sort 
# def Merge(left,right):
#     i,j=0,0
#     result=[]
#     while i<len(left) and j<len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
# print(Merge([7,14],[3,12]))

# def MergeSort(nums):
#     if len(nums) <= 1:
#        return nums
#     mid = len(nums) // 2
#     left = nums[:mid]
#     right = nums[mid:]
#     left_sorted = MergeSort(left)
#     right_sorted = MergeSort(right)
#     return Merge(left_sorted, right_sorted)
# print(MergeSort([14,7,3,12]))

#quick sort
def Partition(arr,low,high):
    pivot = arr[low]
    i,j=low+1,high
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break
    arr[low],arr[j]=arr[j],arr[low]
    return j
print(Partition([14,7,3,12],0,3))