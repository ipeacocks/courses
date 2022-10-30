class Solution:
    def removeElement(self, nums, val):
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return nums, i

a = Solution()
nums = [0,1,2,2,3,0,4,2]
print(a.removeElement(nums, 2))


# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         while val in nums:
#             nums.remove(val)
#         return len(nums)