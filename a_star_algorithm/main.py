from astar import *
import json
import time



start = time.time()



f = open('map5.png_data.json')
data = json.load(f)

walls,width,height = data.values()
diagram5 = GridWithWeights(width, height)
start, goal = (4, 57), (295, 280)
diagram5.walls = []


for a in walls :
    diagram5.walls.append((a[0],a[1]))
    





came_from, cost_so_far = a_star_search(diagram5, start, goal)
print(reconstruct_path(came_from, start=start, goal=goal))
draw_grid(diagram5, point_to=came_from, start=start, goal=goal)
draw_grid(diagram5, path=reconstruct_path(came_from, start=start, goal=goal))


end = time.time()
