#1. Count the number of digits in a number 

'''n = int(input())
count = 0 
while n!=0:
    n//=10
    count+=1
print(count)'''

#2 . Sum of digits in a given number 
'''n = int(input())
sum = 0 
while n!=0:
    sum+=n%10
    n//=10
print(sum)'''

#3 . Even and odd digit count 

'''n = int(input("enter your number"))
odd_count = 0 
even_count = 0 
while n > 0:
    if (n%10)%2==0:
        even_count+=1
    else:
        odd_count+=1
    n//=10
print(odd_count)
print(even_count)'''

#4. Digital sum of a number 
'''n = int(input())

while n>=10:
    sum = 0
    while n>0:
        sum+=n%10
        n = n//10
    n = sum
print(n)
    '''
# #mam approach 
# n = int(input())
# while n>=10:
#     n = sum(list(map(int,str(n))))
# print(n)

#3. Check Palindrome Number
n = int(input())
s = str(n)

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")

