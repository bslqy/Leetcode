class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Sliding window
        slow = 0
        fast = 0
        d = set()
        ans = 0
        while(slow < len(s) and fast < len(s)):
            if s[fast] not in d:
                d.add(s[fast])
                fast = fast + 1
                ans = max(ans,fast - slow)
            elif s[fast] in d:
                d.remove(s[slow])
                slow = slow + 1
        return ans




if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("dvde"))