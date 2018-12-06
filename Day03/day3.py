input = 368078

test = False

if test:
    input = 1024

def distance(loc1, loc2):
    return abs(loc2[0] - loc1[0]) + abs(loc2[1] - loc1[1])

def grid_location(locs, num):
    return [[e[0], e[1]] for e in locs if num == e[2]][0]

def locs(inp, typ):
    x = 0
    y = 0
    direction = 'right'
    locations = []
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0
    for i in range(1, input+1):
        if i == 1 or typ == 'a':
            num = i
        else:
            num = sum([l[2] for l in locations if abs(l[0]-x) < 2 and abs(l[1] - y) < 2])
        if num > input:
            break
        locations.append([x,y,num])
        print(num)
        if direction == 'right':
            x += 1
            if x > max_x:
                max_x += 1
                direction = 'up'
        elif direction =='up':
            y -= 1
            if y < min_y:
                min_y -= 1
                direction = 'left'
        elif direction =='left':
            x -= 1
            if x < min_x:
                min_x -= 1
                direction = 'down'
        elif direction =='down':
            y += 1
            if y > max_y:
                max_y += 1
                direction = 'right'
    if typ == 'b':
        return num
    if typ == 'a':
        return locations

a_locs = locs(input, 'a')

input_loc = grid_location(a_locs, input)
one_loc = grid_location(a_locs, 1)
input_dist = distance(input_loc, one_loc)

print('a', input_dist)
print('b', locs(input, 'b'))