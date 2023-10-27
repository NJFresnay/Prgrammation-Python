class StyloCouleur():
    def __init__(self,col):
        super().__init__()
        if col in ["vert","rouge","bleue","noire"]:
            self.col = col
        else :
            raise SyntaxError

    def print(self, chaine):
        m = len(chaine)
        n = chaine.split(" ")
        if (n[0] == self.col):
            match self.col:
                case "vert":
                    print("\x1b[32m",str(n[0])+' '+str(n[1]))
                    print("\x1b[0m")
                    pass
                case "bleue":
                    print("\x1b[34m",str(n[0])+' '+str(n[1]))
                    print("\x1b[37m")
                    pass
                case "noire":
                    print("\x1b[30m",str(n[0])+' '+str(n[1]))
                    print("\x1b[37m")
                    pass
                case "rouge":
                    print("\x1b[31m",str(n[0])+' '+str(n[1]))
                    print("\x1b[37m")
                    pass
        else:
            raise SyntaxError
