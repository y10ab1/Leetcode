class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        candidate_cols=[]
        for i in range(len(picture)):
            bpos,bcnt=0,0
            for j in range(len(picture[0])):
                if picture[i][j] == 'B':
                    bcnt+=1
                    bpos=j
                if bcnt>1:
                    break
            if bcnt==1:
                candidate_cols.append(bpos)
        ans=0
        for col in candidate_cols:
            bcnt=0
            for row in range(len(picture)):
                if picture[row][col] == 'B':
                    bcnt+=1
                if bcnt>1:
                    break
            if bcnt==1:
                ans+=1
        return ans
                
                        