import io
import math
import sys

def process (a,b):
    #c = math.ceil(a / b) if a % b != 0 else  a //b 
    c = a // b + (1 if  a % b != 0 else 0)
    #print(f"A={a} B={b} Result={c}")
    print (c)

def fromFile():
    with open ("input.txt", "r") as f:
        while True:
            l = f.readline()
            if l == "":
                break

            ab = l.split(" ")
            a = int(ab[0])
            b = int(ab[1])
            process(a,b)

def fromStdin():
    for line in sys.stdin:
        l = line.rstrip()
        ab = l.split(" ")
        a = int(ab[0])
        b = int(ab[1])
        process(a,b)
        break

#fromFile()
fromStdin()