library(ggplot2)
library(ggthemes)
library(reshape)
library(plyr)

# load data
data <- read.csv('/Users/djq/repos/flann/output/data.csv')
data_long <- melt(data, id=c("paragraph", "polarity"))

# rename col
data_long <- rename(data_long, c('variable'='sentiment'))

# plot
(ggplot(data, aes(paragraph, polarity))
  + geom_point() + geom_rangeframe()) + theme_tufte()

(ggplot(data, aes(paragraph, polarity))
 + geom_point(aes(size=positive + negative)) + geom_rangeframe()) + theme_tufte()

(ggplot(data_long, aes(paragraph, polarity))
 + geom_point(aes(colour=sentiment))) + theme_tufte()

