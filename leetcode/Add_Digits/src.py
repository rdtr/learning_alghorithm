class Solution(object):
    def addDigits(self, num):
        """
            :type num: int
            :rtype: int
            """
        
        if num / 10 == 0:
            return num
        sum = 0
        for ch in str(num):
            sum += int(ch)
        return self.addDigits(sum)

# with the formula:
#if num / 10 == 0:
#    return num
#        r = (num - 1) / 9
#        return num - r * 9
