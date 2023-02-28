# Nama file     : bruteForce.py
# Fungsi        : Mencari titik terdekat dengan algoritma brute force

import distance as dist

# Pencarian titik terdekat dengan algoritma brute force
def bruteForce(points):
    minDistance = float('inf')
    closestPair = None
    totalOperation = 0;
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distance, totalOperation = dist.getDistance(points[i], points[j], totalOperation)
            if distance < minDistance:
                minDistance = distance
                closestPair = (points[i], points[j])
    return (minDistance, 
            closestPair, 
            totalOperation)