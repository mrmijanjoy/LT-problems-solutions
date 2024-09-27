class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # If the array length is less than or equal to 2, no need to process
        if len(nums) <= 2:
            return len(nums)
        
        # Start index for the modified part of the array
        index = 2
        
        # Traverse the array starting from the third element
        for i in range(2, len(nums)):
            # If current element is not the same as the element at index-2, keep it
            if nums[i] != nums[index - 2]:
                nums[index] = nums[i]
                index += 1
        
        # Return the new length of the array
        return index

        