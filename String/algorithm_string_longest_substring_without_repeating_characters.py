#

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        leng = len(s)
        if leng == 0: return 0

        m = {}

        maxLen = 0
        curLen = 0
        startIdx = 0
        for curIdx, ch in enumerate(s):
            if ch in m and m[ch] >= startIdx:
                startIdx = m[ch] + 1
                m[ch] = curIdx
                curLen = curIdx - startIdx + 1
            else:
                m[ch] = curIdx
                curLen += 1
                if curLen > maxLen: maxLen = curLen
        return maxLen
