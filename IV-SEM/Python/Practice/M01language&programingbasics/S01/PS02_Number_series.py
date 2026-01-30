# n= int(input()("Enter a number:"))
# for i in range(1,n+1):
#     print(i)
     
n = int(input("Enter number of terms: "))

f = 1

for i in range(1, n + 1):
    f*= i
    print(f, end=" ")

