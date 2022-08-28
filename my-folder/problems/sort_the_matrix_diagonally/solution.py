class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat), len(mat[0])
        # start mat[0][n-1]
        # end   mat[m-1][0]
        
        
        temp = []
        istart, jstart = 0,n-1
        while True:
            i,j = istart, jstart


            while 0<=i<m and 0<=j<n:
                temp.append(mat[i][j])
                i,j=i+1,j+1

            temp.sort()
            i,j = istart, jstart
            cnt = 0
            while 0<=i<m and 0<=j<n:
                mat[i][j] = temp[cnt]
                i,j,cnt =i+1,j+1,cnt+1
            if i==m and j==1:
                return mat
            
            if jstart != 0:
                jstart-=1
            else:
                istart+=1
            temp=[]
                