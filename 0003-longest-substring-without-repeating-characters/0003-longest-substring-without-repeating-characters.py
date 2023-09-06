class Solution(object):
    def lengthOfLongestSubstring(self, s):
#         charset = set()
#         l = 0
#         res = 0
        
#         for r in range(len(s)):
#             while s[r] in charset:
#                 charset.remove(s[l])
#                 l += 1
#             charset.add(s[r])
#             res = max(res, r - l + 1)
#         return res
    
        unique_set = set()
        repeat = 0
        longest_unique_count = 0
        for i in range(len(s)):
            while s[i] in unique_set:
                unique_set.remove(s[repeat])
                repeat += 1
            unique_set.add(s[i])
            longest_unique_count = max(longest_unique_count, i - repeat + 1)
        return(longest_unique_count)
        
        """
        :type s: str
        :rtype: int
        """
        