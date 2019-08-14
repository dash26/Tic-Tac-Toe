print "x and y key values for reference ..\n"
print  " 00 01 02 \n \n"," 10 11 12 \n \n"," 20 21 22 \n \n"
 
matrix = [[' ',' ',' '],
          [' ',' ',' '],
          [' ',' ',' ']]
 
session = True
game_count = 0
#..........................................................................................................................................

#main function
 
def mainfun(matrix,game_count,session):
 
 
    
    a = input("Enter the x position :")
    b = input("Enter the y position :")
 

    if(matrix[a][b] != ' '):
        print "Space already filled ! Select another spot"
        
    else:
        matrix[a][b] = 'X'    
        defend(matrix)
        display(matrix)
        result = wincheck(matrix)
        if(result == 'X wins' or result == "O wins"):
            if(result == "O wins"):
                result = "<=============== O WINS ! YOU LOSE  ==================>"
                print result
                exit()
            elif(result == "X wins"):
                result = "<=============== GODAMNIT !!! YOU WIN :) ==================>"
                print result
                exit()
 

 
                
#..........................................................................................................................................
    
#Display    

def display(matrix):
    for i in range(3):
        for j in range(3):
            print matrix[i][j]+' | ',
        print "\n"
#...........................................................................................................................................

        
#Check for victory
        
def wincheck(matrix):
    
    
    xh1=0
    xh2=0
    xh3=0
    xv1=0
    xv2=0
    xv3=0

    oh1=0
    oh2=0
    oh3=0
    ov1=0
    ov2=0
    ov3=0

    xd1=0
    xd2=0

    od1=0
    od2=0

    v = 2
    #horizontal first row
    for i in range(3):
        if(matrix[0][i] == 'X'):
            xh1= xh1 + 1
    if(xh1 == 3):
        return "X wins"
    for i in range(3):
        if(matrix[0][i] == 'O'):
            oh1= oh1 + 1 
    if(oh1 == 3):
        
        return "O wins"

    #horizontal second row     
    for i in range(3):
        if(matrix[1][i] == 'X'):
            xh2= xh2 + 1
             
    if(xh2 == 3):
        return "X wins"

    for i in range(3):
        if(matrix[1][i] == 'O'):
            oh2= oh2 + 1

    if(oh2 == 3):
        return "O wins"

    #horizontal Third row
    for i in range(3):
        if(matrix[2][i] == 'X'):
            xh3= xh3 + 1
 
    if(xh3 == 3):
        return "X wins"

    for i in range(3):
        if(matrix[2][i] == 'O'):
            oh3= oh3 + 1

    if(oh3 == 3):
        return "O wins"
    
    #Vertical first row
    for i in range(3):
        if(matrix[i][0] == 'X'):
            xv1= xv1 + 1
 
    if(xv1 == 3):
        return "X wins"

    for i in range(3):
        if(matrix[i][0] == 'O'):
            ov1= ov1 + 1

    if(ov1 == 3):
        return "O wins"

    #Vertical Second row
    for i in range(3):
        if(matrix[i][1] == 'X'):
            xv2= xv2 + 1
 
    if(xv2 == 3):
        return "X wins"

    for i in range(3):
        if(matrix[i][1] == 'O'):
            ov2= ov2 + 1

    if(ov2 == 3):
        return "O wins"

   #Vertical Third row
    for i in range(3):
        if(matrix[i][2] == 'X'):
            xv3 = xv3 + 1
 
    if(xv3 == 3):
        return "X wins"

    for i in range(3):
        if(matrix[i][2] == 'O'):
            ov3= ov3 + 1

    if(ov3 == 3):
        return "O wins"


    #Left Diagonal
    for i in range(3):
        for j in range(3):
            if(i == j):
                if(matrix[i][j] == 'X'):
                    xd1 = xd1 + 1
 
    if(xd1 == 3):
        return "X wins"

    for i in range(3):
        for j in range(3):
            if(i == j):
                if(matrix[i][j] == 'O'):
                    od1 = od1 + 1
 
    if(od1 == 3):
        return "O wins"

    #Right Diagonal
    for i in range(3):
 
        if(matrix[i][v] == 'X'):
            xd2 = xd2 + 1
        v = v -1
    if(xd2 == 3):
        return "X wins"

    for i in range(3):
        if(matrix[i][v] == 'O'):
            od2 = od2 + 1
        v = v - 1
        
    if(od2 == 3):
        return "O wins"

 
#........................................................................................................................................


#Defend

def defend(matrix):
    c1=0
    c2=0
    c3=0
    c4=0
    c5=0
    c6=0

    c7=0
    c8=0

    v1 =2
    v2 =2

    movemade= 0
    #Horizontal 1
    for i in range(3):
        if(matrix[0][i] == 'X'):
            c1 +=1
    if(c1 == 2):
        val = winordefend(matrix)
        if(val == -1):
            return -1
        for i in range(3):
            if(matrix[0][i] == ' '):
                print "defending .."
                matrix[0][i] = 'O'
                movemade = 1
                return -1
                 

    #Horizontal 2
    for i in range(3):
        if(matrix[1][i] == 'X'):
            c2 +=1
    if(c2 == 2):
        val = winordefend(matrix)
        if(val == -1):
            return -1
        for i in range(3):
            if(matrix[1][i] == ' '):
                print "defending .."
                matrix[1][i] = 'O'
                movemade = 1
                return -1

    #Horizontal 3
    for i in range(3):
        if(matrix[2][i] == 'X'):
            c3 +=1
    if(c3 == 2):
        val = winordefend(matrix)
        if(val == -1):
            return -1
        for i in range(3):
            if(matrix[2][i] == ' '):
                print "defending .."
                matrix[2][i] = 'O'
                movemade = 1
                return -1

    #Vertical 1
    for i in range(3):
        if(matrix[i][0] == 'X'):
            c4 +=1
    if(c4 == 2):
        val = winordefend(matrix)
        if(val == -1):
            return -1
        for i in range(3):
            if(matrix[i][0] == ' '):
                print "defending .."
                matrix[i][0] = 'O'
                movemade = 1
                return -1

    #Vertical 2
    for i in range(3):
        if(matrix[i][1] == 'X'):
            c5 +=1
    if(c5 == 2):
        val = winordefend(matrix)
        if(val == -1):
            return -1
        for i in range(3):
            if(matrix[i][1] == ' '):
                print "defending .."
                matrix[i][1] = 'O'
                movemade = 1
                return -1


    #Vertical 3
    for i in range(3):
        if(matrix[i][2] == 'X'):
            c6 +=1
    if(c6 == 2):
        val = winordefend(matrix)
        if(val == -1):
            return -1
        for i in range(3):
            if(matrix[i][2] == ' '):
                print "defending .."
                matrix[i][2] = 'O'
                movemade = 1
                return -1

    #Diagonal left
    for i in range(3):
        for j in range(3):
            if(i == j):
                if(matrix[i][j] == 'X'):
                    c7 += 1
    if(c7 == 2):
        val = winordefend(matrix)
        if(val == -1):
            return -1
        for i in range(3):
            for j in range(3):
                if(i == j):
                    if(matrix[i][j] == ' '):
                        print "defending .."
                        matrix[i][j] = 'O'
                        movemade = 1
                        return -1

    #Diagonal right
    for i in range(3):
        if(matrix[v1][i] == 'X'):
            c8+=1
        v1 -=1
    if(c8 == 2):
        val = winordefend(matrix)
        if(val == -1):
            return -1
        for i in range(3):
            if(matrix[v2][i] == ' '):
                print "defending .."
                matrix[v2][i] = 'O'
                movemade = 1
                return -1
            v2 -=1
     

    if(movemade == 0):
        print "random"
        for i in range(3):
            for j in range(3):
                if(matrix[i][j] == ' '):
                    matrix[i][j] = 'O'
                    movemade += 1
                    return -1
            
#.........................................................................................................................................
#This function will tell the computer to win instead of defending

def winordefend(matrix):
    win =0

    #first check if we can win
    chance1=0
    chance2=0
    chance3=0
    chance4=0
    chance5=0
    chance6=0
    chance7=0
    chance8=0

    v1 =2
    v2 =2
   

    #Horizontal 1
    for i in range(3):
        if(matrix[0][i] == 'O'):
            chance1 +=1
    if(chance1 == 2):
        for i in range(3):
            if(matrix[0][i] == ' '):
                print "attacking 1.."
                matrix[0][i] = 'O'
                return -1
                 

    #Horizontal 2
    for i in range(3):
        if(matrix[1][i] == 'O'):
            chance2 +=1
    if(chance2 == 2):
        for i in range(3):
            if(matrix[1][i] == ' '):
                print "attacking chance2.."
                matrix[1][i] = 'O'
                return -1

    #Horizontal 3
    for i in range(3):
        if(matrix[2][i] == 'O'):
            chance3 +=1
    if(chance3 == 2):
        for i in range(3):
            if(matrix[2][i] == ' '):
                print "attacking 3.."
                matrix[2][i] = 'O'
                return -1

    #Vertical 1
    for i in range(3):
        if(matrix[i][0] == 'O'):
            chance4 +=1
    if(chance4 == 2):
        for i in range(3):
            if(matrix[i][0] == ' '):
                print "attacking 4.."
                matrix[i][0] = 'O'
                return -1

    #Vertical 2
    for i in range(3):
        if(matrix[i][1] == 'O'):
            chance5 +=1
    if(chance5 == 2):
        for i in range(3):
            if(matrix[i][1] == ' '):
                print "attacking 5.."
                matrix[i][1] = 'O'
                return -1


    #Vertical 3
    for i in range(3):
        if(matrix[i][2] == 'O'):
            chance6 +=1
    if(chance6 == 2):
        for i in range(3):
            if(matrix[i][2] == ' '):
                print "attacking 6.."
                matrix[i][2] = 'O'
                return -1

    #Diagonal left
    for i in range(3):
        for j in range(3):
            if(i == j):
                if(matrix[i][j] == 'O'):
                    chance7 += 1
    if(chance7 == 2):
        for i in range(3):
            for j in range(3):
                if(i == j):
                    if(matrix[i][j] == ' '):
                        print "attacking 7.."
                        matrix[i][j] = 'O'
                        return -1

    #Diagonal right
    for i in range(3):
        if(matrix[i][v1] == 'O'):
            chance8+=1
        v1 -=1
    if(chance8 == 2):
        for i in range(3):
            if(matrix[i][v2] == ' '):
                print "attacking 8.."
                matrix[i][v2] = 'O'
                return -1
            v2 -=1
#..........................................................................................................................................

def exit():
    try:
        exit()
    except:
        exit()

#......................................................................................................................................
#User Choice
 
while(session):
    game_count = game_count+1
    if(game_count == 6):
        print "<=======OOH LOOK AT YOU ! STILL NOT GOOD ENOUGH !! ITS A Tie ======>"
        exit()
    if(game_count == 1):
        a = input("Enter the x position :")
        b = input("Enter the y position :")
        if(matrix[a][b] != ' '):
            print "Space already filled ! Select another spot"
        else:
            matrix[a][b] = 'X'
            if(matrix[1][1] == 'X'):
                matrix[0][0] = 'O'
            else:
                matrix[1][1] = 'O'
        display(matrix)
    else:       
        mainfun(matrix,game_count,session) 


    
