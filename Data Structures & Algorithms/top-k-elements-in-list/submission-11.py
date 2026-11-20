class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        results = []
        mp = defaultdict(list)
        for i, n in enumerate(nums):
            mp[n] = mp.get(n, 0) + 1
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, val in mp.items():
            buckets[val].append(num)
        for i in range(len(buckets) -1 , -1, -1):
            for b in buckets[i]:

                results.append(b)
        return results[:k]
        
    

        



            
