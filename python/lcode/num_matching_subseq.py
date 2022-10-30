# not done
class Solution:
    def numMatchingSubseq(self, s, words):
        # counter = len(words)
        # t = s
        # for word in words:
        #     index_item = 0
        #     s = t
        #     for letter in word:
        #         # print(letter)
        #         try:
        #             index_item = s.index(letter, index_item)
        #             s = s[:index_item] + s[index_item + 1:]
        #         except:
        #             counter -= 1
        #             break
        #         # print(counter)
        # return counter
        
        counter = 0
        for word in words:
            j = 0
            i = 0
            while (len(s) > j and len(word) > i):
                # print(i, j)
                if s[j] == word[i]:
                    j += 1
                    i += 1
                else:
                    j += 1

                if i == len(word):
                    counter += 1
        return counter


a = Solution()
print(a.numMatchingSubseq("abcde", ["acd","bcea","ace","aze","de"]))