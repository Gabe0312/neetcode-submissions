class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        
        outputSet = set()

        for i, iNums in enumerate(nums): 
            for j, jNums in enumerate(nums):

                if i != j and iNums + jNums == target:
                    return [i,j]
        return []

               
        


        