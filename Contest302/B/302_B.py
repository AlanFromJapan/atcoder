import io
import sys

SNUKE = "snuke"
M = []
l = sys.stdin.readline().strip()
H = int(l.split(" ")[0])
W = int(l.split(" ")[1])

i = 0
while i < H:
    l = sys.stdin.readline().strip()
    M.append(l)
    i = i+1

#Now process
def DBG(s):
    #print (s)
    pass

def findNextS(x,y):
    if x >= W:
        x = 0
        y = y  + 1
    if y >= H:
        raise Exception ("Not found")

    while M[y][x] != 's':
        x = x + 1
        if x >= W:
            x = 0
            y = y  + 1
        if y >= H:
            raise Exception ("Not found")
    return x, y

def checkPos (x,y, pos):
    return x >= 0 and x < W and y >=0 and y < H and M[y][x] == SNUKE[pos]

def findSnuke2(x,y,dx,dy):
    resp = []
    for pos in range(1, len(SNUKE)):
        if checkPos(x + pos * dx,y + pos * dy, pos):
            resp.append([x + pos * dx,y + pos * dy])
        else:
            resp.clear()
            break
    if len(resp) > 0:
        return resp
    return None
        
def findSnuke(x,y):
    #x,y IS a S, so skip

    #Horizontal
    # for pos in range(1, len(SNUKE)):
    #     dx = 1
    #     dy = 0
    #     if checkPos(x + pos * dx,y + pos * dy, pos):
    #         resp.append([x + pos * dx,y + pos * dy])
    #     else:
    #         resp.clear()
    #         break
    # if len(resp) > 0:
    #     return resp
    resp = findSnuke2(x,y,1,0)
    if resp != None:
        return resp
    
    resp = findSnuke2(x,y,-1,0)
    if resp != None:
        return resp
    
    resp = findSnuke2(x,y,0,1)
    if resp != None:
        return resp
    
    resp = findSnuke2(x,y,0,-1)
    if resp != None:
        return resp
    
        
    resp = findSnuke2(x,y,1,1)
    if resp != None:
        return resp
    resp = findSnuke2(x,y,-1,1)
    if resp != None:
        return resp    
    resp = findSnuke2(x,y,1,-1)
    if resp != None:
        return resp
    resp = findSnuke2(x,y,-1,-1)
    if resp != None:
        return resp
        
    return None


#DBG(M)
finished = False
x,y = 0,0
while not finished:
    x,y = findNextS(x,y)
    DBG(f"FOund s at ({x}, {y})")
    
    r = findSnuke(x,y)
    if (r != None):
        DBG(f"Found SNUKE at {r}")
        finished = True
        r.insert(0, [x,y])
        for rr in r:
            print(f"{rr[1] + 1} {rr[0] +1}")
    else:
        DBG("Nope...")
        x = x + 1
