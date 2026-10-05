class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Using the hash map to pair the number with their frequency
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        
        # sort the hash_map from max frequency to min using the bucket 2d array4
        # this 2d array will have 1 column and len(nums) +1 rows because the max frequency could be equal to the len(nums) 
        buckets = [[] for _ in range(len(nums) +1)]

        # set the buckets with the index is the frequency and the value is the number
        for num, freq in hash_map.items():
            buckets[freq].append(num)
        # revert the bucket by its index then get the resutl base on the k
        results = []
        for freq in range(len(buckets)-1, 0, -1):
            for buc in buckets[freq]:
                results.append(buc)
                if len(results) == k:
                    return results
        