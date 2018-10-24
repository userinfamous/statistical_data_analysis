# Imports
from math import sqrt
from random import randint

#List of data
list = [1,2,3,4,5,6,7,8,9,10]

def standard_deviation(list):
    mean = sum(list)/len(list)
    variance = 0
    standardard_deviation = 0
    for i in list:
        variance += pow(i - mean,2)
    print('%.2f' % sqrt(variance))
