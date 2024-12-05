library(tidyr)
tmp <- read.csv('life_exp.csv') %>% pivot_longer(c(starts_with(c('le','sd')))) %>%
    separate(name, into = c('type','sex','education'), sep = "_")

## Hacky: this manipulation to get separate columns for life expectancy and sd
## could be done more elegantly.
data <- tmp[tmp$type == 'le', ]
sd <- tmp[tmp$type == 'sd', ]

names(data)[5] <- 'lifeexp'
data$sd <- sd$value

plot(data$lifeexp, data$sd)

## Some different ways to display the relationships.

library(ggplot2)

ggplot(data, aes(x = lifeexp, y = sd)) + geom_point() + facet_wrap(~country)
ggplot(data, aes(x = lifeexp, y = sd)) + geom_point(aes(color = sex, shape = education)) + facet_wrap(~country)

ggplot(data, aes(x = lifeexp, y = sd)) + geom_point(aes(color = education)) + facet_wrap(~sex)

ggplot(data, aes(x = lifeexp, y = sd)) + geom_point(aes(color = sex)) + facet_wrap(~education)

