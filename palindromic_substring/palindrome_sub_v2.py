
"""Solution to Longest Palindromic Substring Leetcode exercise"""

# Solution attempt 1, no guidance

class Solution:
    """Solution"""
    def __init__(self) -> None:
        self.found_palis = {}

    @staticmethod
    def validate_input(src) -> bool:
        """Validate the input string against constraints"""
        # length constraints
        if len(src) > 1000 or len(src) < 1:
            print("error: string length must be greater than 0 and less than 1000")
            return False

        # character constraints
        if not str(src).isalnum():
            print("error: invalid characters (letters and digits only)")
            return False
        return True

    def longest_palindrome(self, src) -> str:
        """find the longest palindromic substring"""

        # validate input
        if not self.validate_input(src):
            raise ValueError

        # assuming there are no palindromes found, the longest palindrome is the first char
        long_palindrome = src[0]

        # if whole input is a palindrome it must be longest one
        if src == src[::-1]:
            long_palindrome = src
            print(f"longest palindrome: {long_palindrome}")
            return long_palindrome

        # create a dict using the characters as keys, each containing a list of
        # the indices where the char appears in the string
        results = {}
        for idx, char in enumerate(src):
            if char in results:
                for prev_idx in results[char]:
                    possible = src[prev_idx:idx+1]
                    if possible == possible[::-1] and len(possible) > len(long_palindrome):
                        long_palindrome = possible
                results[char].append(idx)
            else:
                results[char] = [idx]
        if len(results) == 1:
            long_palindrome = src
        print(f"longest palindrome: {long_palindrome}")
        return long_palindrome


test_inputs = [
    # (input, expected_output)
    ("babad", "bab"),
    ("a", "a"),
    ("bb", "bb"),
    ("abcda", "a"),
    ("cbba", "bb"),
    ("ac", "a"),
    ("ccc", "ccc"),
    ("abcba", "abcba"),
    ("xaabacxcabaaxcabaax", "xaabacxcabaax"),
    ("babaddtattarrattatddetartrateedredividerb", "ddtattarrattatdd")
    ]

for case, expected_out in test_inputs:
    print(f"testcase: \"{case}\"")
    result = Solution().longest_palindrome(case)
    if result == expected_out:
        print("[+] PASSED")
    else:
        print("[!] FAILED")
        raise Exception(f"correct result is '{expected_out}', got '{result}'")
    print("")
