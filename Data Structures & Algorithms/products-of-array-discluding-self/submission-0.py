class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productAll = 1
        output = []

        null_idx = None
        null_count = 0
        for idx, n in enumerate(nums):
            if n == 0 and null_count == 0: 
                null_idx = idx
                null_count += 1
                continue
            productAll *= n

        for idx, n in enumerate(nums):
            if null_idx is not None:
                if idx == null_idx:
                    output.append(int(productAll))
                else:
                    output.append(0)
            else:
                output.append(int(productAll / n))
        
        return output
        