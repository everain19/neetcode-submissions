class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dimension = 9
        for i in range(dimension):
            row_num_counter = defaultdict(int)
            for j in range(dimension):
                if board[i][j] != '.':
                    if row_num_counter[board[i][j]] > 0:
                        return False
                    row_num_counter[board[i][j]] += 1

        for i in range(dimension):
            column_num_counter = defaultdict(int)
            for j in range(dimension):
                if board[j][i] != '.':
                    if column_num_counter[board[j][i]] > 0:
                        return False
                    column_num_counter[board[j][i]] += 1

        box_coord_x_start = 0
        box_coord_x_end = 3
        box_coord_y_start = 0
        box_coord_y_end = 3

        while box_coord_x_start <= 9 and box_coord_y_start <= 6:
            if box_coord_x_start == 9 and box_coord_y_start == 6:
                break

            if box_coord_x_start == 9:
                box_coord_x_start = 0
                box_coord_x_end = 3
                box_coord_y_start += 3
                box_coord_y_end += 3
            box_num_counter = defaultdict(int)
            for row in board[box_coord_x_start:box_coord_x_end]:
                for num in row[box_coord_y_start:box_coord_y_end]:
                    if num != '.':
                        if box_num_counter[num] > 0:
                            return False
                        box_num_counter[num] += 1

            box_coord_x_start += 3
            box_coord_x_end += 3
            box_num_counter = defaultdict(int)

        return True