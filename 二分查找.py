def left_func(nums, target):
    n = len(nums) - 1
    left = 0
    right = n
    while (left <= right):
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid - 1
        if nums[mid] < target:
            left = mid + 1
    return left


a = left_func([5, 7, 8, 8, 9, 10], 9)
print(a)
# b = left_func(nums, target + 1)
# if a == len(nums) or nums[a] != target:
#     return [-1, -1]
# else:
#     return [a, b - 1]
