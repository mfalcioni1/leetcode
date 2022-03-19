class Solution:
    def canWinNim(self, n: int) -> bool:
        # giving 4 is a win
        # so receiving 5,6,7 is a win
        # giving 8 is a win
        # so receiving 9, 10, 11 is a win
        # ...

        if n % 4 == 0:
            return False
        else:
            return True
