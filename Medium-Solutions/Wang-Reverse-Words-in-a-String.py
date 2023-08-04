"""
Wang-Reverse-Words-in-a-String.py
    This program reverse the order of a string sentence by words

by: Kyle Wang
August 3, 2023
"""
class Solution(object):
    def reverseWords(self, s):
# split s into list so that it is easy to reverse
        sList = s.split()
        result = ""
# reverse iterated for loop to reorder s
        for i in range(len(sList)-1, -1, -1):
            result += sList[i] + " "
# string will always end with a space, so need to use strip() to remove
        return result.strip()

        """
        :type s: str
        :rtype: str
        """
