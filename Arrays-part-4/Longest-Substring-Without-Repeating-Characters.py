class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = [0]*200
        st, maxi = 0, 0
        for e in range(len(s)):
            ind = ord(s[e]) - ord('a')
            dic[ind] += 1
            if dic[ind] > 1:
                while dic[ind] > 1:
                    dic[ord(s[st]) - ord('a')] -= 1
                    st += 1
            maxi = max(maxi, e-st+1)
        
        return maxi
