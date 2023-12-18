#!/bin/env python3

import Animaux

animal = Animaux.Animaux("John")
#print(animal)

animal1 = Animaux.Digitigrade("Hey")
#print(animal1)
#print(animal1)
# animal2 = Animaux.Digitigrade("Hallo")
# print(animal2)
# print(animal2.fuite())

parcKruger = Animaux.Territoire()
parcKruger += Animaux.Autruche("Polux")
parcKruger += Animaux.Autruche("Cheetah")
parcKruger += Animaux.Chat("Zouzou")

print(parcKruger)

if __name__ == "__main__":
    pass
