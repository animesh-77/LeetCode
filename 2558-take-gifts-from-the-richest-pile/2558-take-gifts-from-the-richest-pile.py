class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        import bisect, math
        
        gifts.sort()
        lenGifts= len(gifts)
        
        for _ in range(k):
            maxGift= gifts[-1]
            gifts= gifts[:lenGifts-1]
            
            newVal= int(math.floor(math.sqrt(maxGift)))
            
            bisect.insort(gifts, newVal)
            
        return sum(gifts)