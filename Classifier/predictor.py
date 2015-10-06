import math

def normalDistribution(x, mean, std_dev):
    expVal = math.exp(-(math.pow(x - mean, 2)/ (2 * math.pow(std_dev, 2))))
    return (1/(math.sqrt(2 * math.pi) * std_dev)) * expVal

def classProbabilities(summarySet, input_list):
    probabilities = {}
    for classVal, summaries in summarySet.iteritems():
        probabilities[classVal] = 1
        for i in range(len(summaries)):
            mean, std_dev = summaries[i]
            attribute_value = input_list[i]
            probabilities[classVal] *= normalDistribution(attribute_value, mean, std_dev)
    return probabilities

def predictEntry(summarySet, inputEntry):
    probabilities = classProbabilities(summarySet, inputEntry)
    label, bestProbabilty = None, -1
    for classVal, probability in probabilities.iteritems():
        if label is None or probability > bestProbabilty:
            bestProbabilty = probability
            label = classVal
    return label

def getAllPredictions(summarySet, testingSet):
    predArr = []
    for i in range(len(testingSet)):
        predArr.append(predictEntry(summarySet, testingSet[i]))
    return predArr

