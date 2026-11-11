class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        results = []
        buckets = [[] for _ in range(len(nums) + 1)]
        mp = defaultdict(int)

        for n in nums:
            mp[n] += 1
        
        for num, v in mp.items():

            buckets[v].append(num)
        for b in range(len(buckets) - 1, 0, -1):

            for i in buckets[b]:
                results.append(i)
                if len(results) == k:
                    return results


            
