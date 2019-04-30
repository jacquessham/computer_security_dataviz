library(ggplot2)
library(dplyr)
library(magrittr)

setwd("/Users/jacquessham/Documents/MSDS/MSAN622/Homework/Week3")
data <- read.csv("computer_security.csv")
# Convert string to date type
data$date <- as.Date(data$date, format="%Y-%m-%d")
sub_data <- data[((data$date=="2006-08-24"&data$l_ipn==1)|
                 (data$date=="2006-09-04"&data$l_ipn==5)|
                 (data$date=="2006-09-18"&data$l_ipn==4)|
                 (data$date=="2006-09-26"&(data$l_ipn==3|data$l_ipn==6))),]

data_1_2108 <- data[(data$l_ipn==1&data$r_asn==2108),]
data_1_3307 <- data[(data$l_ipn==1&data$r_asn==3307),]

uni1 <- unique(sub_data$r_asn[sub_data$l_ipn==1])

# Plot on ggplot to have a glance
all_ipn %>% ggplot() + geom_point(aes(x=date, y=sumtraffic, color=factor(l_ipn))) +
  geom_vline(xintercept = as.Date("2006-08-24", format="%Y-%m-%d")) +
  geom_vline(xintercept = as.Date("2006-09-04", format="%Y-%m-%d")) +
  geom_vline(xintercept = as.Date("2006-09-18", format="%Y-%m-%d")) +
  geom_vline(xintercept = as.Date("2006-09-26", format="%Y-%m-%d"))

all_ipn2 <- data %>% group_by(l_ipn, date) %>% summarise(sumtraffic = log(sum(f))) %>% 
  filter(l_ipn==3)
all_ipn2 %>% ggplot() + geom_point(aes(x=date, y=sumtraffic, color=factor(l_ipn))) +
  geom_vline(xintercept = as.Date("2006-08-24", format="%Y-%m-%d")) +
  geom_vline(xintercept = as.Date("2006-09-04", format="%Y-%m-%d")) +
  geom_vline(xintercept = as.Date("2006-09-18", format="%Y-%m-%d")) +
  geom_vline(xintercept = as.Date("2006-09-26", format="%Y-%m-%d"))

# Export the aggregated numbers to plot in Python
all_ipn <- data %>% group_by(l_ipn, date) %>% summarise(sumtraffic = sum(f))
all_ipn_log <- data %>% group_by(l_ipn, date) %>% summarise(sumtraffic = log(sum(f)))
write.csv(all_ipn, file="data.csv")
write.csv(all_ipn_log, file="data_log.csv")