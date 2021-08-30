def NinjaChess(king, ninja):
    for i in range(0,8):
            if(chr(i+97) == ninja[0]):
                a1=i
            if(chr(i+97) == king[0]):
                a2=i
    b1= int(ninja[1])-1
    b2 = int(king[1])-1
    # (a1, b1) : Position of ninja in chess board matrix
    # (a2, b2) : Position of king in chess board matrix

    # Brd is a 8x8 matrix of chessboard
    brd = []
    for i in range(0,8):
        tmp = []
        for j in range(0,8):
            tmp.append(0)
        brd.append(tmp)
    
    #Ninja Row move
    for i in range(0,8):
        if(i == a2 and b1 == b2):
            break
        brd[i][b1] = 1
    #Ninja Column move
    for j in range(0,8):
        if(a1 == a2 and j == b2):
            break
        brd[a1][j] = 1

    #Ninja diagonal move
    for i in range(0,8):
        if(a1+i < 8 and b1+i < 8):
            if(a1+i == a2 and b1+i == b2):
                break
            brd[a1+i][b1+i] = 1
    for i in range(0,8):
        if(a1-i >= 0 and b1-i >= 0):
            if(a1-i == a2 and b1-i == b2):
                break
            brd[a1-i][b1-i] = 1
    for i in range(0,8):
        if(a1+i < 8 and b1-i >= 0):
            if(a1+i == a2 and b1-i == b2):
                break
            brd[a1+i][b1-i] = 1
    for i in range(0,8):
        if(a1-i >=0 and b1+i <8):
            if(a1-i == a2 and b1+i == b2):
                break
            brd[a1-i][b1+i] = 1

    #Ninja knight move
    if(a1+2<8 and b1+1<8):
        brd[a1+2][b1+1] = 1
    if(a1+2<8 and b1-1>=0):
        brd[a1+2][b1-1] = 1
    if(a1+1<8 and b1+2<8):
        brd[a1+1][b1+2] = 1
    if(a1+1<8 and b1-2>=0):
        brd[a1+1][b1-2] = 1
    if(a1-1>=0 and b1+2<8):
        brd[a1-1][b1+2] = 1
    if(a1-1>=0 and b1-2>=0):
        brd[a1-1][b1-2] = 1
    if(a1-2>=0 and b1+1<8):
        brd[a1-2][b1+1] = 1
    if(a1-2>=0 and b1-1>=0):
        brd[a1-2][b1-1] = 1
    
    ans = [0, 0, 0, 0] #answer
    
    brd[a1][b1] = 9
    brd[a2][b2] = 8
    for i in range(0,8):
        print(brd[i])

    for i in range(0,8):
        for j in range(0,8):
            if(i != a1 or j != b1):        #Not in Ninja's Position
                if(abs(i-a2)>1 or abs(j-b2)>1):    #Not in White King's Reach
                    safe = 1
                    valid = 0
                    if(brd[i][j] == 1):     #Check or Checkmate
                        safe = 0

                    for x in range(-1,2):
                        for y in range(-1,2):
                            if((i+x >= 0 and i+x < 8) and (j+y >= 0 and j+y < 8) and not(x==0 and y==0)):  #Valid square
                                if(brd[i+x][j+y] == 0):
                                    valid = 1
                    if((abs(i-a1)<2 and abs(j-b1)<2) and not(abs(a1-a2)<2 and abs(a1-a2)<2)):
                        valid = 1

                    if(safe==0 and valid==0):   #checkmate
                        ans[0]+=1
                    
                    if(safe==0 and valid==1):   #check
                        ans[1]+=1

                    if(safe==1 and valid==0):   #stalemate
                        ans[2]+=1

                    if(safe==1 and valid==1):   #NOICE
                        ans[3]+=1

                    

    return ans

        

print("#####",NinjaChess("a3", "e4"))