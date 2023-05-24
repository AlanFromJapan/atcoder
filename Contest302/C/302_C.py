import io
import sys

DEBUG = False

l = sys.stdin.readline().strip()
N = int(l.split(" ")[0])
M = int(l.split(" ")[1])

S = []
i = 0
while i < N:
    l = sys.stdin.readline().strip()
    S.append(l)
    i = i+1

#Now process
def DBG(s):
    if not DEBUG:
        return
    print (s)

def DBGMX(s):
    if not DEBUG:
        return
    for l in s:
        print(l)

def distance(a,b):
    d = 0
    for i in range(M):
        if a[i] != b[i]:
            d = d + 1
    return d

#Calculate all the distances in a symetric matrix
DBG(S)
finished = False
dis = []
for i in range(N):
    dis.append([])
    for j in range(N):
        dis[i].append(distance(S[i], S[j]))

DBGMX(dis)

#Basically a path exists IF there is at least one word distant of 1 for each word. 
possible = True
for i in range(N):
    possible = possible and (1 in dis[i])    
print("Yes" if possible else "No")