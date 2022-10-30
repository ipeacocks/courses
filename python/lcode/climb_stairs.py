from functools import lru_cache

class Solution:
   @lru_cache(None)
   def climbStairs(self, n: int) -> int:
       if n == 1:
           return 1
       if n == 2:
           return 2
       return self.climbStairs(n - 1) + self.climbStairs(n - 2)

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         climbs = range(0, n + 1)
#         s = [1, 1]
#         for i in climbs[2:]:
#             s.append(s[-1] + s[-2])
#         return s[-1]
    
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         climbs = range(0, n + 1)
#         s = {0:1, 1:1}
#         for i in climbs[2:]:
#             s[i] = s[i-1] + s[i-2]
#             i_prev = i
#         return s[n]


a = Solution()
print(a.climbStairs(20))