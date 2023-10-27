class Instant:
    def __init__(self, h=0, m=0, s=0):
        # self.h = h + m//60 + s//3600
        # self.m = m +
        # self.s = s
     # def __init__(self,h=0,m=0,s=0):
     #    self.hh = h + m//60 + s//3600
     #    self.mm = m%60 + (s%3600)//60
     #    self.ss = s%6



    def __str__(self):
        s =[]
        if self.h!=0: s += [f"{self.h}h"]
        if self.m!=0: s += [f"{self.m}m"]
        if self.s!=0: s += [f"{self.s}s"]
        return " ".join(s)


