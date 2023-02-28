# Nama file     : randomize.py
# Fungsi        : Membangkitkan titik-titik secara random sesuai input

import random as rand

# Generate random points
def randomizePoints(totalPoints, dimension, maximum, minimum):
    points = []
    for i in range(totalPoints):
        point = []
        for j in range(dimension):
            point.append(rand.randint(minimum, maximum))
        points.append(point)
    return points