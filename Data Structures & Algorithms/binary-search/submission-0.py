class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low <= high:

            
            mid = int((high-low)/2 + low)

            mid_val = nums[mid]
            
            if mid_val < target:
                low = mid + 1

            elif mid_val > target:
                high = mid - 1

            else:
                return mid

        
        if nums[mid] == target:
            return mid

        else:
            return -1


        
        