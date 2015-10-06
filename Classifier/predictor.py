import math

def normalDistribution(x, mean, stdev):
    exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
    return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent

def standardizeData(x, mean, stdev):
    return (x - mean)/stdev

def classProbabilities(summaries, input_list):
    probabilities = {}
    for classVal, classSummaries in summaries.iteritems():
        probabilities[classVal] = 0
        for i in range(len(classSummaries)):
            mean, std_dev = classSummaries[i]
            vector = input_list[i]
            # vector = standardizeData(vector, mean, std_dev)
            # We take logarithmic probabilties because we tend so close to 0 otherwise
            if normalDistribution(vector, mean, std_dev) > 0:
                probabilities[classVal] += math.log(normalDistribution(vector, mean, std_dev))
            # probabilities[classVal] *= normalDistribution(vector, mean, std_dev)
    
    return probabilities

def predictEntry(summaries, inputVal):
    probabilities = classProbabilities(summaries, inputVal)
    label, bestProbability = None, -1
    for classVal, probabiltiy in probabilities.iteritems(): 
        if label is None or probabiltiy > bestProbability:
            bestProbability = probabiltiy
            label = classVal
    return label

def getAllPredictions(summarySet, testingSet):
    predArr = []
    for i in range(len(testingSet)):
        predArr.append(predictEntry(summarySet, testingSet[i]))
    return predArr

