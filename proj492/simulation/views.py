from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse

import os
import json


from .astar import astar


def index(request):
    context = {}
    return render(request, "simulation/index.html", context)

def createPath(request):
    dirname = os.path.dirname(__file__)

    start = request.POST.get('start','')
    destination = request.POST.get('destination','')

    print(start,destination)

    startList = start.split(",")
    destinationList = destination.split(",")
    
    startLat = float(startList[0])
    startLong = float(startList[1])
    destLat = float(destinationList[0])
    destLong = float(destinationList[1])
    

    referenceLat = 29.60664638126832
    referenceLong = -94.98276875969165
    diffLat = 0.0010201373003512
    diffLong = 0.0011693200529241



    def coordToPixel(coord, ref ,diff):
        pixel = int(abs(abs(ref) - abs(coord)) / diff)
        return pixel
     
    startY = coordToPixel(startLat, referenceLat, diffLat)
    startX = coordToPixel(startLong, referenceLong, diffLong)
    destY = coordToPixel(destLat, referenceLat, diffLat)
    destX = coordToPixel(destLong, referenceLong, diffLong)

    print(startX,startY)
    print(destX,destY)
    dataFileName = 'map6_data.json'
    dataFilePath = os.path.join(dirname, dataFileName)

    f = open(dataFilePath)
    data = json.load(f)

    walls,width,height = data.values()

    start, goal = (startX, startY), (destX, destY)
    diagram5 = astar.GridWithWeights(width, height)
    diagram5.walls = []

    for a in walls :
        diagram5.walls.append((a[0],a[1]))
    

    came_from, cost_so_far = astar.a_star_search(diagram5, start, goal)
    path = astar.reconstruct_path(came_from, start=start, goal=goal)

    currentLat = referenceLat
    currentLong = referenceLong

    tempList = []


    for a in path:
        currentLat -= diffLat * a[1]
        currentLong += diffLong * a[0]
        tempList2 = [currentLong, currentLat]

        tempList.append(tempList2)

        currentLat = referenceLat
        currentLong = referenceLong


 
 

    print("son")
    return HttpResponse(JsonResponse({"path":tempList,"pixelPath":path}))
