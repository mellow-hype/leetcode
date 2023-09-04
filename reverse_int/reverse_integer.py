# Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the 
# value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

class Solution:
    """Reverse an integer"""
    @staticmethod
    def reverse(x: int) -> int:
        """reverse an integer"""
        neg = "-" if x < 0 else ""
        reverse = str(x).strip('-')[::-1].strip('0')
        rev_int = int(neg+reverse)
        if (rev_int < -2**31) or (rev_int > 2**31):
            return 0
        return rev_int

test_cases = [
    (123, 321),
    (-123, -321),
    (120, 21),
    (-120, -21)
]

for case, correct in test_cases:
    print(Solution().reverse(case))
