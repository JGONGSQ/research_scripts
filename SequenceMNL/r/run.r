list_of_packages = c("foreign", "nnet", "ggplot2", "reshape2", "mlogit")

new_packages <- list_of_packages[!(list_of_packages %in% installed.packages()[,"Package"])]

if(length(new_packages) > 0) {
  install.packages(new_packages, repos="http://cran.rstudio.com/")
}
library("nnet", "mlogit")
Data <<- read.table("/Users/daddyspro/Desktop/SMNL_Data.csv", header = T, sep=",")

# This is the function to use in R code. for sequence MNL we might user a logit 
mu <- multinom(choice ~ income + last_visit + distance, data = Data)
summary <- summary(mu)
print(summary)
forecast_result <- predict(mu, newdata=Data)

outputfile = "/Users/daddyspro/Desktop/test.csv"
write.csv(data.frame(forecast_result), outputfile)