from PIL import Image
from numpy import asarray
import os
import json
from math import sqrt


dirname = os.path.dirname(__file__)

class ImageConverter:
    def __init__(self,imageName) :

        self.imagePath = os.path.join(dirname, f'map_images\\{imageName}')
        print(self.imagePath)
        self.mapImage = Image.open(self.imagePath)
        self.width, self.height= self.mapImage.size
        self.mapImageRGB = self.mapImage.convert("RGB")
        self.mapVisualText = ""
        self.wallList = []
    
        
        self.createWallMatrix()


    def createWallMatrix(self):
        wallMatrix = []
        for a in range(self.width):
            print(int((a/self.height)*100))
            tempList = []
            for b in range(self.width):
                rgb_pixel_value = self.mapImageRGB.getpixel((b,a))

                if(str(rgb_pixel_value) != '(214, 216, 221)'):
                    tempList.append("1")

                else:
                    tempList.append("0")
            wallMatrix.append(tempList)

        self.generateImageData(wallMatrix)

    def generateImageData(self,matrix):
        mapVisualText = ""
        wallList = []
        

        for count,a in enumerate(matrix):
            mapVisualText += "\n"
            for count2,b in enumerate(a):
                if(b == "1"):
                    wallList.append([count2,count])
                mapVisualText += str(b)
        
        self.mapVisualText = mapVisualText
        self.wallList = wallList



    def createJsonFile(self,fileName):
        data = {
            "walls":self.wallList,
            "width":self.width,
            "height":self.height
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









imageName = "map5"
imageExtensionName =  imageName + ".png"
mapVisualName = os.path.join(dirname, f'map_data\\{imageName}_visual.txt')
mapDataName =  os.path.join(dirname, f'map_data\\{imageName}_data.json')

imageConverter = ImageConverter(imageExtensionName)
imageConverter.createJsonFile(mapDataName)
imageConverter.createVisualTextFile(mapVisualName)


        




