class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x = len(nums)/2
        mapp = {}
        for i in nums:
            if i in mapp:
                mapp[i] = mapp[i] + 1
            else:
                mapp[i] = 1
        for idx, val in mapp.items():
            if val > x:
                return idx
        