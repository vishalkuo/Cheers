import csv, os, random

def loadFile(fileName):
    lines = csv.reader(open(fileName, "rb"))
    rows = list(lines)
    for i in range(len(rows)):
        rows[i] = [float(attribute) for attribute in rows[i]]
    return rows

"""
" We want to split our total set into a training set and a testing set to build our data off of
"""
def getTrainAndTestSet(totalSet, splitPct):
    trainSetSize = int(len(totalSet) * splitPct)
    trainSet = []
    copy = list(totalSet)
    while len(trainSet)< trainSetSize:
        randIndex = random.randrange(len(copy))
        trainSet.append(copy.pop(randIndex))
    return (trainSet, copy)