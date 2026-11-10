class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_map = {}
        result = []



        #buckets 2d
        nums_list = [[] for _ in range(len(nums) +1)]


        for n in nums:
            nums_map[n] = nums_map.get(n, 0) + 1

        for num, freg in nums_map.items():
            nums_list[freg].append(num)
        
        for i in range(len(nums_list) -1, 0, -1):
            for n in nums_list[i]:
                result.append(n)
            
                if len(result) == k:
                    return result



        
                


        