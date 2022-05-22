class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        presum = [0] * (len(tiles)+1)
        startpos = [s for s,_ in tiles]
        res = 0
        for i in range(1, len(tiles)+1):
            presum[i] = presum[i-1] + tiles[i-1][1] - tiles[i-1][0] + 1
        
        for i, (s, e) in enumerate(tiles):
            if e-s+1 >= carpetLen:
                return carpetLen
            
            endtileID = bisect_right(startpos, s+carpetLen-1) -1
            
            extra = 0
            if s+carpetLen-1 < tiles[endtileID][1]:
                extra = tiles[endtileID][1] - (s+carpetLen-1)
            
            
            res = max(res, presum[endtileID+1] - presum[i] - extra)
        return res
            
            
            
            
                
                
        
            