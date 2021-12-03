from PIL import Image
from numpy import asarray
import os

# print(data)
sea = 0
land = 0
other = 0
count = 0


width = 1208
height = 773

        
matrix = []

red_image = Image.open("map4.png")
red_image_rgb = red_image.convert("RGB")
for a in range(width):
    print((a/width)*100)
    tempList = []
    for b in range(height):


        count += 1
        
        rgb_pixel_value = red_image_rgb.getpixel((a,b))
        # print(str(rgb_pixel_value))



        if(str(rgb_pixel_value) == '(214, 216, 221)'):
            land+=1
            tempList.append("0")

        else:
            sea+=1
            tempList.append("1")

    matrix.append(tempList)

print(sea,land,other, count)
print(matrix)


tempText = ""

text2 = "["

for count,a in enumerate(matrix):
    tempText += "\n"
    for count2,b in enumerate(a):
        if(b == "0"):
            text2 += f"({count2},{count}),"
        tempText += str(b)
text2 += "]"
print(tempText)
print(text2)

os.remove("mapWalls.txt")
with open('mapWalls.txt', 'w') as f:
    f.write(tempText) 

os.remove("walls.txt")
with open('walls.txt', 'w') as f:
    f.write(text2) 


