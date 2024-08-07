from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import csv

img = Image.open("cropped.png")

arr = np.array(img)
arr = np.sum(arr,axis=2)

arr = arr[:250,:370]

#plt.imshow(arr)
#plt.show()

lines = []
for row in arr:
	line = [str(x) for x in row]
	lines.append(line)

with open('SAR_image.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(lines)



