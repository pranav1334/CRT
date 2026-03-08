'''set:
1.use {} to create a set
2.set does not allow duplicates
3.set unindexed
4.set is unordered
'''
# s = {True, 10, 12.45, 10, 1, 9+5j}
# print(s,type(s))
# print(s[3])


# adding elements
A = {1, 2, 3}
B = {3, 4, 5}
A.add(4)
B.update({6,7})
print(A,B)
# removing elements
A.pop()
print(A)
print(help(set))