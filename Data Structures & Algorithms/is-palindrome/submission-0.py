class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned_text = re.sub(r'[^\w\s]', '', s)
        s = "".join(cleaned_text.split()).lower()
        # s = [char for char in s if char not in string.punctuation]
        print(s)
        left, right = 0, len(s)-1

        while left < right:
            if s[left] != s[right]:
                return False
            left+=1
            right-=1
        
        return True
        