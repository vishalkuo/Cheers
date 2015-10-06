import main, Classifier.classSummarizer as math

outlierSet = []
standardizedSet = []
for i in range(10000):
    outlierSet.append(main.runMe(False))
    standardizedSet.append(main.runMe(True))

print "*** RESULTS ***"
print "Average accuracy for an outlier set: ", math.mean(outlierSet)
print "Average accuracy for a standardized set: ", math.mean(standardizedSet)
print "Standard deviation of outlier set accuracies: ", math.std_dev(outlierSet)
print "Standard deviation of standardized set accuracies: ", math.std_dev(standardizedSet)