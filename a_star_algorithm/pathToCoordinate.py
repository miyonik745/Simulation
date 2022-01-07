import json
import os

dirname = os.path.dirname(__file__)

dataFileName = 'astar_path.json'
dataFilePath = os.path.join(dirname, dataFileName)
f = open(dataFilePath)
data = json.load(f)
path = data["path"]

# print(path)


startLat = 29.60664638126832
startLong = -94.98276875969165
diffLat = 0.0010201373003512
diffLong = 0.0011693200529241


currentLat = startLat
currentLong = startLong



tempList = []


for a in path:
    currentLat -= diffLat * a[1]
    currentLong += diffLong * a[0]
    tempList2 = [currentLong, currentLat]

    tempList.append(tempList2)

    currentLat = startLat
    currentLong = startLong


tempDict = {
    "pathCoord": tempList
}


with open(os.path.join(dirname, "astar_path_coord.json"), 'w') as f:
        json.dump(tempDict, f)





# for a in path:
#     old
