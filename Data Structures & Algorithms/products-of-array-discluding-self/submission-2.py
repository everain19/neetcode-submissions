class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output: List[int] = []

        productAll = 1
        zero_idxs = []
        for idx, n in enumerate(nums):
            if n == 0:
                zero_idxs.append(idx)
                continue
            productAll *= n

        if len(zero_idxs) > 1:
            output = [0] * len(nums)
            return output

        if len(zero_idxs) == 1:
            output = [0] * len(nums)
            output[zero_idxs[0]] = productAll
        else:
            for idx, n in enumerate(nums):
                output.append(productAll // n)

        return output