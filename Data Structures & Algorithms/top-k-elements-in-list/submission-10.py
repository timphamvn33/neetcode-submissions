class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        results = []

        for n in nums:
            mp[n] = mp.get(n, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]


        

        for num, v in mp.items():
            bucket[v].append(num)


        for i in range(len(bucket) - 1, -1, -1):
            for b in bucket[i]:
                results.append(b)
                if len(results) == k:
                    return results

        return results[0:k]

        



            
