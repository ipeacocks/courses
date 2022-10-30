class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for index, num in enumerate(nums):
            if index - 1 >= 0 and nums[index - 1] == nums[index]:
                nums[index-1] = "_"
        while "_" in nums:
            nums.remove("_")
        return len(nums)

# nums[:] = sorted(set(nums))
# return len(nums)

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
        
#         length = 0
#         if len(nums) == 0: return length
#         for i in range(1,len(nums)):
#             if nums[length] < nums[i]:
#                 length += 1
#                 nums[length] = nums[i]
#         return length+1