class Solution:
    def romanToInt(self, s: str) -> int:
        def stringToList(s):
            s_l = []
            s_l[:0] = s
            return s_l
        res = [None]*len(s)
        s_l = stringToList(s)
        for i in range(len(s_l)):
            if s_l[i] == "I":
                res[i] = 1
            elif s_l[i] == "V":
                res[i] = 5
            elif s_l[i] == "X":
                res[i] = 10
            elif s_l[i] == "L":
                res[i] = 50
            elif s_l[i] == "C":
                res[i] = 100
            elif s_l[i] == "D":
                res[i] = 500
            elif s_l[i] == "M":
                res[i] = 1000
        
        def addSub(res):
            if len(res) == 1:
                return res[0]
            ttl = 0
            sub = 0
            for i in range(len(res)):    
                if i == len(res)-1:
                    ttl = ttl + res[i] - sub
                elif res[i] >= res[i+1]:
                    ttl = ttl + res[i] - sub
                    sub = 0
                else:
                    sub = res[i]
            return ttl
        
        return addSub(res)

sol = Solution()
sol.romanToInt("IV")
sol.romanToInt("III")
sol.romanToInt("LVIII")
sol.romanToInt("MCMXCIV")
sol.romanToInt("MMMM")