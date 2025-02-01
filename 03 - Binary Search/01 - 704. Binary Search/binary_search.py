from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_index = 0
        right_index = len(nums)-1
        
        while right_index - left_index > 1:            
            middle_index = int((right_index - left_index)/2) + left_index
            
            if nums[middle_index] == target:
                return middle_index
            elif nums[middle_index] > target:
                right_index = middle_index
            else:
                left_index = middle_index
            
        if nums[left_index] == target:
            return left_index
        if nums[right_index] == target:
            return right_index
            
        return -1
    
if __name__ == '__main__':
    s = Solution()
    print(s.search([2,6,9], 9))