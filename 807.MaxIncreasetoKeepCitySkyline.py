class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        print zip(*grid)
        max_each_row = [max(i) for i in grid]
        max_each_column = [max(j) for j in zip(*grid)] # zip(*grid) create a col wise list
        increase = 0
        row = len(grid)
        col = len(grid[0])
        # for i in range(col):
        #     maximum = 0
        #     for j in range(row):  
        #         maximum = max(grid[j][i],maximum)
        #     max_each_column.append(maximum)   
            
        for i in range(row):
            for j in range(col):
                increase += min(max_each_row[i], max_each_column[j]) - grid[i][j]
        return increase
