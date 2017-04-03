list_of_packages = c("foreign", "nnet", "ggplot2", "reshape2", "mlogit", "afex", "car")

new_packages <- list_of_packages[!(list_of_packages %in% installed.packages()[,"Package"])]

if(length(new_packages) > 0) {
  install.packages(new_packages, repos="http://cran.rstudio.com/")
}
library("nnet", "mlogit", "afex", "car")
Data <<- read.table("/Users/daddyspro/Desktop/master_project/Data/results/sequence.csv", header = T, sep=",")

# This is the function to use in R code. for sequence MNL we might user a logit 
mu <- multinom(destination ~ HOUSINC + last_visited + GENDER + HOMESLA + HOUSEHOLD + AGEGROUP + LIFECYCLE + OVER15, data = Data)
summary <- summary(mu)
print(summary)
# z <- summary(mu)$coefficients/summary(mu)$standard.errors
# p <- (1 - pnorm(abs(z), 0,1)) * 2
# print(p)

# set_sum_contrasts()
# anova(mu, type="III")

forecast_result <- predict(mu, newdata=Data)

outputfile = "/Users/daddyspro/Desktop/master_project/Data/results/sequence_forecast.csv"
write.csv(data.frame(forecast_result), outputfile)