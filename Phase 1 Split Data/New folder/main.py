from math import sqrt

def minMoves(n, startRow, startCol, endRow, endCol):
    # create chess board
    chess_board =[]
    for row in range(n):
        li1 = []
        for col in range(n):
            li1.append("*")
        chess_board.append(li1)
    #  Identify knight
    Knight = 'K'
    chess_board[startRow][startCol] = Knight
    K =  [startRow,startCol]
    #  Identify target
    Target = "T"
    chess_board[endRow][endCol] = Target
    T = [endCol,endRow]

    def find_shortest(K, T):
    #find second shortest route:
        target = 101
        y = K[0]
        x = K[1]
        count = 0
        li_of_path = []

        step1 = [[y-2,x-1],[y-1,x-2],[y+1,x-2],[y+2,x-1],[y-2,x+1],[y-1,x+2],[y+1,x+2],[y-2,x+1]]
        for i in step1:
            distance = sqrt((i[0] - T[0])**2  + (i[1] - T[1])**2)
            li_of_path.append(distance)
        lowest = min(li_of_path)
        li_of_path.remove(lowest)
        sec_lowest = (min(li_of_path))

        for i in step1:
            distance = sqrt((i[0] - T[0])**2  + (i[1] - T[1])**2)
            if distance == sec_lowest:
                yay = i[0]
                yay2 = i[1]
                break
        return sec_lowest







    # # condition win
    # count = 0
    # while not K == T:
    #     count = count + 1
    #     find_shortest(K,T)

    return find_shortest(K,T)



x = minMoves(10, 5, 5, 1, 2)

print(x)