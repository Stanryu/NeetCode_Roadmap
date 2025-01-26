class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        aux_map = {}
        for idx, i in enumerate(nums):
            diff = target - i
            if diff in aux_map:
                return [aux_map[diff], idx] 
            aux_map[i] = idx

if __name__=="__main__":
    s = Solution()
    print(s.twoSum([3, 4, 5, 6], 7))