class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Counting frequency of each number
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Creating buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        # Putting numbers into buckets based on their frequency
        for num, freq in count.items():
            buckets[freq].append(num)

        # Collecting k most frequent elements
        result = []

        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)

                if len(result) == k:
                    return result