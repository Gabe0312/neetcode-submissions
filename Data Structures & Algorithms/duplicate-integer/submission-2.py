class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        array = set()
        for n in nums:
            if n in array:
                return True
            array.add(n)
        return False
        