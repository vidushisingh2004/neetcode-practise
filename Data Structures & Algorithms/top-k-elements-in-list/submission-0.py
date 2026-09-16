class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Count how many times each number appears
        count = {}

        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        # Create buckets where the index = frequency
        freq = [[] for i in range(len(nums) + 1)]

        # Put each number into its frequency bucket
        for number, frequency in count.items():
            freq[frequency].append(number)

        # Start with the highest frequency
        res = []

        for i in range(len(nums), 0, -1):
            res.extend(freq[i])

            # Stop once we have k elements
            if len(res) >= k:
                return res[:k]




        