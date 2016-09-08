# Get the args from the line
args <- commandArgs(trailingOnly = TRUE)

if (length(args)==0) {
  stop("At least one argument must be supplied", call.=FALSE)
}

# define the input file path with argus
input_file_path = args[1]
num_of_outside_goods = args[2]

# Read the data
print("Reading data")
Data <<- read.table(input_file_path, header=T, sep=",") 

# get the table headers
print("Initial the data")
table_headers = names(Data)

# get the index number of each variables
ivuno = match("uno", table_headers, 0)
ivsero = match("sero", table_headers, 0)
sprintf('ivuno %i', ivuno)
print(ivsero)

nobs = nrow(Data)
numout = num_of_outside_goods 
print(nobs)
print(numout)




