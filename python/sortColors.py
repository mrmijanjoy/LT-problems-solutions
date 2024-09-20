class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                # Swap nums[mid] and nums[low]
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # Move mid pointer
                mid += 1
            else:
                # Swap nums[mid] and nums[high]
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
