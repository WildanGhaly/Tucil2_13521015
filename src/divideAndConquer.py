# Nama file     : divideAbdConquer.py
# Fungsi        : Mencari titik terdekat dengan algoritma divide and conquer

import distance as dist

# Pencarian titik terdekat dengan algoritma divide and conquer
def divideAndConquer(points, totalOperation):
    if (len(points) == 2):
        distance, totalOperation = dist.getDistance(points[0], points[1], totalOperation)
        return (distance, points[0], points[1], totalOperation)
    
    elif (len(points) == 3):
        minDistance = float('inf')
        point1 = points[0]
        point2 = points[1]
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dis, totalOperation = dist.getDistance(points[i], points[j], totalOperation)
                if (dis < minDistance):
                    minDistance = dis
                    point1 = points[i]
                    point2 = points[j]
        return (minDistance, 
                point1, point2,
                totalOperation)

    else:
        mid = (len(points) // 2)
        leftPointsDist, leftPoint1, leftPoint2, totalOperation = divideAndConquer(points[:mid], totalOperation)
        rightPointsDist, rightPoint1, rightPoint2, totalOperation = divideAndConquer(points[mid:], totalOperation)
        if (leftPointsDist < rightPointsDist):
            minDistance = leftPointsDist
            point1 = leftPoint1
            point2 = leftPoint2
        else:
            minDistance = rightPointsDist
            point1 = rightPoint1
            point2 = rightPoint2

        midX = points[mid][0]
        minPoints = []
        for point in points:
            if (abs(point[0] - midX) < minDistance):
                minPoints.append(point)

        for i in range(len(minPoints)):
            for j in range(i+1, len(minPoints)):
                dis, totalOperation = dist.getDistance(minPoints[i], minPoints[j], totalOperation)
                if (dis < minDistance):
                    minDistance = dis
                    point1 = minPoints[i]
                    point2 = minPoints[j]
        
        return (minDistance, 
                point1, point2,
                totalOperation)
        