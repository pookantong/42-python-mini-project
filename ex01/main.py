from checkmate import checkmate
import sys

def process_file(filename: str) -> str:
    try:
        with open(filename, "r") as f:
            board = f.read()
    except:
        return ""

    return board


def main():
    if len(sys.argv) < 2:
        print("Error")
        return
    
    
    for filename in sys.argv[1:]:
        board = process_file(filename)

        if board is None:
            print("Error")
            continue
        
        print("------------------------------------------------------")
        print(filename)

        checkmate(board)
        
if __name__ == "__main__":
    main()
