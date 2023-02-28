# Nama file     : plot.py
# Fungsi        : Membuat plot dari titik-titik yang ada

import matplotlib.pyplot as plt

# Plot the points and the line between p1 and p2
def plot(points, p1, p2):
    x = []
    y = []
    z = []
    for point in points:
        if (point != p1 and point != p2):
            x.append(point[0])
            if (len(point) > 1):
                y.append(point[1])
                if (len(point) == 3):
                    z.append(point[2])
    if (len(point) == 3):
        ax = plt.axes(projection ='3d')
        ax.scatter(x, y, z, color='black')
        ax.set_title('3D Plot')
        plt.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], color='red')
        ax.scatter(p1[0], p1[1], p1[2], color='red')
        ax.scatter(p2[0], p2[1], p2[2], color='red')
    elif (len(point) == 2):
        plt.scatter(x, y, color='black')
        plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color='red')
        plt.scatter(p1[0], p1[1], color='red')
        plt.scatter(p2[0], p2[1], color='red')
    else: # len(point) == 1
        plt.scatter(x, [0 for i in x], color = 'black')
        plt.scatter(p1[0], 0, color = 'red')
        plt.scatter(p2[0], 0, color = 'red')
        plt.plot([p1[0], p2[0]], [0, 0], color = 'red')
    plt.show()
    
