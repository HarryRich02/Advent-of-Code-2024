with open("input.txt", "r") as f:
    data = [list(lines.strip("\n")) for lines in f]

for i in range(len(data)):
    if "^" in data[i]:
        guard = [i, data[i].index("^")]
        break

data[guard[0]][guard[1]] = "X"

direction = 0
positions = 1
while guard[0]>=0 and guard[1]>=0:
    if direction == 0 and 0 <= guard[0]-1:
        if data[guard[0]-1][guard[1]] == "#":
            direction = (direction + 1)%4
        else:
            guard[0] -= 1
            if data[guard[0]][guard[1]] != "X":
                data[guard[0]][guard[1]] = "X"
                positions += 1
    elif direction == 1 and guard[1]+1 < len(data[0]):
        if data[guard[0]][guard[1]+1] == "#":
            direction = (direction + 1)%4
        else:
            guard[1] += 1
            if data[guard[0]][guard[1]] != "X":
                data[guard[0]][guard[1]] = "X"
                positions += 1
    elif direction == 2 and guard[0]+1 < len(data):
        if data[guard[0]+1][guard[1]] == "#":
            direction = (direction + 1)%4
        else:
            guard[0] += 1
            if data[guard[0]][guard[1]] != "X":
                data[guard[0]][guard[1]] = "X"
                positions += 1
    elif direction == 3 and 0 <= guard[1]-1:
        if data[guard[0]][guard[1]-1] == "#":
            direction = (direction + 1)%4
        else:
            guard[1] -= 1
            if data[guard[0]][guard[1]] != "X":
                data[guard[0]][guard[1]] = "X"
                positions += 1
    else:
        break
    
print(positions)