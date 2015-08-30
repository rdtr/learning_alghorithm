class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """

        flags = [False] * len(s)

        for word in wordDict:
            if s.find(word) == 0:
                flags[len(word)-1] = True

        for i in range(0, len(s)-1):
            if not flags[i]:
                continue
            for word in wordDict:
                if i + len(word) > len(flags)-1:
                    continue
                if s.find(word, i+1) == i+1:
                    flags[i+len(word)] = True
        return flags.pop(-1)
