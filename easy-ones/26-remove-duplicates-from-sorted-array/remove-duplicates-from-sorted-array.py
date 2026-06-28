class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = {}
        for i in nums:
            if i not in seen:
                seen[i] = 0
        k = 0
        for i in seen:
            nums[k] = i
            k += 1

        return k


        