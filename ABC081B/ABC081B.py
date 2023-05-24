#https://atcoder.jp/contests/abs/tasks/abc081_b
import sys

N = int(sys.stdin.readline().strip())

A = sys.stdin.readline().strip().split(" ")

round = 0
possible = True
while possible:
    B = []

    for i in A:
        i = int(i)
        if (i % 2 == 1) or (i == 0):
            possible = False
            break
        B.append(i/2)
    
    if possible:
        A = B
        round = round +1

print(round)