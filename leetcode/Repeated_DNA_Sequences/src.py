class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        appearance = {}

        i = 0
        while i + 10 <= len(s):
            needle = s[i:i+10]
            if needle in appearance:
                appearanceCount = appearance[needle]
                if appearanceCount == 1:
                    res.append(needle)
                appearance[needle] = appearanceCount + 1
            else:
                appearance[needle] = 1
            i += 1
        return res
