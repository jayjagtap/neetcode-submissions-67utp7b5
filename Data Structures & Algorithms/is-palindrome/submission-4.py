class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = "".join(s.split()).lower()
        left, right = 0, len(s)-1
        print(s)

        while right > left :
            while left < right and not s[left].isalnum():
                left+=1
    
            while left < right and not s[right].isalnum():
                right-=1

            if s[left] != s[right]:
                return False
            left+=1
            right-=1

        return True
        