class Solution:
    def uniquePaths(self, rows: int, cols: int) -> int:
        table = []
        for i in range(rows):
            table.append([1] * cols)


        for i in range(1, len(table)):
            for j in range(1, len(table[1])):
                table[i][j] = table[i-1][j] + table
