class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= 1:
            return nums
        seen = {}
        for num in nums:
            if num in seen :
                seen[num] += 1
            else:
                seen[num] = 1
        seen = dict(sorted(seen.items(), key = lambda seen: seen[1], reverse = True))
        #print(seen)
        new =[]
        for i, v in seen.items():
                new.append(i)
        return new[:k]
            
        
        