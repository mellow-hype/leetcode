#!/usr/bin/python3

class Solution:
    def __init__(self) -> None:
        self.found_palis = {}

    def findPalindromes(self, src) -> None:
        # length constraints
        if len(src) > 1000 or len(src) < 1:
            print("error: string length must be greater than 0 and less than 1000")
            return
        if not str(src).isalnum():
            print("error: invalid characters (letters and digits only)")
            return

        if src == src[::-1]:
            self.found_palis[src] = len(src)
        print(f"Input: s = \"{src}\"")
        # if length = 2 and it didnt match the above check, this can't be a
        # palindrome, return the first char
        if len(src) == 2:
            self.found_palis[src[0]] = len(src[0])

        # for all other cases, use the following algo
        else:
            # create a dict using the characters as keys, each containing a list of
            # the indices where the char appears in the string
            results = {}
            for idx, char in enumerate(src):
                if char in results:
                    results[char].append(idx)
                else:
                    results[char] = [idx]

            # iterate through the dict items (char, occ_index_list)
            for occ_idx in list(results.values()):
                # palis always have at least one repeating char, only check chars with
                # multiple occurrences
                if len(occ_idx) > 1:
                    # iterate through the list of occurrence indices
                    for idx in range(len(occ_idx)):
                        # the largest subscriptable index of a list is len(list)-1 
                        max_occ_idx = len(occ_idx) - 1
                        if idx + 1 <= max_occ_idx:
                            # the current index at which the char occurs
                            start = occ_idx[idx]
                            # the next index at which the char occurs
                            next = occ_idx[idx + 1]

                            # create a slice from the first occurrence to the next
                            # need to add +1 to `next` since the slice index is not inclusive
                            possible = src[start:next + 1]

                            # check that this is a palindrome by comparing against reversed version
                            if possible == possible[::-1]:
                                self.found_palis[possible] = len(possible)

    def longestPalindromeSubstring(self, src) -> None:
        self.findPalindromes(src)

        # find the longest palis that aren't a direct match to the input str
        longest = [""]
        for f in self.found_palis.keys():
            if f == src:
                if len(src) == 1 or len(src) == 2:
                    longest = [f]
                else:
                    continue
            if len(f) > len(longest[0]):
                longest = [f]
            elif len(f) == len(longest[0]):
                longest.append(f)
        if longest[0]:
            print(f"Output: {longest[0]}")
            return longest[0]

    def longestPalindrome(self, src) -> None:
        self.findPalindromes(src)

        # find the longest palindromes
        longest = [""]
        for f in self.found_palis.keys():
            if len(f) > len(longest[0]):
                longest = [f]
            elif len(f) == len(longest[0]):
                longest.append(f)
        if longest:
            print(f"Output: {longest[0]}")
            if len(longest) > 1:
                print(f"other valid answers are: {longest[1:]}")


test_inputs = ["babad", "a", "bb", "abba", "ac"]
for case in test_inputs:
    Solution().longestPalindromeSubstring(case)
    print("")
