datasets = read.csv("Data.csv")
datasets = datasets[, 2:3]
#taking care of missing data

"datasets$Age = ifelse(is.na(datasets$Age),
                      ave(datasets$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                      datasets$Age)
datasets$Salary = ifelse(is.na(datasets$Salary),
                      ave(datasets$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                      datasets$Salary)"

#encoding categorial data

"datasets$Country = factor(datasets$Country,
                          levels = c('France',  'Spain', 'Germany'),
                          labels = c(1, 2, 3))
datasets$Purchased = factor(datasets$Purchased,
                          levels = c('Yes',  'No'),
                          labels = c(1, 0))"

#splitting the dataset into the training set and test set
library(caTools)
set.seed(123)
split = sample.split(datasets$Purchased, SplitRatio = 0.8)
trainingSet = subset(datasets, split == TRUE)
testSet = subset(datasets, split == FALSE)

#scaling feature
"trainingSet[, 2:3] = scale(trainingSet[, 2:3])
testSet[, 2:3] = scale(testSet[, 2:3])"