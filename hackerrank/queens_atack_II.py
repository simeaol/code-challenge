#n: an integer, the number of rows and columns in the board
#k: an integer, the number of obstacles on the board 
#r_q: integer, the row number of the queen's position 
#c_q: integer, the column number of the queen's position 
#obstacles: a two dimensional array of integers where each element is an array of  integers, the row and column of an obstacle
def queen_atack(n, k, r_q, c_q, obstacles):
    resp = 0
    quen_pos = (r_q, c_q)

    cont = 0

    #from queen position to up 
    for up in range(r_q, -1, -1):        
        print("({},{})".format(up, c_q)) 
        tuples = (up, c_q)
        if(tuples == quen_pos):
            continue
        elif(tuples in obstacles):
            break
        else:
            cont += 1
    resp += cont
    print("From queen to up={}".format(cont))

    cont = 0 #reset counter

    #from queen position to down 
    for down in range(r_q+1, n):
        print("({},{})".format(down, c_q)) 
        tuples = (down, c_q)
        if(tuples == quen_pos):
            continue
        elif(tuples in obstacles):
            break
        else:
            cont += 1
    resp += cont
    print("From queen to down={}".format(cont))

    cont = 0
    #################################################################################
    #from queen position to left
    for left in range(c_q, -1, -1):
        print("({},{})".format(r_q, left)) 
        tuples = (r_q, left)
        if(tuples == quen_pos):
            continue
        elif(tuples in obstacles):
            break
        else:
            cont += 1
    resp += cont
    print("From queen to left-side={}".format(cont))

    cont = 0
    #from queen position to rigth
    for rigth in range(c_q+1, n):
        print("({},{})".format(r_q, rigth)) 
        tuples = (r_q, rigth)
        if(tuples == quen_pos):
            continue
        elif(tuples in obstacles):
            break
        else:
            cont += 1
    resp += cont
    print("From queen to rigth-side={}".format(cont))

    cont = 0
    diagonal_inc = c_q + 1
    #################################################################
    #from queen to main diagonal up
    for main_up in range(r_q, 0, -1):
        print("({},{})".format(main_up, diagonal_inc))
        tuples = (main_up, diagonal_inc)
        if(tuples == quen_pos):
            diagonal_inc += 1
            continue
        elif(tuples in obstacles):
            break
        else:
            cont += 1
            diagonal_inc += 1
    resp += cont
    print("From queen to main diagonal-up={}".format(cont))

    cont = 0
    diagonal_inc = c_q + 1
    #from queen to main diagonal down
    for main_up in range(r_q+1, n-1):
        if(diagonal_inc >= n):
            break
        print("({},{})".format(main_up, diagonal_inc))
        tuples = (main_up, diagonal_inc)
        if(tuples == quen_pos):
            diagonal_inc += 1
            continue
        elif(tuples in obstacles):
            break
        else:
            cont += 1
            diagonal_inc += 1
    resp += cont
    print("From queen to main diagonal-down={}".format(cont))

    ##########################################################################

    cont = 0
    diagonal_desc = c_q - 1
    #from queen to secundary diagonal
    for main_up in range(r_q-1, -1, -1):
        print("({},{})".format(main_up, diagonal_desc))
        tuples = (main_up, diagonal_desc)
        if(tuples == quen_pos):
            diagonal_desc -= 1
            continue
        elif(tuples in obstacles):
            break
        else:
            cont += 1
            diagonal_desc -= 1

    resp += cont
    print("From queen to secundary diagonal-up={}".format(cont))

    cont = 0
    diagonal_desc = c_q - 1
    #from queen to secundary diagonal-down
    for main_up in range(r_q+1, n):
        print("({},{})".format(main_up, diagonal_desc))
        tuples = (main_up, diagonal_desc)
        if(tuples == quen_pos):
            diagonal_desc -= 1
            continue
        elif(tuples in obstacles):
            break
        else:
            cont += 1
            diagonal_desc -= 1

    resp += cont
    print("From queen to secundary diagonal-down={}".format(cont))

    return resp


if __name__ == "__main__":
    '''n = 4
    k = 0
    r_q = 0
    c_q = 3
    obstacles = []'''

    n = 5
    k = 3
    r_q = 1
    c_q = 2
    obstacles = [(1,1), (0,4), (3, 2)]

    print("{}".format(queen_atack(n, k, r_q, c_q, obstacles)))



