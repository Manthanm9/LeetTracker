class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, val in enumerate(nums):
            complement = target - val
            #print(seen)
            if complement in seen:
                return [seen[complement], i]
            else:
                seen[val] = i
            
        