#!/bin/env python3

class S(str):
    def __init__(self,chaine=""):
        self.chaine = chaine

    def __getitem__(self,char):
       return self.find(char)


# class Diviseurs(int):
#     def __init__(self, n):
#         self.n = n
#
#     def __getitem__(self, nb):
#         if self.n < nb:
#             raise IndexError("Erreur404!")
#         elif nb>0:
#             return  nb % self.n == 0
#         else:
#             return False

class Indicable():
    def __getitem__(self,i):
        return i*i


class Diviseurs(int):
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return It(self)



    class It():
        def __init__(self, d):
            self.div = d
            self.i = 0

        def __next__(self):
            if self.i == self.div.n:
                raise StopIteration()

            self.i += 1
            while self.div.n %self.i != 0 :
                self.i +=1
            return self.i

        def __iter__(self):
            return self



# try:
#     with open('data', 'w') as mon_fichier:
#         for i in range(-10,10):
#             print(1/i, file=mon_fichier)
# except ZeroDivisionError:
#     print("error")
#
# try:
#     mon_fichier = open("data1", "w")
#     for i in range(-10,10):
#         print(1/i, file=mon_fichier)
#     mon_fichier.close()
# except ZeroDivisionError :
#     print("error")
#

### les context manager
class Balise:
    niv = 0
    def __init__(self,s):
        self.s = s

    def __enter__(self):
        Balise.niv += 1
        print(" "*Balise.niv ,f"<{self.s}>")
        return self

    def __exit__(self, type, value, traceback):
        print(" "*Balise.niv ,  f"</{self.s}>")
        Balise.niv -= 1

    def print(self,sms):
        print (" "*(Balise.niv+1), sms)



with Balise("chapitre") as c1:
    with Balise("titre") as t1:
        t1.print("Titre du chapitre 1")
    with Balise("paragraphe") as p1:
        p1.print("Phrase 1.")
        p1.print("Phrase 2.")
    with Balise("paragraphe") as p2:
        p2.print("Phrase 1.")
        p2.print("Phrase 2.")




class Top:
    def __enter__(self):
        self.t0 = time.time()












if __name__=="__main__":



    s = S("Hello World !")
    # print(s['e'], end=" ")  # indice du premier 'e'
    # print(s['o'], end=" ")

    # d12 = Diviseurs(12)
    # print(f"{d12[4]}")

    mon_indicable = Indicable()

    # for k in mon_indicable:
    #     print(k,end=" ")
    #
    # d12 = Diviseurs(13)
    #
    # for i in d12:
    #     print(i,end=" ")

#     for i,d in enumerate(Diviseurs(100)):
#         if d:
#             print(i,end=" ")
#

    # d = Diviseurs(50)
    # it1 = Diviseurs.It(d)
    # for i in it1:
    #     it2 = Diviseurs.It(d)
    #     for j in it2:
    #         print(f"({i},{j})", end=" ")
