class Solution(object):
    def myPow(self, x, n):
        """
            :type x: float
            :type n: int
            :rtype: float
            """
        if x == 0:
            return 0
        
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n > 0:
            if n % 2 == 0:
                tmp = self.myPow(x, n/2)
                return tmp * tmp
            else:
                tmp = self.myPow(x, (n-1)/2)
                return x * tmp * tmp
        else:
            return 1 / self.myPow(x, -n)