class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        return s == t

if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("rat", "car"))