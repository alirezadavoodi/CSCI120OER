#Write a python programs which find the closest distance to the center of the coordination
#system:
#pointA = (-3,2)
#pointB = (1,3)
#pointC = (4,0)

pointA_x = -3
pointA_y = 2

pointB_x = 1
pointB_y = 3

pointC_x = 4
pointC_y = 0

pointCenter_X = 0
pointCenter_Y = 0

from math import sqrt
#d1 is the distance between pointA and the center
d1 = sqrt((pointCenter_X-pointA_x)**2 + (pointCenter_Y-pointA_y)**2)

#d2 is the distance between pointB and the center 
d2 = sqrt((pointCenter_X-pointB_x)**2 + (pointCenter_Y-pointB_y)**2)

d3 = sqrt((pointCenter_X-pointC_x)**2 + (pointCenter_Y-pointC_y)**2)

minimumDistance = min(d1, d2, d3)

print("min of d1=%f and d2=%f and d3=%f is equal to %f" %(d1, d2, d3, minimumDistance))


