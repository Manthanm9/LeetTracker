class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        right = len(needle )

        for i in range(len(haystack)):
            if haystack[i] == needle[left]:
                if haystack[i:i+ right] == needle:
                    return i
        
        return -1
        