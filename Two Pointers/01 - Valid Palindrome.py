import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #s = s.replace(" ", "").lower()
        #s = ''.join(ch for ch in s if ch not in string.punctuation)
        l = 0
        r = len(s)-1

        while l < r:
            if s[l] == " " or s[l] in string.punctuation:
                l += 1
                continue
            if s[r] == " " or s[r] in string.punctuation:
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    
if __name__=="__main__":
    s = Solution()
    print(s.isPalindrome("No lemon, no melon"))