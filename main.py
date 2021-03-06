import Utils.reader as reader, Classifier.classSummarizer as summarizer, Classifier.predictor as predictor, Utils.validator as validator

filename = 'Assets/wine.csv'
totalSet = reader.loadFile(filename)

def runMe(isRemoveOutliers, outlierConstant):
    trainingSet, testingSet = reader.getTrainAndTestSet(totalSet, 0.70)
    #This line creates a tuple containing for every mean and std_dev for every attribute FOR each class (lots of stuff)
    classSummaries = summarizer.summarizeClasses(trainingSet, 0, isRemoveOutliers, outlierConstant)
    predictions = predictor.getAllPredictions(classSummaries, testingSet)
    accuracy = validator.getPctAccuracy(testingSet, predictions, 0)
    # print ('Accuracy: {0}%').format(accuracy)
    return accuracy
