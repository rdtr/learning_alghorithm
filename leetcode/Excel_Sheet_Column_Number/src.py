class Solution(object):
    def mapToInt(self, ch):
        return 1 + ord(ch) - ord('A')
    
    def titleToNumber(self, s):
        """
            :type s: str
            :rtype: int
            """
        length = len(s)
        base = length - 1
        
        sum = 0
        for ch in s:
            sum += (26 ** base) * self.mapToInt(ch)
            base -= 1
        return sum
