class AdresseIP:
    def __init__(self,a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def classe(self):
        if self.a & 0b10000000 == 0b00000000:
            self.classe = "A"
        elif self.a & 0b11000000 == 0b10000000:
            self.classe = "B"
        elif self.a & 0b11100000 == 0b11000000:
            self.classe = "C"

        return self.classe

    def reseau(self):
        if self.classe == "A":
            self.reseau = str(self.a)+"."

        elif self.classe == "B":
            self.reseau = str(self.a)+"."+ str(self.b)+"."

        elif self.classe == "C":
            self.reseau = str(self.a) +"." +str(self.b) +"."+ str(self.c)+"."
        return self.reseau

    def equipement(self):
        if self.classe == "A":
            self.equipement = "." + str(self.b) + "." +str(self.c) +"."+ str(self.d)

        elif self.classe == "B":
            self.equipement = "." + str(self.c) +"."+ str(self.d)

        elif self.classe == "C":
            self.equipement ="." + str(self.d)

        return self.equipement
