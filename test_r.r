# Get the args from the line
args <- commandArgs(trailingOnly = TRUE)

if (length(args)==0) {
  stop("At least one argument must be supplied", call.=FALSE)
}

for (val in args) {
  print(val)
}

