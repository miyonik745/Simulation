from PIL import Image
from numpy import asarray
import os
import json




class ImageConverter:
    def __init__(self,imageName) :
        self.imagePath = "map_images/" + imageName
        self.mapImage = Image.open(self.imagePath)
        self.width, self.height= self.mapImage.size
        self.mapImageRGB = self.mapImage.convert("RGB")
        self.mapVisualText = ""
        self.wallList = []
    
        
        self.createWallMatrix()


    def createWallMatrix(self):
        wallMatrix = []
        for a in range(self.width):
            print(int((a/self.width)*100))
            tempList = []
            for b in range(self.height):
                rgb_pixel_value = self.mapImageRGB.getpixel((a,b))

                if(str(rgb_pixel_value) == '(214, 216, 221)'):
                    tempList.append("0")

                else:
                    tempList.append("1")
            wallMatrix.append(tempList)

        self.generateImageData(wallMatrix)

    def generateImageData(self,matrix):
        mapVisualText = ""
        wallList = []
        

        for count,a in enumerate(matrix):
            mapVisualText += "\n"
            for count2,b in enumerate(a):
                if(b == "0"):
                    wallList.append([count2,count])
                mapVisualText += str(b)
        
        self.mapVisualText = mapVisualText
        self.wallList = wallList



    def createJsonFile(self,fileName):
        data = {
            "walls":self.wallList,
            "width":self.width,
            "heigh":self.height
        }


        try:
            os.remove(fileName)
        except:
            pass
        with open(fileName, 'w') as f:
            json.dump(data, f)

    def createVisualTextFile(self,fileName):
        try:
            os.remove(fileName)
        except:
            pass
        with open(fileName,  "w+") as f:
            f.write(self.mapVisualText) 











imageName =  "map4" + ".png"
mapVisualName = "map_data/" + imageName + "_visual.txt"
mapDataName =  "map_data/" +imageName + "_data.json"

imageConverter = ImageConverter(imageName)
imageConverter.createJsonFile(mapDataName)
imageConverter.createVisualTextFile(mapVisualName)


        




