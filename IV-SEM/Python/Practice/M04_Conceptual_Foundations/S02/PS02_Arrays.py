# a = [10,23,45,65,1,2,3]
# a.sort()
# print(a[::-1])

# a = [10,23,45,65,1,2,3]
# a.sort()
# a.reverse()
# print(a)

# a = [10,23,45,65,1,2,3]
# rev=[]
# for i in range(len(a)):
#     rev.append(a[len(a)-1-i])
# print(rev)    

'''
#input : [12,45,36,78,96]
#output : [96,78,36,45,12]
#traditional way
li = [12,45,36,78,96]
res=[]
stop = -1 * (len(li) + 1)
for i in range(-1,stop,-1):
    res.append(li[i])
print(res)
#list comprehension
res1 = [li[i] for i in range(-1,stop,-1)]
print(res1)\

#using swapping
li = [12,45,36,78,96]
n = len(li)
print("Before reversing:",li)
for i in range(n//2):
    li[i],li[n-1-i] = li[n-1-i],li[i]
print("After reversing:",li)
'''
'''
li = [12,45,36,78,96]
res = []
for ele in li:
    #res.insert(0,ele)
    res = [ele] + res
print(res)
'''
#check if an array is sorted 
#input : [12,23,45,56,69,100] ==> True
#input : [12,45,36,78,96] ==> False
def check_sorted(li):
    for i in range(len(li)-1):
        if li[i] > li[i+1]:
            return False
    return True
print(check_sorted([12,45,36,78,96]))
print(check_sorted([12,23,45,56,69,100]))




