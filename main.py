import Utils.reader as reader, Classifier.classSummarizer as summarizer

filename = 'Assets/wine.csv'
totalSet = reader.loadFile(filename)

trainingSet, testingSet = reader.getTrainAndTestSet(totalSet, 0.67)
classSummaries = summarizer.summarizeClasses(totalSet, 0)
print classSummaries