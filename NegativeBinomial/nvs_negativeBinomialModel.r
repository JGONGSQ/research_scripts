listOfPakcages <- c("foreign", "ggplot2", "MASS")

newPackages <- listOfPakcages[!(listOfPakcages %in% installed.packages()[,"Package"])]

if (length(newPackages) > 0) {
  install.packages(newPackages, repos = "http://cran.rstudio.com/")
} 
library("foreign")
library("ggplot2")
library("MASS")
rm(list=ls())

# read the data
# data <- read.table("/Users/daddyspro/Desktop/master_project/Data/test_output_file.csv", header = T, sep = ",")
data <- read.table("/Users/daddyspro/Desktop/master_project/Data/NB_ModelData2007.csv", header = T, sep = ",")
# qplot(data$Duration, geom="histogram", binwidth = 1)

# estimate the model with Negative Binomial
# nbm <- glm.nb(NITESUM ~ HOMESLA + ORIGIN_NSW + ORIGIN_VIC + ORIGIN_QLD + ORIGIN_SA + ORIGIN_TAS + ORIGIN_NT + ORIGIN_ACT +
#                 HOUSEHOLD + HOUSINC_LOW + HOUSINC_MEDIUM + HOUSINC_HIGH +
#                 EMPLOYMENT_WORKING + EMPLOYMENT_RETIRED + EMPLOYMENT_STUDYING + GENDER_MALE + MARITAL_SINGLE +
#                 LIFECYCLE_SINGLE + LIFECYCLE_COUPLE_NO_KIDS +
#                 AGEGROUP_15_29 + AGEGROUP_30_39 + AGEGROUP_40_49 + AGEGROUP_50_59 + AGEGROUP_60_69 + CH15TO24,
#               data=data)

nbm <- glm.nb(NITESUM ~ HOMESLA + ORIGIN + HOUSEHOLD + HOUSINC +  EMPLOYMENT +
  GENDER + MARITAL + LIFECYCLE + AGEGROUP + CH15TO24,
data=data)

# nbm <- glm.nb(Duration ~ HOUSEHOLD + HOUSINC_LOW + HOUSINC_HIGH,
#               data=data, init.theta = 3)

# nbm <- glm(Duration ~ EMPLOYMENT_WORKING,
#            family = negative.binomial(), data=data)
# "poisson" glm.fit()
summary(nbm)


simulateResults <- rnegbin(fitted(nbm), mu = nbm$theta, theta = nbm$theta)
# simulateResults <- rnegbin(fitted(nbm), mu = 3.97, theta = 0.68)
simulateResults_with_offset <- simulateResults + 1
# simulate the results
# predictResult <- predict.glm(nbm, newdata = data, type = "response")
# predictResult <- predict(nbm, newdata = data)
# write the results to the csv file
# outputFile = "/Users/daddyspro/Desktop/test_forecast.csv"
# write.csv(summary(nbm)$coefficients, outputFile)

# initial the data with data frame
durationInput <- data.frame(Duration = data$NITESUM)
# durationOutput <- data.frame(Duration = simulateResults)
durationOutput <- data.frame(Duration = simulateResults_with_offset)

# define the data type
durationInput$type <- 'Observed'
durationOutput$type <- 'Simulated'

# combine the values
durationValues <- rbind(durationInput, durationOutput)

# plot the compared results
ggplot(durationValues, aes(Duration, fill = type), binwidth = 1) + geom_histogram(alpha = 0.5, position = 'identity', binwidth = 1)

