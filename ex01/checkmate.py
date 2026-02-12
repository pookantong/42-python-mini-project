class Chess:
    def __init__(self, directions: list[tuple[int, int]], is_full_board: bool):
        self.directions = directions
        self.is_full_board = is_full_board
        
    def can_attack(self, start: tuple[int, int], end: tuple[int, int], board: list[list[str]]) -> tuple[bool, list[tuple[int, int]]]:
        n = len(board)

        for dx, dy in self.directions:
            x, y = start
            path = []
            
            x += dx
            y += dy

            while 0 <= x < n and 0 <= y < n:
                path.append((x, y))
                if (x, y) == end:
                    return True, path
                if board[x][y] in PIECES.keys():
                    break
                if not self.is_full_board:
                    break
                x += dx
                y += dy

        return False, []
        
PIECES = {
    "R": Chess([(1,0), (-1,0), (0,1), (0,-1)], True),
    "B": Chess([(1,1), (1,-1), (-1,1), (-1,-1)], True),
    "Q": Chess([(1,0), (-1,0), (0,1), (0,-1),
                (1,1), (1,-1), (-1,1), (-1,-1)], True),
    "P": Chess([(-1,-1), (-1,1)], False),
}

def checkmate(board: str) -> None:
    rows = board.strip().split("\n")
    n = len(rows)

    if n == 0 or any(len(r) != n for r in rows):
        print("Error Board is not square")
        return

    grid = [list(r) for r in rows]

    king_pos = None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "K":
                if king_pos is not None:
                    print("Error More than one king found")
                    return 
                king_pos = (i, j)
    if king_pos is None:
        print("Error No king found")
        return 

    found_attack = False
    all_paths = []
    
    for i in range(n):
        for j in range(n):
            piece = grid[i][j]
            if piece in PIECES:
                attacked, path = PIECES[piece].can_attack((i, j), king_pos, grid)
                if attacked:
                    found_attack = True
                    all_paths.append(path)

    if found_attack:
        new_grid = [row[:] for row in grid]

        for path in all_paths:
            for x, y in path:
                if new_grid[x][y] != "K":
                    new_grid[x][y] = "X"

        print("Success")
        valid_pieces = set(PIECES.keys()) | {"K"}
        for row in new_grid:
            print(" ".join(
                cell if cell in valid_pieces or cell == "X" else "."
                for cell in row
            ))
    else:
        print("Fail")
