strs = ["flower","flow","flight"]
strs_2 = ["testic","testing","testqa"]
strs_3 = ["a"]
strs_4 = ["a", "a"]
strs_5 = ["abc", "a"]
strs_6 = ["a", "abc"]
strs_7 = [""]
strs_8 = ["c","acc","ccc"]


# def longestCommonPrefix(strs):
#     for i in range(1, len(strs[0]) + 1): # amount of letters in first word
#         first_letters = strs[0][:i]
#         # print(first_letters)
#         for j in strs:
#             if first_letters not in j:
#                 return strs[0][:i-1]
#             elif first_letters == strs[0]:
#                 return strs[0]

# a = longestCommonPrefix(strs)
# print(a)


class Solution:
    def longestCommonPrefix(self, strs):
        for i in range(1, len(strs[0]) + 1): # amount of letters in first word
            first_letters = strs[0][:i]
            for j in strs:
                if not j.startswith(first_letters):
                    return strs[0][:i-1]
        return strs[0]


a = Solution()
print(a.longestCommonPrefix(strs))
print(a.longestCommonPrefix(strs_2))
print(a.longestCommonPrefix(strs_3))
print(a.longestCommonPrefix(strs_4))
print(a.longestCommonPrefix(strs_5))
print(a.longestCommonPrefix(strs_6))
print(a.longestCommonPrefix(strs_7))
print(a.longestCommonPrefix(strs_8))