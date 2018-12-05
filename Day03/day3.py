input = 368078
input = 11

grid = []
max_width = 0
max_height = 0
for i in range(1, input+1):
    if i == 1:
        direction = 'right'
        y = 0
        grid.insert(y,[i])
        max_width = len(grid[y])
    elif direction == 'right':
        grid[y].append(i)
        if len(grid[y]) > max_width:
            direction = 'up'
            max_width = len(grid[y])
            y -= 1
    elif direction == 'up':
        if y < 0:
            grid.insert(0, [i])
            direction = 'left'
            y = 0
        else: 
            grid[y].append(i)
            y -= 1
    elif direction == 'left':
        grid[y].insert(0, i)
        if len(grid[y]) > max_width:
            direction = 'down'
            max_width = len(grid[y])
            y += 1
            print('asdf')
    elif direction == 'down':
        if y == len(grid):
            grid.append([i])
            direction = 'right'
        else:
            grid[y].insert(0, i)
            y += 1

#normalize grid
if direction == 'left' and len(grid[0]) < len(grid[1]):
    grid[0][0:0] = [0] * (len(grid[1]) - len(grid[0]))

if direction == 'down':
    for i in range(1, len(grid)):
        if len(grid[i]) < len(grid[i-1]):
            grid[i].insert(0, 0)

if direction == 'right' and len(grid[len(grid)-1]) < len(grid[len(grid)-2]):
    grid[len(grid)-1].extend([0]*(len(grid[len(grid)-2]) - len(grid[len(grid)-1])))

if direction == 'up':
    for i in range(len(grid)-1, 0, -1):
        if len(grid[i]) > len(grid[i-1]):
            grid[i-1].append(0)
    

breakpoint()
distance = 0
print('a', distance)