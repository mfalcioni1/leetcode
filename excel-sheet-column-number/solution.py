from string import ascii_uppercase
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        len_title = len(columnTitle)
        col_num = 0
        for i in range(len_title):
            n_char = ascii_uppercase.index(columnTitle[i]) + 1
            col_num += 26**(len_title - (i + 1))*n_char

        return col_num

Solution().titleToNumber('ZZ')
# "ZZ" = 702
Solution().titleToNumber('AZZ')
# "AZZ" = 1378
Solution().titleToNumber('BAA')
# "BAA" = 1379