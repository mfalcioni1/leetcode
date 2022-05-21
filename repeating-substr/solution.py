class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def matchChar(s, idx, u_seq):
            if idx < len(s):
                if s[idx] not in u_seq:
                    u_seq = u_seq + s[idx]
                    return matchChar(s, idx + 1, u_seq)
            return len(u_seq)
        if len(s) == 0:
            return 0
        else:
            m_l = 1 # min max length
        for i in range(len(s)): #skip empty and singular string 
            sub_str = s[i:len(s)]
            if m_l < len(sub_str):
                n_l = matchChar(sub_str, 0, '')
                m_l = max(n_l, m_l)
        return m_l


sol = Solution()
s = "au"
sol.lengthOfLongestSubstring(s) == 2
s = "pwwkew"
sol.lengthOfLongestSubstring(s) == 3
s = "abcabcbb"
sol.lengthOfLongestSubstring(s) == 3
s = "bbbbb"
sol.lengthOfLongestSubstring(s) == 1