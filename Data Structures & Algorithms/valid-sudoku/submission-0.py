from collections import Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Check each row for no duplicates and numbers within 1-9
        Check each col for no duplicates and numbers within 1-9

        3*3 blocks
        [[0,0], [0,1], [0,2]].     [0,3]...[3,5]
        [[1,0], [1,1], [1,2]]
        [[2,0], [2,1], [2,2]]

        [3,0].....[5,2] , last block [6,6]....[8,8]

        row=0, col=0 
        while row < 9 and col < 9:
            for r in range(3):
                for c in range(3):
                    square.append(board[row+r][col+c])
            row+=3
            col+=3
        """

        

        # Check rows
        is_valid = True
        for row in board:
            is_valid = is_valid and self.isValid(row)
        
        if is_valid == False: return False

        # Check cols
        cols = [[row[i] for row in board] for i in range(0,9)]
        for col in cols:
            is_valid = is_valid and self.isValid(col)
        
        if is_valid == False: return False

        # Check squares
        for r in range(0,9,3):
            for c in range(0,9,3):
                square = []
                for i in range(r, r+3):
                    for j in range(c, c+3):
                        square.append(board[i][j])
                is_valid = is_valid and self.isValid(square)
                if is_valid == False: return False
        
        return True
            
        
    def isValid(self, check_list: List) -> bool:
        possible_nums = [str(x) for x in range(1, 10)]
        possible_nums.append(".")

        # Check if all nums are in possible_nums
        for num in check_list:
            if num not in possible_nums:
                return False
        
        check_list = [x for x in check_list if x != '.']
        # Now check for frew 
        c = Counter(check_list)
        return not any(v > 1 for v in c.values())

    







        