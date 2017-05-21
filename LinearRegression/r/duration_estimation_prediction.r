rm(list=ls())

# Read the data from the excel
data <- read.table("/Users/daddyspro/Desktop/master_project/data/test_output_file.csv", header=T, sep=",")



# Model Estimation
time_model <- lm(Duration ~ HOUSEHOLD + 
                   EMPLOYMENT_WORKING +  EMPLOYMENT_RETIRED + 
                   HOUSINC_LOW + HOUSINC_MEDIUM + HOUSINC_HIGH + 
                   ORIGIN_QLD	+ ORIGIN_WA +	ORIGIN_TAS + ORIGIN_NT + 
                   LIFECYCLE_COUPLE_NO_KIDS + 
                   CH15TO24 + 
                   DISTANCE_TO_NSW +	DISTANCE_TO_VIC +	DISTANCE_TO_QLD +	
                   DISTANCE_TO_SA +	DISTANCE_TO_TAS +	DISTANCE_TO_NT, data=data);


# Model Results
print(summary(time_model))