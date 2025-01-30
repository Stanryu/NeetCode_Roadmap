class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        nums_set = set(nums)
        if len(nums) == len (nums_set):
            return False
        else:
            return True


if __name__ == "__main__":
    a = Solution() 
    nums = [1,2,3,4,6,7,8,9,5]
    print(a.hasDuplicate(nums))