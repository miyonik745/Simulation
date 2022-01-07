from astar import *
import json
import time


dirname = os.path.dirname(__file__)

dataFileName = 'map6_data.json'
dataFilePath = os.path.join(dirname, dataFileName)



f = open(dataFilePath)
data = json.load(f)

walls,width,height = data.values()
diagram5 = GridWithWeights(width, height)
start, goal = (199, 7), (61, 146)
diagram5.walls = []


for a in walls :
    diagram5.walls.append((a[0],a[1]))
    





came_from, cost_so_far = a_star_search(diagram5, start, goal)
draw_grid(diagram5, point_to=came_from, start=start, goal=goal)
path = reconstruct_path(came_from, start=start, goal=goal)
draw_grid(diagram5, path=path)
print(path)



tempDict = {
    "path": path
}

# for a in path:
#     text += f"({a[0]},{a[1]}),"


        

with open(os.path.join(dirname, "astar_path.json"), 'w') as f:
        json.dump(tempDict, f)

# with open(os.path.join(dirname, "astar_path.txt"), 'w') as f:
#         f.write(text) 


