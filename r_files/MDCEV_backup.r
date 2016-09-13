##### MDCEV model for vehicle fleet mix #####
print('Getting arguments')
# args <- commandArgs(trailingOnly = TRUE)

# if(length(args)==0) {
# stop("Need args for this script file")
# } 

# for (val in args) {
# print(val)
# } 


##### Description #####
# This Code Estimates an MDCEV model of vehicle fleet mix with 1 outside good (non-motorized mileage)
# Gamma profile of the MDCEV model is estimated

library("utils")   # to use csv read function
library("foreign") # to use spss read function
library("pastecs") # to use descriptive statistics function
library("mlogit")
library("graphics")
library("VGAM")
library("ZeligChoice") # This package is for actual mlogit function
library("aod")
library("plotrix")
rm(list = ls())

# Read data
print("Reading data")
Data <<- read.table("/Users/James/Desktop/master_project/r_resources/Model_Estimation/az_hhld_vfc_cleaned_final.csv", header=T, sep=",") 

nobs <- 4262     #Number of observations in the dataset
numout <<- 1     #Number of outside goods (i.e., always consumed goods)
config <- 4      #Utility specification configuration, possible values: 1,4,5,6,7
alp0to1 <<- 1    #1 if you want the Alpha values to be constrained between 0 and 1, 0 otherwise
                 #putting _alp0to1 = 1 is recommended practice and can provide estimation stability

price <- 0       #1 if there is price variation across goods, 0 otherwise
nc <<- 14        #Number of alternatives (in the universal choice set) including outside goods
po <<- 7
ivuno <- 5
ivsero <- 6
wtind <<- 5

f  <-	c(167,	8,	9,	10,	11,	12,	13,	14,	15, 16, 17,	18,	19,	20)
fp	<-	c(5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5, 5)




## Constants Only Model
## First alternative is the outside good "Annual non motorized mileage"
# ivmt1  <-	c(6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,  6)
# ivmt2	<-	c(5,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,  6)
# ivmt3	<-	c(6,	5,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,  6)
# ivmt4	<-	c(6,	6,	5,	6,	6,	6,	6,	6,	6,	6,	6,	6,  6)
# ivmt5	<-	c(6,	6,	6,	5,	6,	6,	6,	6,	6,	6,	6,	6,  6)
# ivmt6	<-	c(6,	6,	6,	6,	5,	6,	6,	6,	6,	6,	6,	6,  6)
# ivmt7	<-	c(6,	6,	6,	6,	6,	5,	6,	6,	6,	6,	6,	6,  6)
# ivmt8	<-	c(6,	6,	6,	6,	6,	6,	5,	6,	6,	6,	6,	6,  6)
# ivmt9	<-	c(6,	6,	6,	6,	6,	6,	6,	5,	6,	6,	6,	6,  6)
# ivmt10	<-c(6,	6,	6,	6,	6,	6,	6,	6,	5,	6,	6,	6,  6)
# ivmt11	<-c(6,	6,	6,	6,	6,	6,	6,	6,	6,	5,	6,	6,  6)
# ivmt12	<-c(6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	5,	6,  6)
# ivmt13	<-c(6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	5,  6)
# ivmt14  <-c(6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,  5)


# Baseline utility specification
# Full Model
ivmt1 <- c(6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6);
ivmt2 <- c(5, 130, 132, 137, 159, 187, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6);
ivmt3 <- c(6, 6, 6, 6, 6, 6, 5, 136, 128, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6);
ivmt4 <- c(6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 127, 152, 159, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6);
ivmt5 <- c(6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 132, 136, 192, 188, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6);
ivmt6 <- c(6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 132, 192, 128, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6);
ivmt7 <- c(6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 47, 192, 127, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6);
ivmt8 <- c(6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 127, 136, 152, 159, 187, 190, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6);
ivmt9 <- c(6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 129, 141, 151, 200, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6);
ivmt10 <- c(6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 130, 133, 125, 191, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6);
ivmt11 <- c(6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 131, 138, 124, 160, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6);
ivmt12 <- c(6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 124, 152, 130, 196, 6, 6, 6, 6, 6, 6, 6, 6, 6);
ivmt13 <- c(6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 159, 128, 133, 196, 6, 6, 6, 6);
ivmt14 <- c(6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 124, 151, 138);



# Satiation parameter (alpha) specification
# First alternative is the outside good "Annual non motorized mileage"

ivdt1  <-	c(5,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,  6)
ivdt2	<-	c(6,	5,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,  6)
ivdt3	<-	c(6,	6,	5,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,  6)
ivdt4	<-	c(6,	6,	6,	5,	6,	6,	6,	6,	6,	6,	6,	6,	6,  6)
ivdt5	<-	c(6,	6,	6,	6,	5,	6,	6,	6,	6,	6,	6,	6,	6,  6)
ivdt6	<-	c(6,	6,	6,	6,	6,	5,	6,	6,	6,	6,	6,	6,	6,  6)
ivdt7	<-	c(6,	6,	6,	6,	6,	6,	5,	6,	6,	6,	6,	6,	6,  6)
ivdt8	<-	c(6,	6,	6,	6,	6,	6,	6,	5,	6,	6,	6,	6,	6,  6)
ivdt9	<-	c(6,	6,	6,	6,	6,	6,	6,	6,	5,	6,	6,	6,	6,  6)
ivdt10	<-	c(6,	6,	6,	6,	6,	6,	6,	6,	6,	5,	6,	6,	6,  6)
ivdt11	<-	c(6,	6,	6,	6,	6,	6,	6,	6,	6,  6,	5,	6,	6,  6)
ivdt12	<-	c(6,	6,	6,	6,	6,	6,	6,	6,	6,  6,	6,	5,	6,  6)
ivdt13	<-	c(6,	6,	6,	6,	6,	6,	6,	6,	6,  6,	6,	6,	5,  6)
ivdt14  <-	c(6,	6,	6,	6,	6,	6,	6,	6,	6,  6,	6,	6,	6,  5)


# Translation parameter (gamma) specification
# First alternative is the outside good "Annual non motorized mileage" and therefore gamma = 0 for ivgt1 

ivgt1  <-	c(6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,  6)
ivgt2	<-	c(6,	5,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,  6)
ivgt3	<-	c(6,	6,	5,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,  6)
ivgt4	<-	c(6,	6,	6,	5,	6,	6,	6,	6,	6,	6,	6,	6,	6,  6)
ivgt5	<-	c(6,	6,	6,	6,	5,	6,	6,	6,	6,	6,	6,	6,	6,  6)
ivgt6	<-	c(6,	6,	6,	6,	6,	5,	6,	6,	6,	6,	6,	6,	6,  6)
ivgt7	<-	c(6,	6,	6,	6,	6,	6,	5,	6,	6,	6,	6,	6,	6,  6)
ivgt8	<-	c(6,	6,	6,	6,	6,	6,	6,	5,	6,	6,	6,	6,	6,  6)
ivgt9	<-	c(6,	6,	6,	6,	6,	6,	6,	6,	5,	6,	6,	6,	6,  6)
ivgt10	<-	c(6,	6,	6,	6,	6,	6,	6,	6,	6,	5,	6,	6,	6,  6)
ivgt11	<-	c(6,	6,	6,	6,  6,	6,	6,	6,	6,	6,	5,	6,	6,  6)
ivgt12	<-	c(6,	6,	6,  6,	6,	6,	6,	6,	6,	6,	6,	5,	6,  6)
ivgt13	<-	c(6,	6,  6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	5,  6)
ivgt14  <-	c(6,  6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,	6,  5)


ivm <<- c(ivmt1, ivmt2, ivmt3, ivmt4, ivmt5, ivmt6, ivmt7, ivmt8, ivmt9, ivmt10, ivmt11, ivmt12, ivmt13, ivmt14)
ivd <<- c(ivdt1, ivdt2, ivdt3, ivdt4, ivdt5, ivdt6, ivdt7, ivdt8, ivdt9, ivdt10, ivdt11, ivdt12, ivdt13, ivdt14) 
ivg <<- c(ivgt1, ivgt2, ivgt3, ivgt4, ivgt5, ivgt6, ivgt7, ivgt8, ivgt9, ivgt10, ivgt11, ivgt12, ivgt13, ivgt14) 


nvarm <<- length(ivmt1)     #number of variables in baseline utility   = number of columns in ivm1, do not modify this
nvardel <<- length(ivdt1)   #number of variables in satiation          = number of columns in ivd1, do not modify this
nvargam <<- length(ivgt1)   #number of variables in translation        = number of columns in ivg1, do not modify this


# Associating columns with variable names
flagchm <<- f        
flagavm <<- c(5,  5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,  5) #ivuno~ivuno~ivuno;//Append as many "ivuno" as the number of alternatives
flagprcm <<- fp


#### Do not modify anything below this line #####
hh <<- cbind(matrix(c(rep.int(0,numout)),ncol=numout), matrix(c(rep.int(1,(nc-numout))),ncol=nc-numout))

if (config == 1) {
  eqmatdel <<- diag(nvardel)
  
  temp1 <- NULL
  eqmatgam <- NULL
  
  ind <- 1
  for (ind in 1:numout) {
    temp1 <- matrix(c(rep.int(0,nc)),nrow=1)
    temp1[1,ind] <- 1
    eqmatgam <- rbind(eqmatgam, temp1)
  }
  temp2 <- cbind(matrix(c(rep.int(0,numout)),nrow=1), matrix(c(rep.int(1,(nc-numout))),nrow=1))
  eqmatgam <- rbind(eqmatgam ,temp2)
  
  rm(temp1, temp2)
  b <- matrix(c(c(rep.int(0,nvarm)), c(rep.int(0,nrow(eqmatdel))), -1000*c(rep.int(1,numout)), c(rep.int(0,nrow(eqmatgam)-numout))), ncol=1)
  max_active <- rep.int(c(TRUE,FALSE),c((nvarm+nrow(eqmatdel)),nrow(eqmatgam)))
} 
if (config == 4) {
  eqmatdel <- matrix(c(rep.int(1,nc)),nrow=1)
  eqmatgam <- diag(nvargam)
  if (alp0to1 == 0) {
    b <- matrix(c(c(rep.int(0,nvarm)), c(rep.int(0,nrow(eqmatdel))), -1000*c(rep.int(1,numout)), c(rep.int(0,nrow(eqmatgam)-numout))), ncol=1)
  } else {
    b <- matrix(c(c(rep.int(0,nvarm)), -1000*c(rep.int(1,nrow(eqmatdel))), -1000*c(rep.int(1,numout)), c(rep.int(0,nrow(eqmatgam)-numout))), ncol=1)
  }
  max_active <- rep.int(c(TRUE,FALSE,FALSE,TRUE), c(nvarm,nrow(eqmatdel),numout,(nrow(eqmatgam)-numout)))
}
if (config == 5) {
  eqmatdel <- matrix(c(rep.int(1,nvardel)),nrow=1)
  eqmatgam <- diag(nvargam)
  if (alp0to1 == 0) {
    b <- matrix(c(c(rep.int(0,nvarm)), c(rep.int(0,nrow(eqmatdel))), -1000*c(rep.int(1,numout)), c(rep.int(0,nrow(eqmatgam)-numout))), ncol=1)
  } else {
    b <- matrix(c(c(rep.int(0,nvarm)), -5*c(rep.int(1,nrow(eqmatdel))), -1000*c(rep.int(1,numout)), c(rep.int(0,nrow(eqmatgam)-numout))), ncol=1)
  }
  max_active <- rep.int(c(TRUE,FALSE,TRUE), c((nvarm+nrow(eqmatdel)),numout,(nrow(eqmatgam)-numout)))
}
if (config == 6) {
  
  temp1 <- NULL
  eqmatdel <- NULL
  
  ind <- 1
  for (ind in 1:numout) {
    temp1 <- matrix(c(rep.int(0,nc)),nrow=1)
    temp1[1,ind] <- 1
    eqmatdel <- rbind(eqmatdel, temp1)
  }
  temp2 <- cbind(matrix(c(rep.int(0,numout)),nrow=1), matrix(c(rep.int(1,(nc-numout))),nrow=1))
  
  eqmatdel <- rbind(eqmatdel,temp2)
  eqmatgam <- diag(nc)
  
  rm(temp1, temp2)
  if (alp0to1 == 0) {
    b <- matrix(c(c(rep.int(0,nvarm)), c(rep.int(0,nrow(eqmatdel))), -1000*c(rep.int(1,numout)), c(rep.int(0,nrow(eqmatgam)-numout))), ncol=1)
  } else {
    b <- matrix(c(c(rep.int(0,nvarm)), -5*c(rep.int(1,numout)), -1000*c(rep.int(1,(nrow(eqmatdel)-numout))), -1000*c(rep.int(1,numout)), c(rep.int(0,(nrow(eqmatgam)-numout)))), ncol=1)
  }
  max_active <- rep.int(c(TRUE,TRUE,FALSE,FALSE,TRUE), c(nvarm,numout,(nrow(eqmatdel)-numout),numout,(nrow(eqmatgam)-numout)))
}
if (config == 7) {
  eqmatdel <<- matrix(c(rep.int(1,nc)), nrow=1)
  eqmatgam <<- diag(nc)
  if (alp0to1 == 0) {
    b <- matrix(c(c(rep.int(0,nvarm)), c(rep.int(0,nrow(eqmatdel))), -1000*c(rep.int(1,numout)), c(rep.int(0,nrow(eqmatgam)-numout))), ncol=1)
  } else {
    b <- matrix(c(c(rep.int(0,nvarm)), -1000*c(rep.int(1,nrow(eqmatdel))), -1000*c(rep.int(1,numout)), c(rep.int(0,nrow(eqmatgam)-numout))), ncol=1)
  }
  max_active <- rep.int(c(TRUE,FALSE,FALSE), c(nvarm,nrow(eqmatdel),nrow(eqmatgam)))
}



b <- rbind(b, 1)
if (price == 1){
  max_active <- append(max_active, TRUE, after=length(max_active))
} else {
  max_active <- append(max_active, FALSE, after=length(max_active))
}


lpr <- function(x) {
  
  e1 <- nrow(Data)
  wt <- as.matrix(Data[,wtind])
  popass <- as.matrix(Data[,po])
  
  xdel <- t(eqmatdel)%*%x[(nvarm+1):(nvarm+nrow(eqmatdel)),]
  xgam <- t(eqmatgam)%*%x[(nvarm+nrow(eqmatdel)+1):(nvarm+nrow(eqmatdel)+nrow(eqmatgam)),]
  xsigm <- x[(nvarm+nrow(eqmatdel)+nrow(eqmatgam)+1),]  
  
  a <- matrix(c(rep.int(1,nc)), ncol=1)%x%x[1:nvarm,]
  b <- matrix(c(rep.int(1,nc)), ncol=1)%x%xdel
  c <- matrix(c(rep.int(1,nc)), ncol=1)%x%xgam
  
  v2 <- sweep(t(Data[,ivm]),MARGIN=1,t(a),'*')
  w2 <- sweep(t(Data[,ivd]),MARGIN=1,t(b),'*')
  u2 <- sweep(t(Data[,ivg]),MARGIN=1,t(c),'*')
  rm(a, b, c)
  
  if (xsigm <= 0) {
    xsigm <- 1
  }
  
  j <- 1
  v <- NULL
  w <- NULL
  u <- NULL
  for (j in 1:nc) {
    v <- cbind(v, as.matrix(apply(v2[((j-1)*nvarm+1):(j*nvarm),],2,sum),ncol=1))
    w <- cbind(w, as.matrix(apply(w2[((j-1)*nvardel+1):(j*nvardel),],2,sum),ncol=1))
    u <- cbind(u, as.matrix(apply(u2[((j-1)*nvargam+1):(j*nvargam),],2,sum),ncol=1))
  }
  rm(v2, w2, u2)
  
  
  u[,1:numout] <- -1000*matrix(c(rep.int(1,e1)), ncol=numout)  # How can I create multiple column matrix?
  
  
  a <- exp(w)
  if (alp0to1) {
    a <- 1/(1+exp(w))
  }
  
  
  f <- exp(u)
  b <- ifelse(Data[,flagchm] > 0, 1, 0)
  m <- apply(b,1,sum)
  c <- (a*b)/(Data[,flagchm]+f) 
  c <- c/(Data[,flagprcm])
  c[b==0] <- 1
  e <- (1/c)*b
  
  
  d <- apply(e,1,sum)
  c <- (apply(c,1,prod))*d
  temp1 <- v[,1:numout]-a[,1:numout]*log(Data[,flagchm[1:numout]]+f[,1:numout])-log(Data[,flagprcm[1:numout]])
  temp2 <- v[,(numout+1):nc]-a[,(numout+1):nc]*log((Data[,flagchm[(numout+1):nc]]+f[,(numout+1):nc])/f[,(numout+1):nc])-log(Data[,flagprcm[(numout+1):nc]])
  v <- cbind(temp1,temp2)
  rm(temp1,temp2)
  ut <- v/xsigm
  
  p1 <- exp(ut)
  p2 <- (p1*Data[,flagavm])/(apply((p1*Data[,flagavm]),1,sum))
  p3 <- p2
  p3[b==0] <- 1
  p3 <- (apply(p3,1,prod))*c*(factorial(m-1))
  p3 <- p3/(xsigm^(m-1))
  z <- as.matrix(p3)
  w1 <- matrix(c(rep.int(0,e1)),ncol=1)
  
  z1 <- z
  z1 <- ifelse(z>0,log(z),log(z-(z-0.0001)))
  
  return(wt*z1)
}


lgd <- function(x) {
  
  e1 <- nrow(Data)
  wt <- as.matrix(Data[,wtind])
  popass <- as.matrix(Data[,po])
  p0 <- matrix(c(rep.int(0,e1)),ncol=1)
  
  xdel <- t(eqmatdel)%*%x[(nvarm+1):(nvarm+nrow(eqmatdel)),]
  xgam <- t(eqmatgam)%*%x[(nvarm+nrow(eqmatdel)+1):(nvarm+nrow(eqmatdel)+nrow(eqmatgam)),]
  xsigm <- x[(nvarm+nrow(eqmatdel)+nrow(eqmatgam)+1),]
  
  a <- matrix(c(rep.int(1,nc)), ncol=1)%x%x[1:nvarm,]
  b <- matrix(c(rep.int(1,nc)), ncol=1)%x%xdel
  c <- matrix(c(rep.int(1,nc)), ncol=1)%x%xgam
  
  v2 <- sweep(t(Data[,ivm]),MARGIN=1,t(a),'*')
  w2 <- sweep(t(Data[,ivd]),MARGIN=1,t(b),'*')
  u2 <- sweep(t(Data[,ivg]),MARGIN=1,t(c),'*')
  rm(a, b, c)
  
  
  if (xsigm <= 0) {
    xsigm <- 1
  }
  
  j <- 1
  v <- NULL
  w <- NULL
  u <- NULL
  for (j in 1:nc) {
    v <- cbind(v, apply(v2[((j-1)*nvarm+1):(j*nvarm),],2,sum))
    w <- cbind(w, apply(w2[((j-1)*nvardel+1):(j*nvardel),],2,sum))
    u <- cbind(u, apply(u2[((j-1)*nvargam+1):(j*nvargam),],2,sum))
  }
  rm(v2, w2, u2)
  
  u[,1:numout] <- -1000*matrix(c(rep.int(1,e1)), ncol=numout)  
  
  
  a <- exp(w)
  if (alp0to1) {
    a <- 1/(1+exp(w))
  }
  
  f <- exp(u)
  b <- ifelse(Data[,flagchm] > 0, 1, 0)
  m <- apply(b,1,sum)
  c <- (a*b)/(Data[,flagchm]+f)
  c <- c/(Data[,flagprcm])
  c[b==0] <- 1
  e <- (1/c)*b
  d <- apply(e,1,sum)
  c <- (apply(c,1,prod))*d
  temp1 <- v[,1:numout]-a[,1:numout]*log(Data[,flagchm[1:numout]]+f[,1:numout])-log(Data[,flagprcm[1:numout]])
  temp2 <- v[,(numout+1):nc]-a[,(numout+1):nc]*log((Data[,flagchm[(numout+1):nc]]+f[,(numout+1):nc])/f[,(numout+1):nc])-log(Data[,flagprcm[(numout+1):nc]])
  v <- cbind(temp1,temp2)
  rm(temp1,temp2)
  ut <- v/xsigm
  uts <- as.matrix(-ut/xsigm)
  
  p1 <- exp(ut)
  p2 <- (p1*Data[,flagavm])/(apply((p1*Data[,flagavm]),1,sum))
  p3 <- p2
  p3[b==0] <- 1
  p3 <- (apply(p3,1,prod))*c*(factorial(m-1))
  p3 <- p3/(xsigm^(m-1))
  
  g1 <- (matrix(c(rep.int(1,e1)),ncol=1))%x%(diag(nc)) - (as.matrix(p2)%x%(matrix(c(rep.int(1,nc)),ncol=1)))
  g1 <- g1*c(apply(b,1,cbind))
  g1s <- g1*(uts%x%(matrix(c(rep.int(1,nc)),ncol=1)))
  j <- 1
  g2 <- NULL
  g2s <- NULL
  while (j <= e1) {
    g2 <- cbind(g2, apply(g1[((j-1)*nc+1):(j*nc),],2,sum))
    g2s <- cbind(g2s, apply(g1s[((j-1)*nc+1):(j*nc),],2,sum))
    j <- j+1
  }
  rm(g1)
  h <- Data[,flagchm]+f
  g2 <- (1/xsigm)*(t(g2))*p3
  f1 <- sweep((sweep(f,MARGIN=2,hh,'*')),MARGIN=2,(1-hh),'+')
  g2s <- as.matrix((apply(g2s,2,sum) - ((m-1)/xsigm)))
  g2d <- NULL
  if (alp0to1 == 0) { 
    g2d <- as.matrix(g2*(((log(h/f1))*(-a)))+p3*b+p3*(e/d)*(-1))
  } else { 
    g2d <- as.matrix(g2*(((log(h/f1))*(a*(1-a))))+p3*(a-1)*b+p3*(e/d)*(1-a))
  }
  g2g <- as.matrix((g2*(-a)*(1/h)*(-1/f1)*Data[,flagchm]+p3*(-1/h)*b+p3*(e/d)*(1/h))*f)
  g2v <- (matrix(c(rep.int(1,nvarm)),nrow=1))%x%t(g2)
  g2d <- (matrix(c(rep.int(1,nvardel)),nrow=1))%x%t(g2d)
  g2g <- (matrix(c(rep.int(1,nvargam)),nrow=1))%x%t(g2g)
  ylargev <- as.matrix(Data[,ivm])
  gv <- t(matrix(apply(g2v*(matrix(as.vector(ylargev),nc,(e1*nvarm),byrow=TRUE)),2,sum),nvarm,e1,byrow=TRUE))
  ylargev <- as.matrix(Data[,ivd])
  gd <- t(matrix(apply(g2d*(matrix(as.vector(ylargev),nc,(e1*nvardel),byrow=TRUE)),2,sum),nvardel,e1,byrow=TRUE))
  ylargev <- as.matrix(Data[,ivg])
  gg <- t(matrix(apply(g2g*(matrix(as.vector(ylargev),nc,(e1*nvargam),byrow=TRUE)),2,sum),nvargam,e1,byrow=TRUE))
  rm(ylargev)
  
  return(sweep(cbind((cbind(gv, gd%*%t(eqmatdel), gg%*%t(eqmatgam)))/p3,g2s),MARGIN=1,wt,'*'))
}


lpr1 <- function(x) {
  
  e1 <- nrow(Data)
  wt <- as.matrix(Data[,wtind])
  popass <- as.matrix(Data[,po])
  
  xdel <- t(eqmatdel)%*%x[(nvarm+1):(nvarm+nrow(eqmatdel)),]
  xgam <- t(eqmatgam)%*%x[(nvarm+nrow(eqmatdel)+1):(nvarm+nrow(eqmatdel)+nrow(eqmatgam)),]
  xsigm <- x[(nvarm+nrow(eqmatdel)+nrow(eqmatgam)+1),]
  
  a <- matrix(c(rep.int(1,nc)), ncol=1)%x%x[1:nvarm,]
  b <- matrix(c(rep.int(1,nc)), ncol=1)%x%xdel
  c <- matrix(c(rep.int(1,nc)), ncol=1)%x%xgam
  
  v2 <- sweep(t(Data[,ivm]),MARGIN=1,t(a),'*')
  w2 <- sweep(t(Data[,ivd]),MARGIN=1,t(b),'*')
  u2 <- sweep(t(Data[,ivg]),MARGIN=1,t(c),'*')
  rm(a, b, c)
  
  if (xsigm <= 0) {
    xsigm <- 1
  }
  
  j <- 1
  v <- NULL
  w <- NULL
  u <- NULL
  for (j in 1:nc) {
    v <- cbind(v, as.matrix(apply(v2[((j-1)*nvarm+1):(j*nvarm),],2,sum),ncol=1))
    w <- cbind(w, as.matrix(apply(w2[((j-1)*nvardel+1):(j*nvardel),],2,sum),ncol=1))
    u <- cbind(u, as.matrix(apply(u2[((j-1)*nvargam+1):(j*nvargam),],2,sum),ncol=1))
  }
  rm(v2, w2, u2)
  
  a <- 1-w
  f <- u
  b <- ifelse(Data[,flagchm] > 0, 1, 0)
  m <- apply(b,1,sum)
  c <- (a*b)/(Data[,flagchm]+f)
  c <- c/(Data[,flagprcm])
  c[b==0] <- 1
  e <- (1/c)*b
  d <- apply(e,1,sum)
  c <- (apply(c,1,prod))*d
  temp1 <- v[,1:numout]-a[,1:numout]*log(Data[,flagchm[1:numout]]+f[,1:numout])-log(Data[,flagprcm[1:numout]])
  temp2 <- v[,(numout+1):nc]-a[,(numout+1):nc]*log((Data[,flagchm[(numout+1):nc]]+f[,(numout+1):nc])/f[,(numout+1):nc])-log(Data[,flagprcm[(numout+1):nc]])
  v <- cbind(temp1,temp2)
  rm(temp1,temp2)
  ut <- v/xsigm
  
  p1 <- exp(ut)
  p2 <- (p1*Data[,flagavm])/(apply((p1*Data[,flagavm]),1,sum))
  p3 <- p2
  p3[b==0] <- 1
  p3 <- (apply(p3,1,prod))*c*(factorial(m-1))
  p3 <- p3/(xsigm^(m-1))
  z <- as.matrix(p3)
  w1 <- matrix(c(rep.int(0,e1)),ncol=1)
  
  z1 <- z
  z1 <- ifelse(z>0,log(z),log(z-(z-0.0001)))
  
  return(wt*z1)
}


ptm <- proc.time();
temp <- maxLik(lpr,lgd,start=b,method="BHHH",fixed=!max_active);
summary(temp);

k <- coef(temp);
if (alp0to1 == 0){
  k[(nvarm+1):(nvarm+nrow(eqmatdel)),] <- 1-exp(k[(nvarm+1):(nvarm+nrow(eqmatdel)),])
  k[(nvarm+nrow(eqmatdel)+1):(nvarm+nrow(eqmatdel)+nrow(eqmatgam)),] <- exp(k[(nvarm+nrow(eqmatdel)+1):(nvarm+nrow(eqmatdel)+nrow(eqmatgam)),])
} else {
  k[(nvarm+1):(nvarm+nrow(eqmatdel)),] <- 1/(1+exp(-k[(nvarm+1):(nvarm+nrow(eqmatdel)),]))
  k[(nvarm+nrow(eqmatdel)+1):(nvarm+nrow(eqmatdel)+nrow(eqmatgam)),] <- exp(k[(nvarm+nrow(eqmatdel)+1):(nvarm+nrow(eqmatdel)+nrow(eqmatgam)),])
}

temp1 <- maxLik(lpr1,start=k,method="BFGS",fixed=!max_active,iterlim=0,finalHessian="BHHH");
summary(temp1);
print(proc.time() - ptm);
####################################################### End of code ###################################################################################