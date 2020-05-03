'''
        _   _      _       _       _    _         _           _    _     _
X   Y   X   Y    X-X     Y-Y    (X-X)(Y-Y)     (X-X)^2     (X-X)(Y-Y)/(X-X)^2
'''

x = [1,2,3,4,5]
y = [2,4,5,4,5]


x_mod = sum(x) / len(x)
y_mod = sum(y) / len(y)

x_minus_x_mod = [(x[i] - x_mod) for i in range(len(x))]
y_minus_y_mod = [(y[i] - y_mod) for i in range(len(y))]

multiply_xy_mods = [(x_minus_x_mod[i] * y_minus_y_mod[i]) for i in range(len(x))]
square_x_mods = [(x_minus_x_mod[i] * x_minus_x_mod[i]) for i in range(len(x))]


slope = sum(multiply_xy_mods)/sum(square_x_mods)
intercept = y_mod - (slope * x_mod)

print('Slope: ', slope)
print('Intercet At Y: ', intercept)

# Now If you want You Can Substitute All the Values in
# y= mx+c and Input the Independent Variable to get the
# Approximate Value of y.
# Example : y = mx+c
#Slope:  0.6 -- m
#Intercet At Y:  2.2 - constant C
# y = 0.6 * 2.5 + 2.2
