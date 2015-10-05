import Utils.reader as reader

filename = 'Assets/wine.csv'
totalSet = reader.loadFile(filename)

trainingSet, testingSet = reader.getTrainAndTestSet(totalSet, 0.67)
