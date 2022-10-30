class Solution:
    def isSubsequence(self, s: str, t: str):
        # index = [0]
        index_item = 0
        for j in s:
            try:
                index_item = t.index(j, index_item)
                # index = index_item
                # index.append(index_item)
                t = t[:index_item] + t[index_item + 1:]
            except:
                return False
        return True

a = Solution()
print(a.isSubsequence("ahb", "ahbgdc"))

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         i=0
#         j=0
#         while(j<len(t) and i<len(s)):
#             if(s[i] == t[j]):
#                 i+=1
#                 j+=1
#             else:
#                 j+=1
#         if(i==len(s)):
#             return True
#         return False