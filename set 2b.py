#anju
import sys, string, math
a,b = map(int,input().split())
b = b%a
L1 = list(map(int,input().split()))
L2 = L1[-b:] + L1[:-b]
print(*L2)