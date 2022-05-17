class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def matchChar(s, idx, n_l):
            if idx < len(s):
                if s[idx] != s[idx+1]:
                    matchChar(s, idx+1, n_l+1)
                else:
                    return n_l
        m_l = 1 # min max length
        for i in range(len(s)):
            n_l = matchChar(s[i:len(s)-1], 0, 1)
            m_l = max(n_l, m_l)
        return m_l




s = "pwwkew"
sol = Solution()
sol.lengthOfLongestSubstring(s)