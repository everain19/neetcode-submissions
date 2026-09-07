class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = defaultdict(int)
        
        for n in nums:
            nums_count[n] += 1
        
        buckets = [[] for i in range(len(nums) + 1)]

        for num, count in nums_count.items():
            buckets[count].append(num)

        output = []

        for i in range(len(buckets)):
            elem = buckets[len(buckets) - 1 - i]
            while len(elem) and k > 0:
                output.append(elem.pop())
                k -= 1
        
        return output


            