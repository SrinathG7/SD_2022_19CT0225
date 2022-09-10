

board = [[0]*5]*5

p1 = ["p", "p", "p", "p", "p"]
p2 = ["p", "p", "p", "p", "p"]

board[0] = p1
board[4]= p2
turnFlag = 0    #p1 else p2

while(p1 is not None or p2 is not None):
    if(not p1):
        print("p1's chance")
    print("1  2  3  4  5")
    for i in range(len(board)):
        strBoard ='  '.join([str(elem) for elem in board[i]])
        print(strBoard, end = " ")
        print()
    print("1  2  3  4  5")
    print()
    
    break
    


# print(board)
