# Nama file     : main.py
# Fungsi        : Menjadi main dari program

import bruteForce as bf
import divideAndConquer as dc
import randomize as rand
import time
import plot

# Main program
def main():
    # Input
    while (True):
        print("\n=========================================")
        print("           Closest Pair Problem          ")
        print("=========================================")
        jumlahTitik = int(input ("Enter number of points    : "))
        dimensi = int(input     ("Enter dimension           : "))
        maxim = int(input       ("Enter maximum value       : "))
        minim = int(input       ("Enter minimum value       : "))
        if (maxim < minim):
            print("Maximum value must be greater than minimum value")
        elif (jumlahTitik < 2):
            print("Number of points must be greater than 1")
        elif (dimensi < 1):
            print ("Dimension must be greater than 0")
        else:
            print("Generating points...")
            break
    
    # Generate random points
    points = rand.randomizePoints(jumlahTitik, dimensi, maxim, minim)
    points.sort(key=lambda x: x[0])

    # Brute Force
    start = time.time()
    dist, (p1, p2), totalOperation = bf.bruteForce(points)
    end = time.time()
    
    # Print result
    print("\nBrute Force: ")
    print("     Distance            : ", round(dist,3))
    print("     Point 1             : ", p1)
    print("     Point 2             : ", p2)
    print("     Total Operation     : ", totalOperation)
    print("     Time                : ", round((end - start)*1000,4), "ms")
    
    # Divide and Conquer
    start = time.time()
    dist, p1, p2, totalOperation = dc.divideAndConquer(points, 0)
    end = time.time()
    
    # Print result
    print("\nDivide and Conquer : ")
    print("     Distance            : ", round(dist,3))
    print("     Point 1             : ", p1)
    print("     Point 2             : ", p2)
    print("     Total Operation     : ", totalOperation)
    print("     Time                : ", round((end - start)*1000,4), "ms")
    
    if (dimensi <= 3):
        plot.plot(points, p1, p2)
    else:
        print("\nPlotting is not available for dimension greater than 3")
        
if __name__ == '__main__':
    main()