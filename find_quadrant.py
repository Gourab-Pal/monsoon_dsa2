def find_quadrant(x,y):
    if((x>0) & (y>0)):
        return 1
    elif((x<0) & (y>0)):
        return 2
    elif((x<0) & (y<0)):
        return 3
    else:
        return 4
    
print(find_quadrant(1,1))