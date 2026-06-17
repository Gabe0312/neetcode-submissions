class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numAnswers = set()

        for i in nums:
            if i in numAnswers:
                return True
            numAnswers.add(i)  
        return False
        
        

      
        