class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0

        curLength = 0
        lastWordLength = 0
        for ch in s:
            if ch == " ":
                curLength = 0
                continue
            curLength += 1
            lastWordLength = curLength
        return lastWordLength
