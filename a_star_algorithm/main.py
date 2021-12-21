from astar import *
import json
import time



start = time.time()

dirname = os.path.dirname(__file__)

dataFileName = 'map5_data.json'
dataFilePath = os.path.join(dirname, dataFileName)



f = open(dataFilePath)
data = json.load(f)

walls,width,height = data.values()
diagram5 = GridWithWeights(width, height)
start, goal = (190, 240), (236, 417)
diagram5.walls = []


for a in walls :
    diagram5.walls.append((a[0],a[1]))
    





came_from, cost_so_far = a_star_search(diagram5, start, goal)
draw_grid(diagram5, point_to=came_from, start=start, goal=goal)
path = reconstruct_path(came_from, start=start, goal=goal)
draw_grid(diagram5, path=path)
print(path)


end = time.time()
