from math import sqrt

# x and y axis on the scatter plot
x = [2,1,3,2,4,5,3]
y = [4,3,4,3,6,5,5]

# number of dataset
n = len(x)

# ==//Formula//==
#                   n(sigma xy)-(sigma x)(sigma y)                          //numerator//
#  R =  ===========================================================         //divided by//
#       sqrt([nsigma x^2 - (sigma x)^2][nsigma y^2 - (sigma y)^2] )         //denominator//

# ==//Variables//==
sigma_xy = 0
sigma_x = sum(x)
sigma_y = sum(y)
sigma_xx = 0
sigma_yy = 0

# ==//Maths==//
for i in range(0,len(x)):
    sigma_xy += x[i]*y[i]
for i in x:
    sigma_xx += pow(i,2)
for i in y:
    sigma_yy += pow(i,2)

# Separating into two different set of equations
numerator = (n*sigma_xy)-(sigma_x * sigma_y)
denominator = sqrt( (n*(sigma_xx) - pow((sigma_x),2)) * (n*(sigma_yy) - pow((sigma_y),2)) )

print(numerator/denominator)
