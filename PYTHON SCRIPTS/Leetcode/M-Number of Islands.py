class Solution:
    def numIslands(grid: list[list[str]]) -> int:
        def search(lvl, n, g):
            g[lvl][n]='2'
            if n!=len(g[lvl])-1 and g[lvl][n+1] == '1': search(lvl,n+1,g)
            if n!=0 and g[lvl][n-1] == '1': search(lvl,n-1,g)
            if lvl!=len(g)-1 and g[lvl+1][n] == '1': search(lvl+1,n,g)
            if lvl!=0 and g[lvl-1][n] == '1': search(lvl-1,n,g)
            return 1
        count=0
        for i in range(len(grid)):
            for t in range(len(grid[i])):
                if grid[i][t] == '1': count+=search(i,t,grid)
        return count
    

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

# Output: 3

print(Solution.numIslands(grid))