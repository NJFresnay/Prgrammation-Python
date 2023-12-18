#!/bin/env python3
# fichier exceptions1.py

# def myfunction():
#     x = 1/0
#
# def mafonction():
#     myfunction()
#
# def main():
#     mafonction()

# l = [1,2,3,4,5,6,7,8]
#
# def f(i):
#     f(l[i])
#
# def main():
#     f(0)


from math import sqrt as sqrt

def g(x):
    if sqrt(x)>2:
        f(x-10)
    else:
        return x

def f(x):
    g(x)

def main():
    f(45)

if __name__ == "__main__":
    main()
