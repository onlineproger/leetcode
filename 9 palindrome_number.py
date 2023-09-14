class Solution:
    """
    #9
    Given an integer x, return true if x is a palindrome, and false otherwise.
    """
    def is_palindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
