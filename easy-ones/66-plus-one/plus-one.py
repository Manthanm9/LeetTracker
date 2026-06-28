class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range( len(digits) -1, -1, -1):
            if digits[i] < 9:
                digits[i] = digits[i] + 1
                break
            elif digits[i] == 9  and i == 0:
                digits[i] = 0
                digits = [1] + digits
            else:
                digits[i] = 0
            
                
            

        return digits
        