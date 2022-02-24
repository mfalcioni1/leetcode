from typing import List
from itertools import combinations
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None
    def twoSumIter(self, nums: List[int], target: int) -> List[int]:
        cmb = combinations(nums, 2)
        for i in cmb:
            if sum(i) == target:
                p_1 = nums.index(i[0])
                if p_1 == nums.index(i[1]):
                    p_2 = nums.index(i[1], p_1+1)
                else:
                    p_2 = nums.index(i[1])
                return [p_1, p_2]
        return None

sums = Solution()
sums.twoSum([2, 7, 11, 15], 9)
sums.twoSumIter([2, 7, 11, 15], 9)
sums.twoSumIter([3, 3, 3, 3], 6)