class Solution(object):
    def isPalindrome(self, x):
        newX = str(x)
        secX = []
        for i in newX:
            secX.append(i)
        secX.reverse()
        comp = ""
        for i in secX:
            comp += str(i)

        if newX == comp:
            return True
        else:
            return False


        """
        :type x: int
        :rtype: bool
        """
