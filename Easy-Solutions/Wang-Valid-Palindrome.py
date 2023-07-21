class Solution(object):
    def isPalindrome(self, s):
        palindrome = lower("".join(filter(unicode.isalnum, s)))
        
        if (palindrome == palindrome[::-1]):
            return True
        else:
            return False
            
        """
        :type s: str
        :rtype: bool
        """
