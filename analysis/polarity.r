library(ggplot2)
library(ggthemes)
library(reshape)
library(plyr)
library(sqldf)

# load data
paragraphs <- read.csv('/Users/djq/repos/flann/output/data.csv')
data_melted <- melt(paragraphs, id=c("chapter", "paragraph"))
chapter_mean <- cast(data_melted, chapter~variable, mean)
chapter_sum <- cast(data_melted, chapter~variable, sum)

# plot paragraph data
(ggplot(paragraphs, aes(paragraph, polarity))
  + geom_point() + geom_rangeframe()) + theme_tufte()

(ggplot(paragraphs, aes(paragraph, polarity))
 + geom_point(aes(size=1/subjectivity)) + geom_rangeframe()) + theme_tufte()

# interjections
(ggplot(paragraphs, aes(paragraph, no_count/word_count))
 + geom_line() + geom_rangeframe()) + theme_tufte()

# plot chapter data
(ggplot(chapter_mean, aes(chapter, polarity))
 + geom_point(aes(size=word_count))) + theme_tufte() + ylim(-1,1) + xlim(1,12)

(ggplot(chapter_mean, aes(chapter, polarity))
 + geom_point(aes(size=subjectivity))) + theme_tufte() + ylim(-1,1) + xlim(1,12)

  # interjections
(ggplot(chapter_sum, aes(chapter, no_count))
 + geom_line() + geom_rangeframe()) + theme_tufte()

