#Simple Linear Regression
datasets = read.csv("Salary_Data.csv")

#splitting the dataset into the training set and test set
library(caTools)
set.seed(123)
split = sample.split(datasets$Salary, SplitRatio = 2/3)
trainingSet = subset(datasets, split == TRUE)
testSet = subset(datasets, split == FALSE)

#Fitting Simple Linear Regression to the Training set
regressor = lm(formula = Salary ~ YearsExperience,
               data = trainingSet)
#Predicting the Test set Results
yPrediction = predict(regressor, newdata = testSet)
#Visualizing the Training set result
library(ggplot2)
ggplot() +
  geom_point(aes(x = trainingSet$YearsExperience, y = trainingSet$Salary), 
             colour = 'red') +
  geom_line(aes(x = trainingSet$YearsExperience, y = predict(regressor, newdata = trainingSet)),
            colour = 'blue') +
  ggtitle('Salary VS Experience (Training set)') + 
  xlab('Year of Experience') +
  ylab('Salary')

#Visualizing the Test set Results
ggplot() +
  geom_point(aes(x = testSet$YearsExperience, y = testSet$Salary), 
             colour = 'red') +
  geom_line(aes(x = trainingSet$YearsExperience, y = predict(regressor, newdata = trainingSet)),
            colour = 'blue') +
  ggtitle('Salary VS Experience (Test set)') + 
  xlab('Year of Experience') +
  ylab('Salary')