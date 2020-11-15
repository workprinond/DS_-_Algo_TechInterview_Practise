def findSum(nums, target):
    target -= 30
    map = {}
    maximum = -1
    ans = [-1,-1]
    for i in range(len(nums)):
        if nums[i] not in map:
            map[target - nums[i]] = i
        else:
            if nums[i] > maximum or target - nums[i] > maximum:
                ans[0] = map[nums[i]]
                ans[1] = i
                maximum = max(nums[i],target - nums[i])
    if ans != [-1,-1]:
        return ans
    else:
        return []