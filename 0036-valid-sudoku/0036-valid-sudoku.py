class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def isValid(arr):
            nums = set()
            for item in arr:
                if not item == ".":
                    if int(item) <1 or int(item) >9:
                        print("item <1 or ?=>9")
                        return False
                    if item in nums:
                        print("number repeated")
                        return False
                    else:
                        nums.add(item)
            return True
        
        
        #Doing the rows
        rowsAreOk = True
        for row in board:
            if not isValid(row):
                rowsAreOk = False
        
        #Doing the columns
        columnsAreOk = True
        for i in range(9):
            col = []
            for row in board:
                col.append(row[i])
            if not isValid(col):
                columnsAreOk = False
        
        #Doing the subboxes
        minisAreOk = True
        #scanning rows
        for c in range (0,9,3):
            for i in range(0,9,3):
                box = []
                for j in range(3):
                    for k in range(3):
                        box.append(board[c+j][i+k])
                # print(box)
                if not isValid(box):
                    minisAreOk = False
        print(rowsAreOk)
        print(columnsAreOk)
        print(minisAreOk)
        return rowsAreOk and columnsAreOk and minisAreOk
            
            
        
            