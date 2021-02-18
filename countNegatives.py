# 124 ms runtime
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        counter = 0

        for i in grid:
            for j in i:
                if j<0:
                    counter+=1
        return counter

# 104 ms runtime
 # class Solution:
    # def countNegatives(self, grid: List[List[int]]) -> int:
    #     counter = 0
    #     n = len(grid)
    #     m = len(grid[0])
    #     j = 0
    #     i = n -1
    #     while i >= 0 and j < m:
    #         if grid[i][j] < 0:
    #             counter += m - j
    #             i -= 1
    #         else:
    #             j += 1
    #     return counter
