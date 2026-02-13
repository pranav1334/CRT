# li = [1, 2, 3, 4, 5]
# res =[]
# for ele in li:
#     res.append(ele*2)

# print([ele*2 for ele in li])

# li = [1, 2, 3, 4, 5]
# res =[]
# for i in li:
#     if i%2 == 0:
#         res.append(i)
# print(res)
# print([i for i in li if i%2 == 0])
# print((i for i in li if i%2 == 0))
# print({i:i*2 for i in li if i%2 == 0})

# li1 = ['a', 'b', 'c']
# res =" "
# for i in li1:
#     res = res + i + " "
# print(res)

# print(" ".join(li1))
    

# n = int(input("enter number:"))
# for i in range(1, n + 1):
#     print(" "*(n - i) +"* "*i)

# dimond pattern
n = int(input("Enter number: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)

