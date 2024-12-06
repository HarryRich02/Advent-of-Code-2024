import copy

with open("input.txt", "r") as f:
    data = [list(lines.strip("\n")) for lines in f]

for i in range(len(data)):
    if "^" in data[i]:
        guard = [i, data[i].index("^")]
        break

guardStart = copy.deepcopy(guard)

direction = 0
positions = []
while guard[0]>=0 and guard[1]>=0:
    if direction == 0 and 0 <= guard[0]-1:
        if data[guard[0]-1][guard[1]] == "#":
            direction = (direction + 1)%4
        else:
            guard[0] -= 1
            if data[guard[0]][guard[1]] != "X":
                data[guard[0]][guard[1]] = "X"
                positions.append([guard[0], guard[1]])
    elif direction == 1 and guard[1]+1 < len(data[0]):
        if data[guard[0]][guard[1]+1] == "#":
            direction = (direction + 1)%4
        else:
            guard[1] += 1
            if data[guard[0]][guard[1]] != "X":
                data[guard[0]][guard[1]] = "X"
                positions.append([guard[0], guard[1]])
    elif direction == 2 and guard[0]+1 < len(data):
        if data[guard[0]+1][guard[1]] == "#":
            direction = (direction + 1)%4
        else:
            guard[0] += 1
            if data[guard[0]][guard[1]] != "X":
                data[guard[0]][guard[1]] = "X"
                positions.append([guard[0], guard[1]])
    elif direction == 3 and 0 <= guard[1]-1:
        if data[guard[0]][guard[1]-1] == "#":
            direction = (direction + 1)%4
        else:
            guard[1] -= 1
            if data[guard[0]][guard[1]] != "X":
                data[guard[0]][guard[1]] = "X"
                positions.append([guard[0], guard[1]])
    else:
        break

loops = 0
for i in range(len(positions)):
    data[positions[i][0]][positions[i][1]] = "#"
    loop = []
    guard = copy.deepcopy(guardStart)
    direction = 0

    while guard[0]>=0 and guard[1]>=0:
        if direction == 0 and 0 <= guard[0]-1:
            if data[guard[0]-1][guard[1]] == "#":
                direction = (direction + 1)%4
            else:
                guard[0] -= 1

        elif direction == 1 and guard[1]+1 < len(data[0]):
            if data[guard[0]][guard[1]+1] == "#":
                direction = (direction + 1)%4
            else:
                guard[1] += 1

        elif direction == 2 and guard[0]+1 < len(data):
            if data[guard[0]+1][guard[1]] == "#":
                direction = (direction + 1)%4
            else:
                guard[0] += 1

        elif direction == 3 and 0 <= guard[1]-1:
            if data[guard[0]][guard[1]-1] == "#":
                direction = (direction + 1)%4
            else:
                guard[1] -= 1

        else:
            break
        
        if [guard, direction] in loop:
            loops += 1
            break
        loop.append([copy.deepcopy(guard), copy.deepcopy(direction)])
    
    data[positions[i][0]][positions[i][1]] = "."
    print(i)

print(loops)