#!/bin/env python3

def is_mutable(x,y):
  print(f'{type(x).__name__} is {"mutable" if x is y else "immutable"}')
#
# a = b = "uv"
# b += "w"
# is_mutable(a,b)
#
# a = b = [1,2]
# b += [3]
# print(is_mutable(a,b))
#
#
# a = {1,2}
# b=a
# a.add(9)
# print(a)
# print(b)
#
# is_mutable(a,b)

# les classe personnalisées sont mutables, de memes que les dictionnaires

# t = (1,2,[3,4])
# print(t, id(t) )      # (1,2,[3,4]) 139727011443776
# print(t[2],id(t[2]) ) # [3,4] 139727011443712
#
#
# l = t[2]
# l += [5]
# print(t,id(t))   # (1,2,[3,4,5]) 139727011443776
# print(t[2],id(t[2])  # [3,4,5] 139727011443712



from copy import copy

a = [1,2]
b = copy(a)
print(a is b)       # [1, 2] [1, 2] True

print(a,b,a is b)       # [1, 2] [1, 2] False
b += [3]
print(a,b)              # [1, 2] [1, 2, 3]

# une liste de liste garde un lien avec sa copie par la methode "copy"



if __name__ == "__main__":
    pass
