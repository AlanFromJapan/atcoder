#https://atcoder.jp/contests/abc302/tasks/abc302_e
import io
import sys

DEBUG = True

l = sys.stdin.readline().strip()
N = int(l.split(" ")[0])
Q = int(l.split(" ")[1])

VERTEX = [[] for i in range(N)]

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

def addEdge(src, dest):
    global VERTEX
    VERTEX[src-1].append(dest)
    VERTEX[dest-1].append(src)

def removeEdge(src):
    global VERTEX
    for e in VERTEX[src-1]:
        VERTEX[e-1].remove(src)
    VERTEX[src-1].clear()


def countOrphans():
    connected = []

    for v in VERTEX:
        for e in v:
            if e not in connected:
                connected.append(e)
    return N - len(connected)


i = 0
while i < Q:
    l = sys.stdin.readline().strip().split(" ")
    #DBG(f"{l}")
    if l[0] == "1":
        addEdge(int(l[1]), int(l[2]))
    else:
        removeEdge(int(l[1]))
    
    print(f"{countOrphans()}")
    
    i = i+1



