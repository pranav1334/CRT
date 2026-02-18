#While loop to count digits in a "integer":
n = int(input())
counter = 0
while n > 0:
    counter += 1
    n //= 10
print(counter)

#For loop using range:
for counter in range(0,2,1):
    print('Hello World!') 

#To find the squares of each element in a array:
arr = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(arr)):
    arr[i] = arr[i] ** 2
print(arr)

#To find even numbers in a given range:
for eve in arr:
    if eve % 2 == 0:
        print(eve,end=' ')

#To find number of vowels in a given string:
vowels = input()
count = 0
for word in vowels:
    if word in 'aeiouAEIOU':
        count += 1
print(count)


'''
Password retry system(max 3 attempts)
if correct password entered, login successful
else ask for password 3 times
once attempts exceeded, print account locked
'''
password = "090906"
attempts = 0
while attempts < 3:
    user_input = input("Enter password: ")
    if user_input == password:
        print("Login successful")
        break
    else:
        attempts += 1
        if attempts == 3:
            print("Account locked")