library(ggplot2)

ozone <- read.csv2("/users/2024/ds1/123010405/Documents/OP/open_regression/data_ozone.csv", header=TRUE)
summary(ozone)

# représentation graphique
ggplot(data = ozone, aes()) +
  geom_smooth(data=ozone)




# regression linéaire simple de max03 et T12

reg_simple <- lm(maxO3~T12, data = ozone)

summary(reg_simple)

ggplot(data = ozone, aes(x=T12, y=maxO3)) +
  geom_point()+
  stat_smooth(method = 'lm', se=FALSE, col="red")

# les valeurs ajustées
ozone$maxO3_aj <- reg_simple$fitted.values

ggplot(data = ozone, aes(x=maxO3, y=maxO3_aj))+
  geom_point()+
 geom_abline(intercept = 0, slope = 1,col="green")

# les résidus
ozone$residus <- reg_simple$residuals
ggplot(data = ozone, aes(x=residus))+
  geom_histogram(binwidth = 10, aes(y = ..density..))+
  ggtitle('Histogramme')
