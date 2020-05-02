# weight = [3,5,2,6,7,1,2,7,1,7]  # Hours
# height = [80,90,75,80,90,50,65,85,40,100]  # Percentage


# weight = [3, 4, 5, 5, 6, 8, 7, 7.5, 9, 8, 4.5, 4, 6.5, 7, 2, 6, 4, 11, 10.5]  # No of years Of extperience
# height = [10, 10, 15, 15, 20, 15, 20, 25, 20, 25, 30, 25, 30, 15, 25, 20, 25, 20, 15]  #  % Hike

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


y = (mean * 2) + height_intercept  # y= mx + c (y- dependent variable m - Mean or c - Intercept at y)
print(y)
