print("------> Start forecasting process <-----")
source("r_files/forecast/mdcev_alpha_forecast.r");
args <- commandArgs(trailingOnly = TRUE)

if (length(args)==0){
    stop("At least one argument must be supplied", call.=FALSE)
}
data_filepath = args[1]
number_of_alternatives = strtoi(args[2])
case_config = strtoi(args[3])
alternative_variables = args[4]
output_filepath = args[5]
halton_filepath = args[6]
coef_filepath = args[7]

coef_data <<- read.table(coef_filepath, header=T, sep=",");
print(">>>> Coef Data <<<<")

alternative_variables_2 <- list_creator(strsplit(toString(coef_data[1,"variables"]), ","))
alternative_variables_3 <- list_creator(strsplit(toString(coef_data[2,"variables"]), ","))
alternative_variables_4 <- list_creator(strsplit(toString(coef_data[3,"variables"]), ","))
alternative_variables_5 <- list_creator(strsplit(toString(coef_data[4,"variables"]), ","))
alternative_variables_6 <- list_creator(strsplit(toString(coef_data[5,"variables"]), ","))
# print(temp_variable)

alternative_values_2 <- float_list_creator(strsplit(toString(coef_data[1,"values"]), ","))
alternative_values_3 <- float_list_creator(strsplit(toString(coef_data[2,"values"]), ","))
alternative_values_4 <- float_list_creator(strsplit(toString(coef_data[3,"values"]), ","))
alternative_values_5 <- float_list_creator(strsplit(toString(coef_data[4,"values"]), ","))
alternative_values_6 <- float_list_creator(strsplit(toString(coef_data[5,"values"]), ","))
# print(temp_values)

Data <<- read.table(data_filepath, header=T, sep=",");
table_headers = names(Data)
output <- output_filepath;

# path for the dataset that draws pesudo random Halton draws to generate the gumbel error terms
# If you do not have the matrix, you can comment out this line and write code to generate random numbers on the fly
# alternatively, you can uncomment this line and set _gumbel = 0 to avoid considering the unobserved heterogeneity
Halton_File <<- halton_filepath;

ivuno <- "uno";         # Column of ones
ivsero <- "sero";       # Column of zeros

numout <- 0;      # Number of outside goods (i.e., always consumed goods)
config <- case_config;      # Utility specification configuration, possible values: 1, 7
alp0to1 <<- 1;    # 1 if you want the Alpha values to be constrained between 0 and 1, 0 otherwise
price <- 0;       # 1 if there is price variation across goods, 0 otherwise
nc <<- number_of_alternatives;         # Number of alternatives (in the universal choice set) including outside goods
po <<- match("id", table_headers, 0);         # position of pointer to case number in data set,

nrep <- 1;        # Number of sets of error term Halton draws overwhich you want to simulate the unobserved heterogeneity

# 1 if Gumbel error terms are used to simulate the unobserved heterogeneity (i.e., the error terms), 
# 0 if no error terms are used for forecast.
# if _gumbel = 0, then set nrep = 1.
gumbel <- 1;
halton_startrow <- 22; # Number of row in dataset of pesudo random halton. It will read halton data from the row number

tolel <- 0.00000001;
tolee <- 0.01;
avg <- 0;



# Provide labels of dependent variables (i.e., the expenditure variables) below
def <- list_creator(strsplit(alternative_variables, ","));

# Provide labels of price variables below; if no price variables, introduce UNO as the variable
fp_list = c()
for (i in 1:nc){
    fp_list = c(ivuno, fp_list)
}
fp <- fp_list #, ivuno, ivuno, ivuno, ivuno, ivuno, ivuno, ivuno, ivuno, ivuno, ivuno, ivuno, ivuno);


# definition of independent variables 
# ivmt[[1]] has variables that influence baseline preference parameter psi, ivd1 has variables that influence the satiation parameter delta, 
# and ivgt[[1]] has variabels that influence the translation parameter gamma; first numout goods are those always consumed, and first good is numeraire  
# Since gamma=0 for the outside goods, the first numout columns of the ivg vectors will be uno or sero, with no other independent variables in these first numout colums 
ivmt <- list();
ivmtc <- list();

ivmt[[1]] <- c("");    # Do not modify this line because the first alternative is considered as base
ivmtc[[1]] <- c(0.0);  # Do not modify this line because the first alternative is considered as base
# ivmt[[2]] <- c("uno","hhsize");
#ivmtc[[2]] <- c(0.249,-0.03);
#ivmt[[3]] <- c("uno","hhsize");
#ivmtc[[3]] <- c(-0.797,-0.027);
ivmt[[2]] <- alternative_variables_2;
ivmtc[[2]] <- alternative_values_2;
ivmt[[3]] <- alternative_variables_3;
ivmtc[[3]] <- alternative_values_3;
ivmt[[4]] <- alternative_variables_4;
ivmtc[[4]] <- alternative_values_4;
ivmt[[5]] <- alternative_variables_5;
ivmtc[[5]] <- alternative_values_5;
ivmt[[6]] <- alternative_variables_6;
ivmtc[[6]] <- alternative_values_6;


# Important Note: For the satiation parameters (alphas and gammas) do not provide the final values of alphas and gammas. 
# Provide the values of the parameters that are actually estimated in the model. 
# For example, gamma is parameterized as exp(theeta), and theeta is estimated. So provide the theeta values here.
# Simialrly, Alpha is parameterized as 1-(1/exp(delta)). Provide the delta values here.
ivdts <- list();
ivdtc <- list();

ivdts[[1]] <- c("uno");
ivdtc[[1]] <- c(2.604);
ivdts[[2]] <- c("uno");
ivdtc[[2]] <- c(2.718);
ivdts[[3]] <- c("uno");
ivdtc[[3]] <- c(2.408);
ivdts[[4]] <- c("uno");
ivdtc[[4]] <- c(2.711);
ivdts[[5]] <- c("uno");
ivdtc[[5]] <- c(2.456);
ivdts[[6]] <- c("uno");
ivdtc[[6]] <- c(2.604);


   
ivgts <- list();

# ivgts[[1]] <- c("uno");    # Only one "sero" for each output good should be entered
# ivgts[[2]] <- c("uno");
# ivgts[[3]] <- c("uno");
# ivgts[[4]] <- c("uno");
# ivgts[[5]] <- c("uno");
# ivgts[[6]] <- c("uno");

for (i in 1:nc){
    ivgts[[i]] <- c("uno")
}

# The Gamma values for all alternatives are restricted to zero.  
ivgtc <- c(0.0); 


########################################################################################################
#  Do Not Modify Next Three Lines
########################################################################################################
arg_inds <- list(numout, config, alp0to1, price, nc, po, ivuno, ivsero, nrep, gumbel, halton_startrow, tolel, tolee, avg);
arg_vars <- list(Halton_File, output);
result <- alpha_forecast(Data, arg_inds, arg_vars, def, fp, ivmt, ivdts, ivgts, ivmtc, ivdtc, ivgtc);
########################################################################################################
