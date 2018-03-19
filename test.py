import copy

width = int(input("How wide?"))
height = int(input("How high?"))
grid = []
row = []
bak = "."
rows={}

for i in range(width):
    row.append(bak)
    
for i in range(height):
    row2 = copy.deepcopy(row)
    grid.append(row2)
    
while True:
    for i in range(len(grid)):
        print(grid[i])
    else:
        break