class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(0,n):
            rem = target - nums[i]
            if rem in nums:
                j = nums.index(rem)
                if i!= j:
                    return sorted([i , j])
                    
