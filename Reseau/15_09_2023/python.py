#!/bin/env python3

# import math
#
# x = float(input("entrer un nombre : "))
# if x>=0:
#     print(math.sqrt(x))


# La boucle while
# from math import log
#
# i = 1
# r = log(1)
# while (r<4):
#     print(i,r)
#     i += 1
#     r = log(i)


# def f(k):
#     return k**2 + k**3
#
# for i in range(1,11):
#     print(f"sum of the square and cube of {i} is {f(i)}")


import sys

def C(n,p):
  if (p==0 or n==p):
    return 1
  else:
    return C(n-1,p)+C(n-1,p-1)

if __name__=="__main__":
  n = int(sys.argv[1])
  p = int(sys.argv[2])
  if p<=n and n>=0 and p>=0:
    print(f"C({n},{p})={C(n,p)}")
