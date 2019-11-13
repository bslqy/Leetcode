"""

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.


Input: "aba"
Output: False


Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

"""


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1,len(s) // 2 + 1):
            print(i)
            print(s[:i]*(len(s) // i))
            if s[:i]*(len(s) // i ) == s:
                return True
        return False



if __name__ == '__main__':
    print(Solution().repeatedSubstringPattern("abcabc"))