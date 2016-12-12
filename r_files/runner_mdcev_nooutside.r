list_of_packages = c("utils","foreign","pastecs","mlogit","graphics","VGAM","ZeligChoice","aod","plotrix", "maxLik", "miscTools")

new_packages <- list_of_packages[!(list_of_packages %in% installed.packages()[,"Package"])]

print("-----> Start Loading Packages <-----")
source("r_files/mdcev_nooutside.r");

if(length(new_packages) > 0) {
  install.packages(new_packages, repos="http://cran.rstudio.com/")
}

args <- commandArgs(trailingOnly = TRUE)


if (length(args)==0) {
  stop("At least one argument must be supplied", call.=FALSE)
}

input_file_path = args[1]
number_of_alternatives = strtoi(args[2])
case_config = strtoi(args[3])
utility_variables = args[4]
city_variables =args[5]
output_results_path = args[6]
alternative_2 = args[7]
alternative_3 = args[8]
alternative_4 = args[9]
alternative_5 = args[10]
alternative_6 = args[11]

alternative_variable_2 = list_creator(strsplit(alternative_2, ",") )
alternative_variable_3 = list_creator(strsplit(alternative_3, ",") )
alternative_variable_4 = list_creator(strsplit(alternative_4, ",") )
alternative_variable_5 = list_creator(strsplit(alternative_5, ",") )
alternative_variable_6 = list_creator(strsplit(alternative_6, ",") )

print("#######################")
print(alternative_variable_2)
print(alternative_variable_3)
print(alternative_variable_4)
print(alternative_variable_5)
print(alternative_variable_6)

print("###### This is the utility variables")
variable_list = list_creator(strsplit(utility_variables, ",") )
print(variable_list)

print("-----> Reading Table <-----")
Data <<- read.table(input_file_path, header=T, sep=",");

table_headers = names(Data)

config <- case_config;     # Utility specification configuration, possible values: 1,4,7
alp0to1 <- 1;    # 1 if you want the Alpha values to be constrained between 0 and 1, 0 otherwise
                 # putting _alp0to1 = 1 is recommended practice and can provide estimation stability
price <- 0;      # 1 if there is price variation across goods, 0 otherwise
nc <- number_of_alternatives;         # Number of alternatives (in the universal choice set) including outside goods
po <- match("id", table_headers, 0);         # Index number of ID column in input data

ivuno <- "uno"
ivsero <-"sero"
wtind <<- "uno"

maxlikmethod1 <- "BHHH"; # Method of maximum likelihood for initial estimation ("BHHH" or "BFGS") 
maxlikmethod2 <- "BFGS"; # Method of maximum likelihood for final estimation ("BHHH" or "BFGS") 

# Position of the DEPENDENT variables (i.e., the consumption quantities for each alternative - NOT consumption expenditures for each alternative).
# Number of labels = number of alternatives. 
def <- list_creator(strsplit(city_variables, ","))


# Positions of PRICE variables
# Provide labels of price variables (one label in each double-quote). Number of labels = number of alternatives.
# Provide all UNO variables if there is no price variation 
fp_list = c()
for (i in 1:nc){
  fp_list = c(ivuno, fp_list)
}
fp <- fp_list

# In the following specification, ivm1, ivm2, ivm3 contain independent variable specifications (on right hand side) for baseline utility (PSI) 
# for alternatives 1, 2, and 3;
# Add a row for ivm4 below if there is a 4th alternative, another addiitonal row for ivm5 if there is a 5th alternative, ...  
# (number of rows = number of alternatives);
# Number of columns = Number of variables including alternative specific constants; consider first alternative as base
ivmt <- list();
ivmt[[1]] <- c("");   # Base alternative
ivmt[[2]] <- c("uno", alternative_variable_2);
ivmt[[3]] <- c("uno", alternative_variable_3);
ivmt[[4]] <- c("uno", alternative_variable_4);
ivmt[[5]] <- c("uno", alternative_variable_5);
ivmt[[6]] <- c("uno", alternative_variable_6);

print(ivmt[[2]])
print(ivmt[[3]])
print(ivmt[[4]])
print(ivmt[[5]])
print(ivmt[[6]])


#for (i in 1:nc){
#  if (i == 1){
#    ivmt[[i]] <- c("") # Base alternative
#  }
#  else {
#    ivmt[[i]] <- c("uno", variable_list)
#  }
#}



# In the following specification, ivdts[[1]], ivdts[[2]], ivdts[[3]] contain input data specifications (on right hand side) for satiation parameters (Alphas) 
# for alternatives 1, 2, and 3;
# Add a row below for ivd4 if there is a 4th alternative, another additional row for ivd5 if there is a 5th alternative,.... 
# (number of rows = number of alternatives);
# Number of columns = Number of alternatives; Note that you can also add individual-specific variables below, so that satiation varies across individuals; 
# However, you will then have to translate outputs to compute actual alpha parameters; 
# This code is written to provide you with the alpha parameters directly for the case when there is no variation in alpha across individuals
ivdts <- list();
# ivdts[[1]] <- c("uno");
# ivdts[[2]] <- c("uno");
# ivdts[[3]] <- c("uno");
# ivdts[[4]] <- c("uno");
# ivdts[[5]] <- c("uno");
# ivdts[[6]] <- c("uno");

for (i in 1:nc){
  ivdts[[i]] <- c("uno")
}



# In the following specification, ivgts[[1]], ivgts[[2]], ivgts[[3]] contain input data specifications (on the right hand side) for translation parameters (Gammas) 
# for alternatives 1, 2, and 3
# Add a row for ivgts[[4]] if there is a 4th alternative another additional row for ivgts[[5]] if there is a 5th alternative,.... 
# (number of rows = number of alternatives) Number of columns = Number of alternatives; 
# Note that you can also add individual-specific variables below, so that gamma varies across individuals; 
# However, you will then have to translate outputs to compute actual gamma parameters; 
# This code is written to provide you with the gamma parameters directly for the case when there is no variation in gamma across individuals 
ivgts <- list();
# ivgts[[1]] <- c("uno");
# ivgts[[2]] <- c("uno");
# ivgts[[3]] <- c("uno");
# ivgts[[4]] <- c("uno");
# ivgts[[5]] <- c("uno");
# ivgts[[6]] <- c("uno");

for (i in 1:nc){
  ivgts[[i]] <- c("uno")
}


# Add variable names for translation and satiation variables
# The number of names for both translation and satiation should be equal to the number of alternatives
alpha_name_list = c()
for (i in 1:nc){
  variable_name = paste('D', i, sep = "")
  alpha_name_list = c(alpha_name_list, variable_name)
}
alpha_names <- alpha_name_list

gamma_name_list = c()
for (i in 1:nc){
  variable_name = paste('G', i, sep = "")
  gamma_name_list = c(gamma_name_list, variable_name)
}
gamma_names <- gamma_name_list

########################################################################################################
#  Do Not Modify Next Three Lines
########################################################################################################
arg_inds <- list(config, alp0to1, price, nc, po); 
arg_vars <- list(ivuno, ivsero, wtind, maxlikmethod1, maxlikmethod2);           


result <- mdcev_nooutgood(Data, arg_inds, arg_vars, def, fp, ivmt, ivdts, ivgts, alpha_names, gamma_names);
########################################################################################################
sink(output_results_path)
summary(result); # Show results from the MDCEV model with no outside good
sink()
# write.table(result$estimate,file=output_results_path, sep=',')


