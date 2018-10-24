from math import sqrt
# R Correlation
# Z score is the data minus
x = [2,1,3,2,4,5,3]
y = [4,3,4,3,6,5,5]
n = len(x)

#               r = n(sigma xy)-(sigma x)(sigma y)                      //numerator//
#   ===========================================================         //divided by//
#   sqrt([nsigma x^2 - (sigma x)^2][nsigma y^2 - (sigma y)^2] )         //denominator//
sigma_xy = 0
sigma_x = sum(x)
sigma_y = sum(y)
sigma_xx = 0
sigma_yy = 0

for i in range(0,len(x)):
    sigma_xy += x[i]*y[i]
for i in x:
    sigma_xx += pow(i,2)
for i in y:
    sigma_yy += pow(i,2)

numerator = (n*sigma_xy)-(sigma_x * sigma_y)
denominator = sqrt( (n*(sigma_xx) - pow((sigma_x),2)) * (n*(sigma_yy) - pow((sigma_y),2)) )

print(numerator/denominator)
