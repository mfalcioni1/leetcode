class Solution:
    def isPalindrome(self, x: int) -> bool:
        l = [n for n in str(x)]
        r_l = l[::-1]
        if r_l == l:
            return True
        else:
            return False

sol = Solution()
sol.isPalindrome(1221)
sol.isPalindrome(122111)
sol.isPalindrome(-123)