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