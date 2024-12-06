with open("input.txt", "r") as f:
    data = [list(lines.strip("\n")) for lines in f]

for i in range(len(data)):
    if "^" in data[i]:
        guard = [i, data[i].index("^")]
        break

import copy
start = copy.deepcopy(guard)

data[guard[0]][guard[1]] = "X"

direction = 0
positions = 1
while guard[0]>=0 and guard[1]>=0:
    if direction == 0:
        try:
            if data[guard[0]-1][guard[1]] != "#":
                guard[0] -= 1
                if data[guard[0]][guard[1]] != "X":
                    positions += 1
                    data[guard[0]][guard[1]] = "X"
            else:
                direction = (direction + 1)%4
        except:
            print("break")
            break
    elif direction == 1:
        try:
            if data[guard[0]][guard[1]+1] != "#":
                guard[1] += 1
                if data[guard[0]][guard[1]] != "X":
                    positions += 1
                    data[guard[0]][guard[1]] = "X"
            else:
                direction = (direction + 1)%4
        except:
            print("break")
            break
    elif direction == 2:
        try:
            if data[guard[0]+1][guard[1]] != "#":
                guard[0] += 1
                if data[guard[0]][guard[1]] != "X":
                    positions += 1
                    data[guard[0]][guard[1]] = "X"
            else:
                direction = (direction + 1)%4
        except:
            print("break")
            break
    elif direction == 3:
        try:
            if data[guard[0]][guard[1]-1] != "#":
                guard[1] -= 1
                if data[guard[0]][guard[1]] != "X":
                    positions += 1
                    data[guard[0]][guard[1]] = "X"
            else:
                direction = (direction + 1)%4
        except:
            print("break")
            break
    print("loop")

data[start[0]][start[1]] = "^"
with open("output.txt", "w") as f:
    for lines in data:
        f.write("%s\n" % lines)
print(start)
print(guard)

print(positions)