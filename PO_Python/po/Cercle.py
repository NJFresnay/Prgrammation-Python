import Point

class Cercle : pass

def examine(un_cercle):
  return f"Soit un cercle {un_cercle.nom} de centre {Point.examine(un_cercle.centre)} et de rayon {un_cercle.rayon}"

def deplace( C,p):
    C.centre = p
    return f"Cercle {C.nom} (centre {Point.examine(C.centre)}, rayon : {C.rayon})"

def copie(c):
    copie.nom = f"copie_de_{c.nom}"
    copie.centre = c.centre
    copie.rayon = c.rayon
    return f"Soit un cercle {copie.nom} de centre {Point.examine(copie.centre)} et de rayon {copie.rayon}"
