class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {"2": ["a", "b", "c"],
                   "3": ["d", "f", "e"],
                   "4": ["g", "h", "i"],
                   "5": ["j", "k", "l"],
                   "6": ["m", "n", "o"],
                   "7": ["p", "q", "r", "s"],
                   "8": ["t", "u", "v"],
                   "9": ["w", "x", "y", "z"]}

        if not digits || len(digits) == 0:
            return []

        # when len == 1
        if len(digits) == 1:
            return mapping(digits[0])

        # case when len > 1
        base = []
        for c in digits:
            local = mapping[c]
            for char in base:
                for j in mapping[digits[i]]:
                    res.append(char + j)
            base = res

