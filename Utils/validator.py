def getPctAccuracy(actual, result, validation_index):
    totalCorrect = 0
    for i in range(len(actual)):
        if actual[i][validation_index] == result[i]:
            totalCorrect += 1
    return totalCorrect/ float(len(actual)) * 100