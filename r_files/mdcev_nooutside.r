# Goal: To read in a simple data file, and look around it's contents.

# Suppose you have a file "x.data" which looks like this:
#        1997,3.1,4
#        1998,7.2,19
#        1999,1.7,2
#        2000,1.1,13
# To read it in --

library(miscTools)
library(maxLik)

list_creator <- function(parameter_list) {
  list = c()
  for (item in parameter_list) {
    list = c(list, item)
  }
  return(list)
}


fp_ind <- function(ind, nc) {
  
  tmp <- c(ind);
  i <- 1;
  while (i <= (nc-1)) {
    tmp <- c(tmp, ind);
    i <- i+1;
  }
  
  #print(tmp);
  return (tmp);
  
}


parameter_ind <- function(ivgt, ind, nc, sero, ncoeffs) {
  
  i <- 1;
  while (i <= nc) {
    j <- 1;
    while (j <= ncoeffs[i]) {
      if (i > ind) {
        ivgt <- c(ivgt, sero);
      }
      if (i < ind) {
        ivgt <- c(sero, ivgt);
      }
      j <- j+1;
    }
    i <- i+1;
  }
  
  return (ivgt);
}



mdcev_nooutgood <- function(Data, arg_inds, arg_vars, dep, fp1, ivmts, ivdts, ivgts, Alpha_Names, Gamma_Names) {

  #row <- 100               #Number of rows to be read at a time by the log-likelihood function
  #nobs <- 1000             #Number of observations in the dataset
  config <- arg_inds[[1]];   #1      #Utility specification configuration, possible values: 1,4,5,6,7
  alp0to1 <<- arg_inds[[2]]; #1    #1 if you want the Alpha values to be constrained between 0 and 1, 0 otherwise
  #putting _alp0to1 = 1 is recommended practice and can provide estimation stability
  price <- arg_inds[[3]];    #0       #1 if there is price variation across goods, 0 otherwise
  nc <<- arg_inds[[4]];      #7                 #Number of alternatives (in the universal choice set) including outside goods
  po <<- arg_inds[[5]];      #4
  
  ivuno <- arg_vars[[1]];    #"uno"
  ivsero <- arg_vars[[2]];   #"sero"
  wtind <<- arg_vars[[3]];   #"uno"
  
  
  f  <- def;  #f <- c("PerBus","Shopping","Social","Recreate","Meal","Serve","Other");
  fp <- fp1;  #fp_ind(ivuno,nc);
  
  
  #### Baseline utility equation
  ivmt <- ivmts;
  
  ncoeffs <- NULL; #c(length(ivmt[[1]]));
  for(i in 2:nc){  # (nc-1)
    ncoeffs <- c(ncoeffs, length(ivmt[[i]]));
  }
 
  tmp1 <- c(ivsero);
  for(j in 2:sum(ncoeffs)){
    tmp1 <- c(tmp1,ivsero);
  }
  ivmt[[1]] <- tmp1;
  
  
  for(i in 2:nc){
    ivmt[[i]] <- parameter_ind(ivmt[[i]], (i-1), (nc-1), ivsero, ncoeffs);
  }

  
  Parameter_names <- NULL;
  if (config == 1) {
    Parameter_names <- c(Alpha_Names,Gamma_Names[1],"sigm");
  }
  else {
    Parameter_names <- c(Alpha_Names[1],Gamma_Names,"sigm");
  }
  
  Variable_names <- NULL;
  for(i in 2:(length(ivmts))) {
    Variable_names <- c(Variable_names, ivmts[[i]]); 
  }
  
  Variable_names <- c(Variable_names,Parameter_names);
  print("Running MDCEV with no outside good...");
  print(Variable_names);
  
  
  

  ncoeffs <- NULL; #c(length(ivdts[[1]]));
  for(i in 1:nc){
    ncoeffs <- c(ncoeffs, length(ivdts[[i]]));
  }
  
  ivdt <- list();
  for (i in 1:nc){
    ivdt1 <- ivdts[[i]];   #c(ivuno);
    ivdt[[i]] <- parameter_ind(ivdt1, i, nc, ivsero, ncoeffs);
  }

  
  ncoeffs <- NULL; #c(length(ivdts[[1]]));
  for(i in 1:nc){
    ncoeffs <- c(ncoeffs, length(ivgts[[i]]));
  }
  
  ivgt <- list();
  for (i in 1:nc){
    ivgt1 <- ivgts[[i]];   #c(ivuno);
    ivgt[[i]] <- parameter_ind(ivgt1, i, nc, ivsero, ncoeffs);
  }


  ivm <<- c(ivmt[[1]]);
  for (i in 2:(length(ivmt))){
    ivm <<- c(ivm, ivmt[[i]]);
  }
  

  ivd <<- c(ivdt[[1]]);
  for (i in 2:(length(ivdt))){
    ivd <<- c(ivd, ivdt[[i]]);
  }
  
  ivg <<- c(ivgt[[1]]);
  for (i in 2:(length(ivgt))){
    ivg <<- c(ivg, ivgt[[i]]);
  }
  
  
  
  nvarm <<- length(ivmt[[1]])  #number of variables in baseline utility   = number of columns in ivm1, do not modify this
  nvardel <<- length(ivdt[[1]]) #number of variables in satiation          = number of columns in ivd1, do not modify this
  nvargam <<- length(ivgt[[1]]) #number of variables in translation        = number of columns in ivg1, do not modify this
  
  
  #Associating columns with variable names
  
  flagchm <<- f        
  #flagavm <<- c("uno","uno","uno","uno","uno","uno","uno")  #ivuno~ivuno~ivuno;//Append as many "ivuno" as the number of alternatives
  flagavm <<- fp_ind(ivuno,nc);
  flagprcm <<- fp
  
  
  #Do not modify the line below####################### 
  
  if (config == 1) {
    eqmatdel <<- diag(nvardel)
    eqmatgam <<- matrix(c(rep(1,nc)),nrow=1)
    b <- matrix(c(c(rep(0,nvarm)), c(rep(0,nrow(eqmatdel))), c(rep(0,nrow(eqmatgam)))), ncol=1)
    max_active <- rep(c(TRUE,FALSE),c((nvarm+nrow(eqmatdel)),nrow(eqmatgam)))
  } 
  if (config == 4) {
    eqmatdel <- matrix(c(rep(1,nc)),nrow=1)
    eqmatgam <- diag(nvargam)
    b <- matrix(c(c(rep(0,nvarm)), -1000*c(rep(1,nrow(eqmatdel))), c(rep(0,nrow(eqmatgam)))), ncol=1)
    max_active <- rep(c(TRUE,FALSE,TRUE),c(nvarm,nrow(eqmatdel),nrow(eqmatgam)))
  }
  if (config == 7) {
    eqmatdel <<- matrix(c(rep(1,nc)), nrow=1)
    eqmatgam <<- diag(nc)
    b <- matrix(c(c(rep(0,nvarm)), -1000*c(rep(1,nrow(eqmatdel))), c(rep(0,nrow(eqmatgam)))), ncol=1)
    max_active <- rep(c(TRUE,FALSE,FALSE), c(nvarm,nrow(eqmatdel),nrow(eqmatgam)))
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
    xsigm <- x[(nvarm+nrow(eqmatdel)+nrow(eqmatgam)+1),];
    
    a <- matrix(c(rep(1,nc)), ncol=1)%x%x[1:nvarm,]
    b <- matrix(c(rep(1,nc)), ncol=1)%x%xdel
    c <- matrix(c(rep(1,nc)), ncol=1)%x%xgam
    
    
    v2 <- sweep(Data[,ivm],MARGIN=2,t(a),'*')
    w2 <- sweep(Data[,ivd],MARGIN=2,t(b),'*')
    u2 <- sweep(Data[,ivg],MARGIN=2,t(c),'*')
    rm(a, b, c)
    
    #print(v2)
    
    if (xsigm <= 0) {
      xsigm <- 1
    }
    
    j <- 1
    v <- NULL
    w <- NULL
    u <- NULL
    for (j in 1:nc) {
      v <- cbind(v, as.matrix(apply(v2[,((j-1)*nvarm+1):(j*nvarm)],1,sum),ncol=1))
      w <- cbind(w, as.matrix(apply(w2[,((j-1)*nvardel+1):(j*nvardel)],1,sum),ncol=1))
      u <- cbind(u, as.matrix(apply(u2[,((j-1)*nvargam+1):(j*nvargam)],1,sum),ncol=1))
    }
    rm(v2, w2)
    
    
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
    v <- v - a*log((Data[,flagchm]+f)/f)-log(Data[,flagprcm])
    ut <- v/xsigm
    
    p1 <- exp(ut)
    p2 <- (p1*Data[,flagavm])/(apply((p1*Data[,flagavm]),1,sum))
    p3 <- p2
    p3[b==0] <- 1
    p3 <- (as.matrix(apply(p3,1,prod)))*c*(factorial(m-1))
    p3 <- p3/(xsigm^(m-1))
    z <- as.matrix(p3)
    w1 <- matrix(c(rep(0,e1)),ncol=1)
    
    z1 <- z
    z1 <- ifelse(z>0,log(z),log(z-(z-0.0001)))
    
    return(wt*z1);
  }
  
  
  lgd <- function(x) {
    
    e1 <- nrow(Data)
    wt <- as.matrix(Data[,wtind])
    popass <- as.matrix(Data[,po])
    p0 <- matrix(c(rep(0,e1)),ncol=1)
    
    xdel <- t(eqmatdel)%*%x[(nvarm+1):(nvarm+nrow(eqmatdel)),]
    xgam <- t(eqmatgam)%*%x[(nvarm+nrow(eqmatdel)+1):(nvarm+nrow(eqmatdel)+nrow(eqmatgam)),]
    xsigm <- x[(nvarm+nrow(eqmatdel)+nrow(eqmatgam)+1),];
    
    a <- matrix(c(rep(1,nc)), ncol=1)%x%x[1:nvarm,]
    b <- matrix(c(rep(1,nc)), ncol=1)%x%xdel
    c <- matrix(c(rep(1,nc)), ncol=1)%x%xgam
    
    
    v2 <- sweep(Data[,ivm],MARGIN=2,t(a),'*')
    w2 <- sweep(Data[,ivd],MARGIN=2,t(b),'*')
    u2 <- sweep(Data[,ivg],MARGIN=2,t(c),'*')
    rm(a, b, c)
    
    
    if (xsigm <= 0) {
      xsigm <- 1
    }
    
    j <- 1
    v <- NULL
    w <- NULL
    u <- NULL
    for (j in 1:nc) {
      v <- cbind(v, as.matrix(apply(v2[,((j-1)*nvarm+1):(j*nvarm)],1,sum),ncol=1))
      w <- cbind(w, as.matrix(apply(w2[,((j-1)*nvardel+1):(j*nvardel)],1,sum),ncol=1))
      u <- cbind(u, as.matrix(apply(u2[,((j-1)*nvargam+1):(j*nvargam)],1,sum),ncol=1))
    }
    rm(v2, w2)
    
    
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
    v <- v - a*log((Data[,flagchm]+f)/f)-log(Data[,flagprcm])
    ut <- v/xsigm
    uts <- as.matrix(-ut/xsigm)
    
    p1 <- exp(ut)
    p2 <- (p1*Data[,flagavm])/(apply((p1*Data[,flagavm]),1,sum))
    p3 <- p2
    p3[b==0] <- 1
    p3 <- (apply(p3,1,prod))*c*(factorial(m-1))
    p3 <- p3/(xsigm^(m-1))
    #z <- as.matrix(p3)
    #w1 <- matrix(c(rep(0,e1)),ncol=1)
    #z1 <- z
    #z1 <- ifelse(z>0,log(z),log(z-(z-0.0001)))
    
    g1 <- (matrix(c(rep(1,e1)),ncol=1))%x%(diag(nc)) - (as.matrix(p2)%x%(matrix(c(rep(1,nc)),ncol=1)))
    g1 <- g1*c(apply(b,1,cbind))
    g1s <- g1*(uts%x%(matrix(c(rep(1,nc)),ncol=1)))
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
    #f1 <- sweep((sweep(f,MARGIN=2,hh,'*')),MARGIN=2,(1-hh),'+')
    g2s <- as.matrix((apply(g2s,2,sum) - ((m-1)/xsigm)))
    g2d <- NULL
    if (alp0to1 == 0) { 
      g2d <- as.matrix(g2*(((log(h/f))*(-a)))+p3*b+p3*(e/d)*(-1))
    } else { 
      g2d <- as.matrix(g2*(((log(h/f))*(a*(1-a))))+p3*(a-1)*b+p3*(e/d)*(1-a))
    }
    g2g <- as.matrix((g2*(-a)*(1/h)*(-1/f)*Data[,flagchm]+p3*(-1/h)*b+p3*(e/d)*(1/h))*f)
    g2v <- (matrix(c(rep(1,nvarm)),nrow=1))%x%t(g2)
    g2d <- (matrix(c(rep(1,nvardel)),nrow=1))%x%t(g2d)
    g2g <- (matrix(c(rep(1,nvargam)),nrow=1))%x%t(g2g)
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
    xsigm <- x[(nvarm+nrow(eqmatdel)+nrow(eqmatgam)+1),];
    
    a <- matrix(c(rep(1,nc)), ncol=1)%x%x[1:nvarm,]
    b <- matrix(c(rep(1,nc)), ncol=1)%x%xdel
    c <- matrix(c(rep(1,nc)), ncol=1)%x%xgam
    
    v2 <- sweep(Data[,ivm],MARGIN=2,t(a),'*')
    w2 <- sweep(Data[,ivd],MARGIN=2,t(b),'*')
    u2 <- sweep(Data[,ivg],MARGIN=2,t(c),'*')
    rm(a, b, c)
    
    if (xsigm <= 0) {
      xsigm <- 1
    }
    
    j <- 1
    v <- NULL
    w <- NULL
    u <- NULL
    for (j in 1:nc) {
      v <- cbind(v, as.matrix(apply(v2[,((j-1)*nvarm+1):(j*nvarm)],1,sum),ncol=1))
      w <- cbind(w, as.matrix(apply(w2[,((j-1)*nvardel+1):(j*nvardel)],1,sum),ncol=1))
      u <- cbind(u, as.matrix(apply(u2[,((j-1)*nvargam+1):(j*nvargam)],1,sum),ncol=1))
    }
    rm(v2, w2)
    
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
    v <- v - a*log((Data[,flagchm]+f)/f)-log(Data[,flagprcm])
    ut <- v/xsigm
    p1 <- exp(ut)
    p2 <- (p1*Data[,flagavm])/(apply((p1*Data[,flagavm]),1,sum))
    p3 <- p2
    p3[b==0] <- 1
    p3 <- (apply(p3,1,prod))*c*(factorial(m-1))
    p3 <- p3/(xsigm^(m-1))
    z <- as.matrix(p3)
    w1 <- matrix(c(rep(0,e1)),ncol=1)
    
    
    z1 <- z
    z1 <- ifelse(z>0,log(z),log(z-(z-0.0001)))
    
    return(wt*z1);
  }
  print("#############   This is b")
  print(b)
  
  ptm <- proc.time()
  temp <- maxLik(lpr,lgd,start=b,method=arg_vars[[4]],fixed=!max_active)
  k <- coef(temp)
  print("################ This is first K ")
  print(k)
  
  if (alp0to1 == 0){
    k[(nvarm+1):(nvarm+nrow(eqmatdel)),] <- 1-exp(k[(nvarm+1):(nvarm+nrow(eqmatdel)),])
    k[(nvarm+nrow(eqmatdel)+1):(nvarm+nrow(eqmatdel)+nrow(eqmatgam)),] <- exp(k[(nvarm+nrow(eqmatdel)+1):(nvarm+nrow(eqmatdel)+nrow(eqmatgam)),])
  } else {
    k[(nvarm+1):(nvarm+nrow(eqmatdel)),] <- 1/(1+exp(-k[(nvarm+1):(nvarm+nrow(eqmatdel)),]))
    k[(nvarm+nrow(eqmatdel)+1):(nvarm+nrow(eqmatdel)+nrow(eqmatgam)),] <- exp(k[(nvarm+nrow(eqmatdel)+1):(nvarm+nrow(eqmatdel)+nrow(eqmatgam)),])
  }
  
  print(!max_active)
  
  temp1 <- maxLik(lpr1,start=k,method=arg_vars[[5]],fixed=!max_active,iterlim=0,finalHessian="BHHH")
  
  row.names(temp1$estimate) <- Variable_names;
  
  #summary(temp1)
  #print(proc.time() - ptm)
  
  return(temp1);
}









