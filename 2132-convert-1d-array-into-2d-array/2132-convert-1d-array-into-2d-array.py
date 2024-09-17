class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if (len(original) != m*n):
            return []
        else:
            ans = [[0] * n for _ in range(m)]

            for i in range(len(original)):
                row, col = int(i // n), int(i % n)
                ans[row][col] = original[i]

        return ans
