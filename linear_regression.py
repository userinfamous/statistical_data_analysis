# Linear Regression
# (y-hat: predicteed value) = a + bx
# y = line
# a = the intercept (we use mean as the intercept)
# b = slope
# x = x-axis value

#===/Formula/====#
#               sigma(xy) * sigma(x)(sigma(y)
# b =    ========================================
#               n(sigma(x^2)) - sigma(x)^2

#Import
import matplotlib.pyplot as plt
import numpy as np

#Variables
x_list = [2,6,7,9,12] # <=== X Dataset
y_list = [90,45,30,5,2] # <=== Y Dataset

# DO NOTE CHANGE
predicted_y = []
n = len(x_list)
sigma_xy = 0
sigma_y = sum(y_list)
sigma_x = sum(x_list)
sigma_xx = 0

# Sigma X^2
for i in x_list:
    sigma_xx += pow(i,2)

# Sigma XY
for i in range(n):
    sigma_xy += x_list[i] * y_list[i]

# Setting up the formula
numerator = (sigma_xy) - (sigma_x * sigma_y)/n
denominator = (sigma_xx) - pow(sigma_x,2)/n

# Linear Regression Line
slope = numerator/denominator

# Finding the y-intercept
x_average = sum(x_list)/len(x_list)
y_average = sum(y_list)/len(y_list)
a = y_average - (slope*x_average)

#predicted slopt (linear regression) over the x-axis
for x in x_list:
    y_hat = a + slope*x
    predicted_y.append(y_hat)

#Show equation
print("n = %.3f, sigma_xy = %.3f, sigmax^2 = %.3f" % (n,sigma_xy,sigma_xx))
print("y-hat = %.3f + %.3fx" % (a,slope))
plt.plot([x_list],[y_list],"ro")
plt.plot(x_list,predicted_y)
plt.ylabel('y')
plt.xlabel('x')
plt.show()
