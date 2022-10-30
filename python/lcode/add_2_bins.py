# class Solution:
#     def to_dec(self, a: str) -> int:
#         a_dec = 0
#         for i in enumerate(a[::-1]):
#             print(i)
#             if int(i[1]) != 0:
#                 a_dec += 2 ** i[0]
#         return a_dec

#     def addBinary(self, a: str, b: str) -> str:

#         a_dec = self.to_dec(a)
#         b_dec = self.to_dec(b)
#         sum_dec = a_dec + b_dec
#         print(a_dec, b_dec, sum_dec)

#         bin_digit = ""

#         while sum_dec != 0:
#             bin_digit += str(sum_dec % 2)
#             sum_dec = sum_dec // 2
#         return bin_digit[::-1]


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result += str(carry %2)
            carry = carry // 2

        return result[::-1]


a = Solution()
print(a.addBinary("11110", "1001"))
