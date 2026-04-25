#frequency of eachb element in a array
# li = list(map(int, input().split()))
# d = {}
# for els in li:
#     if els not in d:
#         d[els] = 1
#     else:
#         d[els] += 1
# print(d)

# d1 = {}
# for els in li:
#     d1[els] = d1.get(els,0) + 1
# print(d1)

#Find the element with max frequency
# [1,2,4,5,2,3,1,1] ==>1
from collections import Counter
li = list(map(int, input().split()))
freq = dict(Counter(li))
print(max(freq, key=freq.get))
