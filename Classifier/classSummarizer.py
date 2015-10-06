import math, numpy as np

def mean(vals):
    return sum(vals)/float(len(vals))

def std_dev(vals):
    avg = mean(vals)
    variance = sum([pow(x - avg,2) for x in vals])/float(len(vals)-1)
    return math.sqrt(variance)

def extractClasses(dataset, class_index):
    separated = {}
    for i in range(len(dataset)):
        row = dataset[i]
        if (row[class_index] not in separated):
            separated[row[class_index]] = []
        separated[row[class_index]].append(row)
    return separated

def summarize(data, class_index, isRemoveOutliers):
    standardizedSet = zip(*data)
    del standardizedSet[class_index]
    if (isRemoveOutliers):
        standardizedSet = [removeOutliers(x) for x in standardizedSet]
    resultSet = [(mean(x), std_dev((x))) for x in standardizedSet]
    return resultSet

def summarizeClasses(input_list, class_index, isRemoveOutliers):
    separatedSet = extractClasses(input_list, class_index)
    summarySet = {}
    for class_value, instances in separatedSet.iteritems():
        summarySet[class_value] = summarize(instances, class_index, isRemoveOutliers)
    return summarySet

def removeOutliers(x):
    a = np.array(x)
    upper_quartile = np.percentile(a, 75)
    lower_quartile = np.percentile(a, 25)
    IQR = (upper_quartile - lower_quartile) * 1.8
    quartileSet = (lower_quartile - IQR, upper_quartile + IQR)
    resultList = []
    for y in a.tolist():
        if y > quartileSet[0] and y < quartileSet[1]:
            resultList.append(y)
    return resultList
    