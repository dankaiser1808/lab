class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleared = "".join(char for char in s if char.isalnum()).lower()
        return cleared == cleared[::-1]