def missingAndRepeating(nums, n):
    res = []
    i, f = 0, False
    while i < len(nums):
        while nums[i] != i+1:
            if nums[nums[i] - 1] == nums[i]:
                res.append(nums[i])
                f = True
                break
            nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        if f: break
        i += 1
    res.append(int((n*(n+1)/2) - sum(nums)+res[0]))
    return reversed(res)
