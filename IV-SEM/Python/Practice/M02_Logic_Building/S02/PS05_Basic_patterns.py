#1. Sqaure Star Pattern
n = int(input())
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

#2. Right Angle Triangle Star Pattern
n = int(input())
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()

#3. Inverted Right Angle Triangle Star Pattern 
n = int(input())
for i in range(n):  
    for j in range(n-i):  
        print("*", end=" ")  
    print()

#4. Number triangle pattern
n = int(input())
for i in range(n):
    for j in range(i+1):
        print(j+1, end=" ")
    print()