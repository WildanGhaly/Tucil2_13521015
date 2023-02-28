# Nama file     : distance.py
# Fungsi        : Menghitung jarak antara dua titik

import math

# Calculate the distance between two points
def getDistance(point1, point2, totalOperation):
    distance = 0
    for i in range (len(point1)):
        distance += (point1[i] - point2[i])**2
    return math.sqrt(distance), totalOperation + 1