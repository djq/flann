library("ggplot2")
library("ggthemes")

data = read.csv('/Users/djq/repos/flann/output/data.csv')


(ggplot(data, aes(paragraph, polarity))
  + geom_point() + geom_rangeframe())


(ggplot(data, aes(paragraph, polarity))
  + geom_line() + geom_rangeframe()
  + theme_tufte())

 (ggplot(mtcars, aes(factor(cyl), mpg)) 
 + theme_tufte(ticks=FALSE)
 + geom_tufteboxplot())