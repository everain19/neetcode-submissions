class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        box_area = defaultdict(set)

        dimension = 9
        for r in range(dimension):
            for c in range(dimension):
                num = board[r][c]
                if num == '.':
                    continue

                box_idx = (r // 3, c // 3)

                if (num in rows[r] or
                    num in cols[c] or
                    num in box_area[box_idx]):
                    return False

                rows[r].add(num)
                cols[c].add(num)
                box_area[box_idx].add(num)
        return True