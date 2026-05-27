class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s: return 0

        chars = set()
        maxLength, length = 1, 1
        n = len(s)

        left, right = 0, 0
        chars.add(s[0])

        while right<n-1:
            right+=1
            if s[right] not in chars:
                length = right - left + 1
                maxLength = max(maxLength, length)
                chars.add(s[right])
            else:
                # Move left until a same char is found and increment by 1
                while s[left] != s[right]:
                    chars.remove(s[left])
                    left+=1
                left+=1
        
        return maxLength
            


            

        