nums = [-2,1,-3,4,-1,2,1,-5,4]
max_sum = cur_sum = 0

# for i in range(0, len(nums)):
#     for j in range(i, len(nums)):
#         print(nums[i:j+1])
#         cur_sum = sum(nums[i:j+1])
#         max_sum = max(max_sum, cur_sum)
# print(max_sum)


for num in nums:
    cur_sum = max(num, cur_sum + num)
    max_sum = max(cur_sum, max_sum)
print(max_sum)