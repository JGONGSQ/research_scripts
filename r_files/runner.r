# Get the args from the line
args <- commandArgs(trailingOnly = TRUE)

if (length(args)==0) {
  stop("At least one argument must be supplied", call.=FALSE)
}

# define the input file path with argus
input_file_path = args[1]
sprintf("-----> path %s",input_file_path)
num_of_outside_goods = strtoi(args[2])
num_of_alternatives = strtoi(args[3])
case_config = strtoi(args[4])

# Reading the data
print("--->>> Reading data <<<---")

Data <<- read.table(input_file_path, header=T, sep=",") 
# some initial value for the model
print("--->>> Initial the data <<<---")

nobs = nrow(Data)
numout = num_of_outside_goods
config = case_config
alp0to1 = 1 # 1 if you want the Alpha values to be constrained between 0 and 1, 0 otherwise
            # putting _alp0to1 = 1 is recommended practice and can provide estimation stability

sprintf('nobs: %i, numout: %i, config: %i', nobs, numout, config)

# get the table headers
table_headers = names(Data)

# get the index number of each variables
price = 0 # equal to 1, if there is price variation across goods, 0 otherwise
nc = num_of_alternatives  #Number of alternatives (in the universal choice set) including outside goods
# po = 7 # need to ask cicy about this value, not sure what is it, might be the id value?
po = match("id", table_headers, 0)
ivuno = match("uno", table_headers, 0)
ivsero = match("sero", table_headers, 0)
wtind = ivuno

sprintf('ivuno: %i, ivsero: %i, number of alternatives: %i, po: %i', ivuno, ivsero, num_of_alternatives, po)

if (po == 0 || ivuno ==0 || ivsero == 0 ){
  stop("One of the po, ivuno or ivsero is 0, please check your data table" ,call.=FALSE)
}















