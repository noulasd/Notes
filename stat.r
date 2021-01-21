install.packages("readxl")
library("readxl")
setwd("C:/Users/dimit/Desktop/Ergasia_Statistikis")
data1 <- read_excel("ergasia_12/ergasia_12.xls")
head(data1)


g1diff <- data1$night[data1$group==1] - data1$day[data1$group==1]
g2diff <- data1$night[data1$group==2] - data1$day[data1$group==2]

shapiro.test(g1diff)
shapiro.test(g2diff)

num <- 625
set.seed(num)

xsim <- rnorm(50)
ysim <- rt(50, df=3)
zsim <- rt(50, df=10)


shapiro.test(xsim)
shapiro.test(ysim)
shapiro.test(zsim)



t.test(g1diff,g2diff,var.equal=FALSE,conf.level = 0.95)

t.test(g1diff,g2diff,var.equal=FALSE,conf.level = 0.95,alternative="greater")
t.test(g1diff,g2diff,var.equal=FALSE,conf.level = 0.95,alternative="less")


logx <- log(data1$night[data1$group==1] / data1$day[data1$group==1])
logy <- log(data1$night[data1$group==2] / data1$day[data1$group==2])


shapiro.test(logx)
shapiro.test(logy)


t.test(logx,logy,var.equal=FALSE,conf.level = 0.95)

t.test(logx,logy,var.equal=FALSE,conf.level = 0.95,alternative="greater")