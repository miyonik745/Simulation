from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse


from .astar import astar


def index(request):
    context = {}
    return render(request, "simulation/index.html", context)

def createPath(request):
    start, goal = (1, 4), (9, 9)
    diagram5 = astar.GridWithWeights(10, 10)
    diagram5.walls = [(0,1),(0,2)]
    
    came_from, cost_so_far = astar.a_star_search(diagram5, start, goal)
    path = astar.reconstruct_path(came_from, start=start, goal=goal)
    print(path)


    return HttpResponse(JsonResponse({"path":path}))
