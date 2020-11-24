def sortNums(nums):
    # constant space solution
    i = 0
    j = len(nums) - 1
    index = 0
    while index <= j:
        if nums[index] == 1:
            nums[index], nums[i] = nums[i], nums[index]
            index += 1
            i += 1
        if nums[index] == 2:
            index += 1
        if nums[index] == 3:
            nums[index], nums[j] = nums[j], nums[index]
            j -= 1
    return nums


print(sortNums([2, 3, 2, 2, 3, 2, 3, 1, 1, 2, 1, 3]))
