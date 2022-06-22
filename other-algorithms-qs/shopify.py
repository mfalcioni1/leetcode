'''
Prompt
Original string: abcdefghijklmn

Operations:F -> move curser forward, B -> move curse backward, R -> replace char

Operation string: F2B1F5Rw  -> abcdefwhijklmn (expected output)

Moving forward by 2 chars, move backward by 1 char, move forward 5 chars, replace 1 char to be "w"

We can assume that curser is at first character at the beginning.
'''

import re

class string_insert:
    
    def __init__(self, s, op, cursor = 0) -> None:
        self.s = s
        self.op = op
        self.cursor = cursor

    def R(self):
        r_act = re.findall("R(.+)", self.op)[0]
        return r_act
    
    def F(self):
        f_ttl = re.findall("F(\d+)", self.op)
        f_ttl = [int(x) for x in f_ttl]
        return sum(f_ttl)
    
    def B(self):
        b_ttl = re.findall("B(\d+)", self.op)
        b_ttl = [int(x) for x in b_ttl]
        return sum(b_ttl)
    
    def insert(self):
        with_char = self.R()
        self.cursor = self.F() - self.B()
        print(self.s[self.cursor])
        replace_char = self.s[self.cursor]
        res = self.s.replace(replace_char, with_char)
        return res
        



op = "F2B1F5Rw"
s = "abcdefghijklmn"
solution = string_insert(s, op)

solution.insert()

# expected result
"abcdefwhijklmn" == solution.insert()