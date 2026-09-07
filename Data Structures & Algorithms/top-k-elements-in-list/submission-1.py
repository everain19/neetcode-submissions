class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = defaultdict(int)
        
        for n in nums:
            nums_count[n] += 1
        
        output = []

        for i in range(k):
            key = max(nums_count, key=nums_count.get)
            nums_count.pop(key)
            output.append(key)
        
        return output

            