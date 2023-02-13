class Solution:
    def longest_palindrome(self, s: str) -> str:
        def is_palindrome(string):
            if string == string[::-1]:
                return True
            return False
        storage = s[0]
        for f_ind, f_let in enumerate(s):
            for s_ind, s_let in enumerate(s[:f_ind+1]):
                if f_let == s_let and is_palindrome(s[:f_ind+1][s_ind:]):
                    if len(s[:f_ind+1][s_ind:]) > len(storage):
                        storage = s[:f_ind+1][s_ind:]
                        break
        return storage
