'''
Sample code to find the accurate Intercept (C) and Slope or Gradient of Line (M) for 2D Linear Equation 
'''

weight = [0.5, 2.3, 2.9]
height = [1.4, 1.9, 3.2]


weight_mod = sum(weight) / len(weight)  # x -- axis
height_mod = sum(height) / len(height)  # y --axis

weight_minus_weight_mod = [(weight[i] - weight_mod) for i in range(len(weight))]  # ([x1 - mod(x)])
height_minus_height_mod = [(height[i] - height_mod) for i in range(len(height))]  # ([y1 -mod(y)])

multiply_mods = [(weight_minus_weight_mod[i] * height_minus_height_mod[i]) for i in range(len(weight))]  # (x1 - mod(x))(y1 - mod(y))
square_weight_mods = [(weight_minus_weight_mod[i] * weight_minus_weight_mod[i]) for i in range(len(weight))] # (x1 - mod(x)) ^2

'''
M = (x1 - mod(x))(y1 - mod(y))/(x1 - mod(x)) ^2
'''

mean = sum(multiply_mods)/sum(square_weight_mods) 

height_intercept = height_mod - (mean * weight_mod) # Constant


y = (mean * 2) + height_intercept  # y= mx + c (y- dependent variable m - Slope or c - Intercept at y)
print(y)
