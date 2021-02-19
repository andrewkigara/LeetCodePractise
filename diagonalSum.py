class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        sum=0
        i=0

        while i<n:
            sum += mat[i][i]+mat[i][n-i-1]
            i+=1
        if(n%2==1):
            sum-=mat[n//2][n//2]

        return sum
