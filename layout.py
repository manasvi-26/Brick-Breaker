#CONTAINS CODE TO CREATE BRICK LAYOUTS FOR FIRST 2 LEVELS

#LAYOUT FOR LEVEL 1

def create_layout1(BRICK_LENGTH,BRICK_WIDTH):

    list = []
    row = 5
    start_col = 5
    end_col = 86

    col = 5
    for r in range(5):
        
        for i in range(10):
            list.append((row,col))
            col+= BRICK_LENGTH
       
        row+= BRICK_WIDTH
        col = start_col

    for r in [4,3,2,1]:
        
        col = start_col
        for i in range(r):
            list.append((row,col))   
            col +=  BRICK_LENGTH
     
        col = end_col
        for i in range(r):
            list.append((row,col))
            col -= BRICK_LENGTH
        
        row += BRICK_WIDTH
    return list


def create_layout2(BRICK_LENGTH,BRICK_WIDTH):
    list = []
    row = 3
    start_col = 5
    end_col = 86

    col = start_col
    for r in range(2):
        for c in range(10):
            list.append((row,col))
            col+= BRICK_LENGTH
       
        row+= BRICK_WIDTH
        col = start_col


    for r in range(6):
        for c in range(4):

            list.append((row,col))
            col += (3*BRICK_LENGTH)

        row += BRICK_WIDTH
        col = start_col
    
    for r in range(2):
        for c in range(10):
            list.append((row,col))
            col+= BRICK_LENGTH
       
        row+= BRICK_WIDTH
        col = start_col
    
    return list

