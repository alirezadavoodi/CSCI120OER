
# Write a Python function which has a list of points as its input parameter. 
# Each point is represented by a dictionary with 3 keys and each key has a value. 
# The keys of the point dictionary is “x”, “y” and “z”. Each point represent a position in the 3D coordination system (space). 
# The function should find and return the point in the input list which has the minimum distance to the center of the 
# coordination system. The center of the coordination system is a point whose 
# values for all the keys are 0 (i.e: center = {“x”=0, “y”=0, “z”=0}

from math import sqrt

def distanceBetween2Points(p1, p2):
    p1x = p1["x"]
    p1y = p1["y"]
    p1z = p1["z"]

    p2x = p2["x"]
    p2y = p2["y"]
    p2z = p2["z"]

    distance = sqrt((p1x-p2x)**2 + (p1y-p2y)**2 + (p1z-p2z)**2)
    return distance

def findClosestPointToCenter(points):
    center = {"x": 0, "y": 0, "z": 0}
    minDistance = distanceBetween2Points(points[0], center)
    closestPoint = points[0]

    for point in points:
        distance = distanceBetween2Points(point, center)
        if distance < minDistance:
            minDistance = distance
            closestPoint = point
    
    return (minDistance, closestPoint)

result = findClosestPointToCenter(
    [
        {"x": 1, "y": 4, "z": 1}, {"x": 3, "y": 7, "z": 10},
        {"x": -1, "y": 3, "z": 4}, {"x": 4, "y": 4, "z": 2},
        {"x": 7, "y": -4, "z": 0}, {"x": 10, "y": 4, "z": 1}

    ]
)

print(result)