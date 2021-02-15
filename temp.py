from math import floor
def simulate_path(inp_x,inp_y,inp_vel_x,inp_vel_y):

        x = start_x = inp_x
        end_x = inp_x + inp_vel_x

        y = start_y = inp_y
        end_y = inp_y + inp_vel_y

        v = abs(end_y - start_y)
        h = abs(end_x - start_x)
        
        dir_x = int(inp_vel_x + 0.1/abs(inp_vel_x+ 0.1))
        dir_y = int(inp_vel_y+ 0.1/abs(inp_vel_y+ 0.1))
        

        q = floor(h/(v+1))
        print(h,v)
        r = h%(v+1)
    
    
        # for i in range(v):
        #     if(i != v -1):
        #         for j in range(q+1):
        #             x += dir_x
        #             l.append((x,y)) 
        #         y += dir_y
        #         l.append((x,y))
        #     else:
        #         for j in range(q):
        #             x += dir_x
        #             l.append((x,y))

        # return l
        l = []
        for i in range(v+1):
            if(r >0):
                #l.append(q+1)
                for j in range(q+1):
                    x+= dir_x
                    l.append((x,y))
                r -= 1
            else:
                #l.append(q)
                for j in range(q):
                    x += dir_x
                    l.append((x,y))
            if(i < v):
                y+= dir_y
                l.append((x,y))
        return l
            

l = simulate_path(1,3,0,1)
print(l)

