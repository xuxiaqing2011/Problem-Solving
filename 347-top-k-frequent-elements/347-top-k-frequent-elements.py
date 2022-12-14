from collections import defaultdict, OrderedDict

class Solution(object):
    def topKFrequent(self, nums, k):
        
        d = defaultdict(int)
        
        for n in nums:
            d[n] += 1
        
        ss = sorted(d.items(), key=lambda item: item[1], reverse=True)
        
        return [ x[0] for x in ss ][:k]