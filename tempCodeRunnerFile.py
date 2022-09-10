NumX-1][pawnNumY-1]) != "p1" and turn:
            print("There is no pawn")
            noPawn += 1
            pawnInput(board, pawnNumX, pawnNumY, noPawn, pFlag)
        else:
            noPawn = 