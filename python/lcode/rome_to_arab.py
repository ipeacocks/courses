class Solution:
    def romanToInt(self, s: str) -> int:
        value = 0
        roman_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        for index, elem in enumerate(s):
            if index - 1 >= 0 and str(s[index - 1]) == "I" and str(elem) == "V":
                value = value - roman_dict[s[index - 1]]
                roman_value = 4
            elif index - 1 >= 0 and str(s[index - 1]) == "I" and str(elem) == "X":
                value = value - roman_dict[s[index - 1]]
                roman_value = 9
            elif index - 1 >= 0 and str(s[index - 1]) == "X" and str(elem) == "L":
                value = value - roman_dict[s[index - 1]]
                roman_value = 40
            elif index - 1 >= 0 and str(s[index - 1]) == "X" and str(elem) == "C":
                value = value - roman_dict[s[index - 1]]
                roman_value = 90
            elif index - 1 >= 0 and str(s[index - 1]) == "C" and str(elem) == "D":
                value = value - roman_dict[s[index - 1]]
                roman_value = 400
            elif index - 1 >= 0 and str(s[index - 1]) == "C" and str(elem) == "M":
                value = value - roman_dict[s[index - 1]]
                roman_value = 900
            else:
                roman_value = roman_dict[elem]
            value = value + roman_value
        return value

a = Solution()
print(a.romanToInt('MIII'))