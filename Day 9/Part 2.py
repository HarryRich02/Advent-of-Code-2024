import copy

with open("Day 9/input.txt", "r") as f:
    diskMap = f.readline()

disk = []
for i in range(len(diskMap)):
    if i%2 == 0:
        disk.append([int(i/2), int(diskMap[i])])
    else:
        disk.append([None, int(diskMap[i])])

for i in range(len(disk)-1, -1, -1):
    if disk[i][0] != None:
        for j in range(i):
            if disk[j][0] == None and disk[j][1] >= disk[i][1]:
                disk[j][1] -= disk[i][1]
                insert = copy.deepcopy(disk[i])
                disk.insert(j, insert)
                disk[i+1][0] = None
                break
    print(i)

position = 0
total = 0
for i in range(len(disk)):
    for j in range(disk[i][1]):
        try:
            total += disk[i][0]*position
        except:
            pass
        position += 1

print(total)