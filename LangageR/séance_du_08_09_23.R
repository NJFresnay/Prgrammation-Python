### les fonctions

carre <- function(x) x^2
carre(2)

fonction_test <- function(x) {
  # renvoie le carre si x est positif et valeur absolue sinon
  if (x<0) return(carre(x))
  else return(abs(x))
}

fonction_test(-3)

