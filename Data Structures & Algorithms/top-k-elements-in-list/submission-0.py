class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency = [[] for _ in range(len(nums)+ 1) ]
        
        count = {}
        
        for n in nums:
            count[n] = count.get(n, 0) + 1
            
        for key, value in count.items():
            frequency[value].append(key)

        res = []    
        for i in range(len(frequency)-1, 0, -1):
            if frequency[i]:
                for n in frequency[i]:
                    res.append(n)
                    k -= 1
                    if k == 0:
                        return res
