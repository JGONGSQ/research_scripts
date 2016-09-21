args <- commandArgs(trailingOnly = TRUE)


if (length(args)==0) {
  stop("At least one argument must be supplied", call.=FALSE)
}


input_file_path = args[1]
number_of_alternatives = args[2]
case_config = args[3]

source("r_files/mdcev_nooutside.r");

Data <<- read.table(input_file_path, header=T, sep=",");

table_headers = names(Data)

config <- case_config;     # Utility specification configuration, possible values: 1,4,7
alp0to1 <- 1;    # 1 if you want the Alpha values to be constrained between 0 and 1, 0 otherwise
                 # putting _alp0to1 = 1 is recommended practice and can provide estimation stability
price <- 0;      # 1 if there is price variation across goods, 0 otherwise
nc <- number_of_alternatives;         # Number of alternatives (in the universal choice set) including outside goods
po <- match("id", table_headers, 0);         # Index number of ID column in input data

ivuno <- match("uno", table_headers, 0);  # Position of UNO variable (i.e., the column of ones) in data set
ivsero <- match("sero", table_headers, 0);# Position of SERO variable (i.e., the column of zeros) in data set
wtind <<- match("uno", table_headers, 0); # Position of WEIGHT variable (i.e., the column of weights) in data set

if (po == 0 || ivuno ==0 || ivsero == 0 ){
  stop("One of the po, ivuno or ivsero is 0, please check your data", call.=FALSE)
}

maxlikmethod1 <- "BHHH"; # Method of maximum likelihood for initial estimation ("BHHH" or "BFGS") 
maxlikmethod2 <- "BFGS"; # Method of maximum likelihood for final estimation ("BHHH" or "BFGS") 

# Position of the DEPENDENT variables (i.e., the consumption quantities for each alternative - NOT consumption expenditures for each alternative).
# Number of labels = number of alternatives. 
def <- c("consume1","consume2","consume3");


# Positions of PRICE variables
# Provide labels of price variables (one label in each double-quote). Number of labels = number of alternatives.
# Provide all UNO variables if there is no price variation 
fp <- c(ivuno, ivuno, ivuno);

# In the following specification, ivm1, ivm2, ivm3 contain independent variable specifications (on right hand side) for baseline utility (PSI) 
# for alternatives 1, 2, and 3;
# Add a row for ivm4 below if there is a 4th alternative, another addiitonal row for ivm5 if there is a 5th alternative, ...  
# (number of rows = number of alternatives);
# Number of columns = Number of variables including alternative specific constants; consider first alternative as base
ivmt <- list();
ivmt[[1]] <- c("");   # Base alternative
ivmt[[2]] <- c("uno","hhsize");
ivmt[[3]] <- c("uno","hhsize");


# In the following specification, ivdts[[1]], ivdts[[2]], ivdts[[3]] contain input data specifications (on right hand side) for satiation parameters (Alphas) 
# for alternatives 1, 2, and 3;
# Add a row below for ivd4 if there is a 4th alternative, another additional row for ivd5 if there is a 5th alternative,.... 
# (number of rows = number of alternatives);
# Number of columns = Number of alternatives; Note that you can also add individual-specific variables below, so that satiation varies across individuals; 
# However, you will then have to translate outputs to compute actual alpha parameters; 
# This code is written to provide you with the alpha parameters directly for the case when there is no variation in alpha across individuals 
ivdts <- list();
ivdts[[1]] <- c("uno");
ivdts[[2]] <- c("uno");
ivdts[[3]] <- c("uno");


# In the following specification, ivgts[[1]], ivgts[[2]], ivgts[[3]] contain input data specifications (on the right hand side) for translation parameters (Gammas) 
# for alternatives 1, 2, and 3
# Add a row for ivgts[[4]] if there is a 4th alternative another additional row for ivgts[[5]] if there is a 5th alternative,.... 
# (number of rows = number of alternatives) Number of columns = Number of alternatives; 
# Note that you can also add individual-specific variables below, so that gamma varies across individuals; 
# However, you will then have to translate outputs to compute actual gamma parameters; 
# This code is written to provide you with the gamma parameters directly for the case when there is no variation in gamma across individuals 
ivgts <- list();
ivgts[[1]] <- c("uno");
ivgts[[2]] <- c("uno");
ivgts[[3]] <- c("uno");


# Add variable names for translation and satiation variables
# The number of names for both translation and satiation should be equal to the number of alternatives
alpha_names <- c("D01","D02","D03");
gamma_names <- c("G01","G02","G03");

########################################################################################################
#  Do Not Modify Next Three Lines
########################################################################################################
arg_inds <- list(config, alp0to1, price, nc, po); 
arg_vars <- list(ivuno, ivsero, wtind, maxlikmethod1, maxlikmethod2);           
result <- mdcev_nooutgood(Data, arg_inds, arg_vars, def, fp, ivmt, ivdts, ivgts, alpha_names, gamma_names);
########################################################################################################

summary(result); # Show results from the MDCEV model with no outside good

