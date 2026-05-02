
def subarraySum(nums, k):
    d = {0:1}
    pref_sum = 0
    count = 0
    for els in nums:
        pref_sum +=els
        if pref_sum - k in d:
            count +=d[pref_sum-k]
        d[pref_sum] = d.get(pref_sum,0)+1
    return count        