class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(c for c in s if c.isalnum())

        for i in range(len(s)):
            j = len(s) - 1 -i
            if not s[i] == s[j]:
                return False

        return True
        