import main, Classifier.classSummarizer as math

outlierSet = []
standardizedSet = []
outlierConstant = 1.5
for i in range(0, 100):    
    for i in range(500):
        outlierSet.append(main.runMe(False, outlierConstant))
        standardizedSet.append(main.runMe(True, outlierConstant))

    print "*** RESULTS AFTER 1000 RUNS ***"
    print "CONSTANT ", outlierConstant
    print "Average accuracy for an outlier set: ", math.mean(outlierSet)
    print "Average accuracy for a standardized set: ", math.mean(standardizedSet)
    print "Standard deviation of outlier set accuracies: ", math.std_dev(outlierSet)
    print "Standard deviation of standardized set accuracies: ", math.std_dev(standardizedSet)

    outlierConstant += 0.05
