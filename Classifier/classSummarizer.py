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

def summarize(data, class_index):
    resultSet = [(mean(x), std_dev(x)) for x in zip(*data)]
    del resultSet[class_index]
    return resultSet

def summarizeClasses(input_list, class_index):
    separatedSet = extractClasses(input_list, class_index)
    summarySet = {}
    for class_value, instances in separatedSet.iteritems():
        summarySet[class_value] = summarize(instances, class_index)
    return summarySet

def removeOutliers(x):
    sort(x)
    print(x)