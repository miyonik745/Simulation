from PIL import Image
from numpy import asarray

# print(data)
sea = 0
land = 0
other = 0
count = 0

matrix = []
red_image = Image.open("map3.png")
for a in range(1208):
    print((a/1208)*100)
    tempList = []
    for b in range(773):


        count += 1
        
        red_image_rgb = red_image.convert("RGB")
        rgb_pixel_value = red_image_rgb.getpixel((a,b))
        # print(str(rgb_pixel_value))



        if(str(rgb_pixel_value) == '(214, 216, 221)'):
            land+=1
            tempList.append(0)

        else:
            sea+=1
            tempList.append(1)

    matrix.append(tempList)

print(sea,land,other, count)
print(matrix)


tempText = ""

for a in matrix:
    tempText += "\n"
    for b in a:
        tempText += str(b)

print(tempText)

with open('readme.txt', 'w') as f:
    f.write(tempText) 