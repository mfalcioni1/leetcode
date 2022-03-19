from typing import List
from math import floor
class Solution:
    def countBits(self, n: int) -> List[int]:
        count = []
        for i in range(0, n+1):
            r = i % 2
            num = i
            bin = []
            while num > 0:
                bin.append(r)
                num = floor(num/2)
                r = num % 2
            count.append(sum(bin))
        return count

calc = Solution()
calc.countBits(5)