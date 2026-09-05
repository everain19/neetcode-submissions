class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
                                                                                     
        for el in nums:                                                                  
            if el in seen:                                                               
                return True                                                              
                                                                                        
            seen[el] = el                                                                
                                                                                        
        return False                                                                     

