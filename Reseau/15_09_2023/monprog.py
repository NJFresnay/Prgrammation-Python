#!/bin/env python3

# x=1
# y=1
# z=1
# def f():
#   def g():
#     z=3
#     print(x,y,z)
#   y=2
#   print(x,y,z)
#   g()
# print(x,y,z)
# f()
# print(x,y,z)


# # Global scope
# country = "Switzerland"
# capital = "Bern"
#
# def printCountry():
#   # Function scope
#   print(country)
#
# def printCountryAndCapital():
#   # Function scope
#   country = "Italy"
#   capital = "Rome"
#
#   def printCapital():
#     print(capital)
#
#   printCountry()
#   printCapital()
#
# printCountryAndCapital()


#import mon_module        # charge mon_module.py

#print(ma_variable) # erreur !
print(mon_module.ma_variable)

ma_variable = 1
print(f"{__name__=}")
print(ma_variable)
print(mon_module.ma_variable)

print(mon_module.ma_fonction())

mon_module.ma_variable = 5
print(mon_module.ma_fonction())

print(" Aie Aie Aie:")

