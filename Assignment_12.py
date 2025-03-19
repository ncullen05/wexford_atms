#Assignment 12
import matplotlib.pyplot as plt

inputlong = float(input("Please enter the longitude coordinates: "))
inputlat =  float(input("Please enter the latitude coordinates: "))

with open("ATMPoints.txt", "a") as f:
    f.write(f"{inputlong}, {inputlat}\n")

longitude = []
latitude = []
with open("ATMPoints.txt", "r") as file:
    for line in file:
        coords = line.strip().split(",")
        longitude.append(float(coords[0]))
        latitude.append(float(coords[1]))

BBox = [-6.4941, -6.4371, 52.3535, 52.3232]

fig, ax = plt.subplots(figsize = (8, 8))
ax.scatter(longitude, latitude, zorder = 1, alpha = 0.9, c = 'r', s = 30)
ax.set_xlim(BBox[0], BBox[1])
ax.set_ylim(BBox[2], BBox[3])
ax.set_title('Wexford ATMs')

img = plt.imread('Wexford.png')
ax.imshow(img, zorder = 0, extent = BBox, aspect = 'equal')

plt.show()