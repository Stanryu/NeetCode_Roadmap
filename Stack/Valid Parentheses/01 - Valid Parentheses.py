class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ['(', '[', '{']
        close_brackets = [')', ']', '}']
        brackets = {')':'(', ']':'[', '}':'{'}
        stack = []

        for i in s:
            if i in open_brackets:
                stack.append(i)
            elif i in close_brackets and stack:
                if not(brackets.get(i) == stack.pop()):
                    return False
            else :
                return False
        if len(stack) == 0 : 
            return True
        else:
            return False


if __name__=="__main__":
    s = Solution()
    print(s.isValid("]"))