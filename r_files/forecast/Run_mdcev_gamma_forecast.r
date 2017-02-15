
source("D:/R_Package_Estimation/MDCEV_NoOutside_Forecasting/mdcev_gamma_forecast.r");

Data <<- read.table("D:/R_Package_Estimation/MDCEV_NoOutside_Forecasting/testnout.csv", header=T, sep=",");
output <- "D:/R_Package_Estimation/MDCEV_NoOutside_Forecasting/testnout_gamma.csv";

# path for the dataset that draws pesudo random Halton draws to generate the gumbel error terms
# If you do not have the matrix, you can comment out this line and write code to generate random numbers on the fly
# alternatively, you can uncomment this line and set _gumbel = 0 to avoid considering the unobserved heterogeneity
Halton_File <<- "D:/R_Package_Estimation/Halton/halton_class15.csv";

ivuno <- "uno";         # Column of ones
ivsero <- "sero";       # Column of zeros

numout <- 0;      # Number of outside goods (i.e., always consumed goods)
config <- 4;      # Utility specification configuration, possible values: 4, 7
alp0to1 <<- 1;    # 1 if you want the Alpha values to be constrained between 0 and 1, 0 otherwise
price <- 0;       # 1 if there is price variation across goods, 0 otherwise
nc <<- 3;         # Number of alternatives (in the universal choice set) including outside goods
po <<- 1;         # position of pointer to case number in data set,

nrep <- 1;        # Number of sets of error term Halton draws overwhich you want to simulate the unobserved heterogeneity

# 1 if Gumbel error terms are used to simulate the unobserved heterogeneity (i.e., the error terms), 
# 0 if no error terms are used for forecasting.
# if _gumbel = 0, then set nrep = 1.
gumbel <- 1;
halton_startrow <- 22; # Number of row in dataset of pesudo random halton. It will read halton data from the row number

tolel <- 0.00000001;
tolee <- 0.01;
avg <- 0;



# Provide labels of dependent variables (i.e., the expenditure variables) below
def <- c("consume1","consume2","consume3");

# Provide labels of price variables below; if no price variables, introduce UNO as the variable
fp <- c(ivuno, ivuno, ivuno); #, ivuno, ivuno, ivuno, ivuno, ivuno, ivuno, ivuno, ivuno, ivuno, ivuno, ivuno, ivuno);


# definition of independent variables 
# ivm[[1]] has variables that influence baseline preference parameter psi, ivd[[1]] has variables that influence the satiation parameter delta, 
# and ivg[[1]] has variabels that influence the translation parameter gamma; 
ivmt <- list();
ivmtc <- list();

ivmt[[1]] <- c("");     # Do not modify this line because the first alternative is considered as base     
ivmtc[[1]] <- c(0.0);   # Do not modify this line because the first alternative is considered as base
ivmt[[2]] <- c("uno","hhsize");
ivmtc[[2]] <- c(0.319,-0.03);
ivmt[[3]] <- c("uno","hhsize");
ivmtc[[3]] <- c(-0.748,-0.025);


# Important Note: For the satiation parameters (alphas and gammas) do not provide the final values of alphas and gammas. 
# Provide the values of the parameters that are actually estimated in the model. 
# For example, gamma is parameterized as exp(theeta), and theeta is estimated. So provide the theeta values here.
# Simialrly, Alpha is parameterized as 1-(1/exp(delta)). Provide the delta values here.
ivdts <- list();

ivdts[[1]] <- c("uno");
ivdts[[2]] <- c("uno");
ivdts[[3]] <- c("uno");


# The alpha values for all alternatives are restricted to -1000.
ivdtc <- c(-1000.0); 

   
ivgts <- list();
ivgtc <- list();

ivgts[[1]] <- c("uno");
ivgtc[[1]] <- c(6.4885);
ivgts[[2]] <- c("uno");
ivgtc[[2]] <- c(5.9695);
ivgts[[3]] <- c("uno");
ivgtc[[3]] <- c(5.4557);




########################################################################################################
#  Do Not Modify Next Three Lines
########################################################################################################
arg_inds <- list(numout, config, alp0to1, price, nc, po, ivuno, ivsero, nrep, gumbel, halton_startrow, tolel, tolee, avg);
arg_vars <- list(Halton_File, output);
result <- gamma_forecast(Data, arg_inds, arg_vars, def, fp, ivmt, ivdts, ivgts, ivmtc, ivdtc, ivgtc);
########################################################################################################