class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counter = defaultdict(int)
        for el in nums:
            num_counter[el] += 1

        nums_counter_bucket = [deque([]) for i in range(len(nums) + 1)]

        for key, val in num_counter.items():
            nums_counter_bucket[val].append(key)

        output = []

        nums_counter_bucket.reverse()
        for bucket in nums_counter_bucket:
          while k > 0 and len(bucket) > 0:
            output.append(bucket.popleft())
            k -= 1

        return output   
        