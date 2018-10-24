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


# List1 is for the data set
list1 = []

# List2 is for generating random sampling from the data
list2 = []

# Starting from 0
j=0

# Number of random samples
n=0

# Math
while j < n:
    name = list1[randint(0,len(list1)-1)]
    if name not in list2:
        list2.append(name)
        j += 1
for j in list2:
    print(j)
