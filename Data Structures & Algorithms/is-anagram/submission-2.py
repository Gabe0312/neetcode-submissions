class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        countS = {}
        countT = {}
        
        for index in s:
            if index not in countS:
                countS[index] = 1
            else:
                countS[index] = countS[index] + 1
        for pos in t:
            if pos not in countT:
                countT[pos] = 1
            else:
                countT[pos] = countT[pos] + 1
        if countS != countT:
            return False
        else: 
            return True
        
                    


        