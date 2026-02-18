# #Factorial 
# '''import math 

# n = int(input())
# print(math.factorial(n))'''

# #Amstrong number 

# # n = list(map(int,input().split()))
# # count = 0 
# # for _ in range(len(n)):
# #     count+=1
# #     for i in range(len(n)):
# #         if i**count == j:
# #             print("Yes")
# #         else:
# #             print("No")


# '''n = input()            
# power = len(n)

# total = 0
# for digit in n:
#     total += int(digit) ** power

# if total == int(n):
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")'''

'''lis = list(map(int, input().split()))

if lis == sorted(lis) or lis == sorted(lis, reverse=True):
    print("Monotonic")
else:
    print("Not Monotonic")
'''
    
#reverse an integer 
# n = int(input())
# s = str(n)

# rev = (s[::-1])
# j = int(rev)
# print(j)


# n = int(input())
# num = 0 
# while n>0:
#     digit = n%10
#     num = num*10+digit
#     n//=10
# print(num)

n = int(input())
romanlis = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
numlis   = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
ans = ""
for i in range(len(romanlis)):
    while n >= romanlis[i]:
        ans += numlis[i]
        n -= romanlis[i]
print(ans)
