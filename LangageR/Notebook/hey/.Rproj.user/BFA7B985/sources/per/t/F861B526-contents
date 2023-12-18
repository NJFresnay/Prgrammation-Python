### les fonctions

carre <- function(x) x^2
carre(2)

fonction_test <- function(x) {
  # renvoie le carre si x est positif et valeur absolue sinon
  if (x<0) return(carre(x))
  else return(abs(x))
}

fonction_test(-3)

# une fonction automatiquement la dernière ligne du code

fp <- function(k, n, start = 0.05, TOL = 1E-10)
{
  ## Fonction pour trouver par la méthode du point
  ## fixe le taux d'intérêt pour lequel une série de
  ## 'n' paiements vaut 'k'.
  ##
  ## ARGUMENTS
  ##
  ##
  ##k: la valeur présente des paiements
  ##
  ##n: le nombre de paiements
  ## start: point de départ des itérations
  ##
  ##TOL: niveau de précision souhaité
  ##
  ## RETOURNE
  ##
  ## Le taux d'intérêt
  i <- start
  repeat
  {
    it <- i
    i <- (1 - (1 + it)^(-n))/k
    if (abs(i - it)/it < TOL)
      break
  }
  i
}

x <- 1:3; y<- 4:6
f <- function(x,y) x*y^2
outer(x,y,f)

# méthode simplifiée
outer(x,y, function(x,y) x*y^2 )






# EXERCICE 5.9

# 5.1
echantillon <- rnorm(100)

variance <- function(x, biased= FALSE) {
  if (biased)  return(1/(length(x)) * sum(x - mean((x))^2))
  else return(1/(length(x)-1) * sum(x - mean((x))^2))
}

variance(echantillon)
variance(echantillon,TRUE)  



matrix2 <- function(donnee, nrow=3, ncol=3, bycol=FALSE, dimnames = FALSE) {
  donnee <- rep(donnee, length=nrow*ncol)
  if (bycol) dim(donnee)= c(nrow,ncol)
  else {
    dim(donnee) = c(ncol,nrow)
    donnee <- t(donnee)
  }
  #names(donnee) <- dimnames
  donnee
}

v <- 1:10
matrix2(v)



# 5.3

# Fonction phi de densité
v <- rnorm(100)

phi <- function(vec) {
  return (  1/(sqrt(2*pi)) * exp((-vec^2)/2) )
}

phi(v)

dnorm(v)

x <- seq(-25,30,length.out=100)

# plot(x, phi(x), 
#      type="l", xlab="abscisses", ylab="phi(x)", abline(h=0,lty=2,col="green"),
#      main = "Densité de la loi gaussienne", panel.first = grid())


#curve(dnorm(c), from = 2, to=2, n=10) qui permet aussi de rajouter une courbe sur un graphe



# Parabole
#(a*x^2+ b*x +c)

parabol <- function(a,b,c) {
  x <- seq(-25,30,length.out=100)
  {
    delta = b^2-4*a*c
    if (delta > 0) {
      x1 <- (-b-sqrt(delta))/2*a
      x2 <- (-b+sqrt(delta))/2*a
      
    }
    else if (delta == 0) {
      x1 <- -b / 2*a
      x2 <- x1
    }
    else 
      x1 <- (-b-sqrt(delta))/2*a
      x2 <- (-b+sqrt(delta))/2*a
  }
  
  curve(a*x^2+b*x+c,from=, to=10, ylab= "f(x)", 
         main= "Parabole de a*x^2+b*x+c",lwd=2)
  
  if (delta >=0) {
    points(c(x1,x2), c(0,0), pch=4, col="blue", lwd=3)
    abline(h=0, lty=2)
    abline(v=c(x1,x2),lty=2)
  }
  return(list(x1,x2,delta))
  
}


data <- iris
head(data)

cor(iris[,1:4])
plot(iris[1:4], col=data$Species, pch=as.numeric(data$Species))
