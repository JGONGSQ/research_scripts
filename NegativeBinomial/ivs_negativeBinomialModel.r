listOfPakcages <- c("foreign", "ggplot2", "MASS")

newPackages <- listOfPakcages[!(listOfPakcages %in% installed.packages()[,"Package"])]

if (length(newPackages) > 0) {
  install.packages(newPackages, repos = "http://cran.rstudio.com/")
} 
# install.packages("countreg", repos="http://R-Forge.R-project.org")
library("foreign")
library("ggplot2")
library("MASS")
library("countreg")

rm(list=ls())

# read the data
data <- read.table("/Users/daddyspro/Desktop/master_project/Data/ivs/2012/NB_Model_IVS_2012.csv", header = T, sep = ",")

# qplot(data$Duration, geom="histogram", binwidth = 1)
#  NUMSTOP + NUMVISIT
# estimate the model with Negative Binomial
nbm <- glm.nb(AUSNITES ~ GENDER + MARITAL + AGEGROUP + NUMSTOP +
                PARTYPE + TRIP_PURPOSE + CUSTOMS, data=data)


summary(nbm)

simulateResults <- rnegbin(fitted(nbm), theta=nbm$theta)
simulateResults_with_offset <- simulateResults + 1
# simulate the results
#predictResult <- predict.glm(nbm, newdata = data, type = "response")
# predictResult <- predict(nbm, newdata = data)
# write the results to the csv file
# outputFile = "/Users/daddyspro/Desktop/test_forecast.csv"
# write.csv(summary.glm(nbm)$coefficients, outputFile)

# initial the data with data frame
durationInput <- data.frame(Duration = data$AUSNITES)
# durationOutput <- data.frame(Duration = simulateResults)
durationOutput <- data.frame(Duration = simulateResults_with_offset)

# define the data type
durationInput$type <- 'Observed'
durationOutput$type <- 'Simulated'

# combine the values
durationValues <- rbind(durationInput, durationOutput)

# plot the compared results
ggplot(durationValues, aes(Duration, fill = type), binwidth = 1) + geom_histogram(alpha = 0.5, position = 'identity', binwidth = 1)

