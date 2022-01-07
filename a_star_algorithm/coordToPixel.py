import json
import os


startLat = 29.550028321321335
startLong = -94.79060658285145

endLat = 29.6900759724104
endLong = -94.81751525878948






referenceLat = 29.60664638126832
referenceLong = -94.98276875969165
diffLat = 0.0010201373003512
diffLong = 0.0011693200529241



def function1(coord, ref ,diff):
    pixel = abs(abs(ref) - abs(coord)) / diff
    print(pixel)
    return pixel
     
y = function1(startLat, referenceLat, diffLat)
x = function1(startLong, referenceLong, diffLong)

