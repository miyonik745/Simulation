from PIL import Image
from numpy import asarray
import os



imageName =  "map4" + ".png"

imagePath = "map_images/" + imageName


mapImage = Image.open(imagePath)
width, height= mapImage.size
mapImageRGB = mapImage.convert("RGB")


        
matrix = []


for a in range(width):
    print((a/width)*100)
    tempList = []
    for b in range(height):
        rgb_pixel_value = mapImageRGB.getpixel((a,b))

        if(str(rgb_pixel_value) == '(214, 216, 221)'):
            tempList.append("0")

        else:
            tempList.append("1")

    matrix.append(tempList)



mapVisualText = ""

mapDataText = "["

for count,a in enumerate(matrix):
    mapVisualText += "\n"
    for count2,b in enumerate(a):
        if(b == "0"):
            mapDataText += f"({count2},{count}),"
        mapVisualText += str(b)
mapDataText += "]"
# print(mapVisualText)
# print(mapDataText)

mapVisualName = "mapData/" + imageName + "_visual.txt"
mapDataName =  "mapData/" +imageName + "_data.txt"

print(mapVisualName)


try:
    os.remove(mapVisualName)
except:
    pass
with open(mapVisualName,  "w+") as f:
    f.write(mapVisualText) 

try:
    os.remove(mapDataName)
except:
    pass
with open(mapDataName , 'w+') as f:
    f.write(mapDataText) 


