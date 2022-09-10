

def pawnInput(board, pawnNumX, pawnNumY, noPawn, pFlag):
    # turn = False
    # if pFlag != 0:
    #     turn = True
    # else:
    #     pFlag = 0
    #     turn = False
    # while(pawnNumX >= 6 or pawnNumX <= 0 or pawnNumY >= 6 or pawnNumY <= 0 or noPawn != 0 or turn):
    #     if pFlag != 0:
    #         turn = True
    #     else:
    #         pFlag = 0
    #         turn = False
    #     print("give a valid input (1 to 5)")
    #     print("Control the Pawn in tile(x-axis)[ 1, 2, 3, 4, 5 ]: ")
    #     pawnNumX = int(input())
    #     print("Control the Pawn in tile(y-axis)[ 1, 2, 3, 4, 5 ]: ")
    #     pawnNumY = int(input())
    #     if(board[pawnNumX-1][pawnNumY-1]) != "p1":
    #         print("There is no pawn")
    #         noPawn += 1
    #         pawnInput(board, pawnNumX, pawnNumY, noPawn, pFlag)
    #     else:
    #         noPawn = 0
    #     if board[pawnNumX-1][pawnNumY-1] == "p2":
    #         print("its not ur move")
    #         pFlag = 1
    #         pawnInput(board, pawnNumX, pawnNumY, noPawn, pFlag)
    #     else:
    #         turn = False
    #         pFlag = 0


    # if board[pawnNumX-1][pawnNumY-1] == "p2":
    #     print("its not ur move")
    #     pFlag = 1
    #     pawnInput(board, pawnNumX, pawnNumY, noPawn, pFlag)
    # else:
    #     turn = False
    #     pFlag = 0
    # while(pawnNumX >= 6 or pawnNumY >= 6 or pawnNumX <= 0 or pawnNumY <= 0):
    print("Control the Pawn in tile(x-axis)[ 1, 2, 3, 4, 5 ]: ")
    pawnNumX = int(input())
    print("Control the Pawn in tile(y-axis)[ 1, 2, 3, 4, 5 ]: ")
    pawnNumY = int(input())
    if pawnNumX >= 6 or pawnNumY >= 6 or pawnNumX <= 0 or pawnNumY <= 0:
        pawnInput(board, pawnNumX, pawnNumY, noPawn, pFlag)
        
    if board[pawnNumX-1][pawnNumY - 1] == 0:
        print("No Pawn")
        print(board[pawnNumX-1][pawnNumY-1])
        pawnInput(board, pawnNumX, pawnNumY, noPawn, pFlag)

    if board[pawnNumX-1][pawnNumY-1] == "p2" and pFlag == 0:
        print("Its not ur Pawn")
        pawnInput(board, pawnNumX, pawnNumY, noPawn, pFlag)
    if board[pawnNumX-1][pawnNumY-1] == "p1" and pFlag == 1:
        print("Its not ur Pawn")
        pawnInput(board, pawnNumX, pawnNumY, noPawn, pFlag)



    res=[]
    res.append(pawnNumX)
    res.append(pawnNumY)
    res.append(noPawn)
    return res

def Moves(board, pawnNumX, pawnNumY, move):
    move = int(input())
    # while(move >= 5 or move <= 0):
    #     print("give a valid input (1 to 4)")
    #     move = int(input())
    if move >= 5 or move <= 0:
        print("give a  valid move")
        Moves(board, pawnNumX, pawnNumY, move)
    
    #Up
    print("move")
    if move == 4:
        board[pawnNumX+1][pawnNumY-1] = "p0"
        
        board[pawnNumX-1][pawnNumY-1] = 0
        
        # board[pawnNumX][pawnNumY-1] = "p0"
        return board
        # if board[pawnNumX][pawnNumY-1] is not None:
        #     board[pawnNumX][pawnNumY-1] = "p1"
        #     return board
        # else:
        #     print("No space try again")
            


board = [[0]*5]*5

p1 = ["p1", "p1", "p1", "p1", "p1"]
p2 = ["p2", "p2", "p2", "p2", "p2"]

board[0] = p1
board[4]= p2
pFlag = 0    #p1 else p2

while(p1 is not None or p2 is not None):
    if(pFlag == 0):
        print("p1's chance")
        
    else:
        print("p2's chance")
        
    print("     1    2    3    4    5")
    for i in range(len(board)):
        strBoard =' | '.join([ str(elem)for elem in board[i]])
        print(str(i+1)+ "    " + strBoard, end = " ")
        print()
    print("     1    2    3    4    5")
    print()
    # print("Control the Pawn in tile(x-axis): 1, 2, 3, 4, 5")
    
    pawnNumX = 0
    # print("Control the Pawn in tile(y-axis): 1, 2, 3, 4, 5")
    pawnNumY = 0
    noPawn = 0
    res = []
    res = pawnInput(board, pawnNumX, pawnNumY, noPawn, pFlag)
    
    # if(board[pawnNumX-1][pawnNumY-1]) == 0:
    #     noPawn += 1
    #     res = pawnInput(board, pawnNumX, pawnNumY, noPawn, pFlag)
    # else:
    #     noPawn = 0
    pawnNumX = res[0]
    pawnNumY = res[1]
    noPawn = res[2]
    print("Moves: ")
    print("Left : 1")
    print("Right: 2")
    print("Down : 3")
    print("Up   : 4")
    move = 0
    
    board = Moves(board, pawnNumX, pawnNumY, move)
    if(not pFlag):
        pFlag = 1
    else:
        pFlag = 0

    
    # break
    


# print(board)
