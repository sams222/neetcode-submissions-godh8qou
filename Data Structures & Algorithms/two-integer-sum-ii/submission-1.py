class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        high = len(numbers)-1
        low = 0
        low_num = numbers[low]
        high_num = numbers[high]

        while low_num + high_num != target:

            if low_num + high_num > target:
                high-=1
                high_num = numbers[high]

            else:
                low += 1
                low_num = numbers[low]

        return [low+1,high+1]
            

            


             

        
