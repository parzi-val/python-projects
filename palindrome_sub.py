def twoSum(nums, target: int):
    index = [
        (i, j)
        for i in range(len(nums))
        for j in range(i + 1, len(nums))
        if nums[i] + nums[j] == target
    ]

    return index


print(twoSum([3, 2, 4], 6))
