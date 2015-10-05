import math

def mean(input_list):
    return sum(input_list) / len(input_list)

"""
" Implementation of sample standard deviation
"""
def std_dev(input_list):
    avg = mean(input_list)
    variance = sum([pow(x - avg, 2) for x in input_list]) / float(len(input_list) - 1)
    return math.sqrt(variance)

def extractClasses(dataset, class_index):
    separated = {}
    for i in range(len(dataset)):
        row = dataset[i]
        if (row[class_index] not in separated):
            separated[row[class_index]] = []
        separated[row[class_index]].append(row)
    return separated

def summarize(list, class_index):
    resultSet = [(mean(x), std_dev(x)) for x in zip(*list)]
    del resultSet[class_index]
    return resultSet

def summarizeClasses(input_list, class_index):
    separatedSet = extractClasses(input_list, class_index)
    summarySet = {}
    for class_value, instances in separatedSet.iteritems():
        summarySet[class_value] = summarize(instances, class_index)
    return summarySet