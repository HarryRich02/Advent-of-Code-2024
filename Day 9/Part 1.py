import copy

with open("Day 9/input.txt", "r") as f:
    diskMap = f.readline()

disk = []
for i in range(len(diskMap)):
    for j in range(int(diskMap[i])):
        if i%2==0:
            disk.append(int(i/2))
        else:
            disk.append(None)

freeSpace = 0
end = len(disk)-1
while freeSpace < end:
    while disk[freeSpace] != None:
        freeSpace += 1
    while disk[end] == None:
        end -= 1
    disk[freeSpace] = copy.deepcopy(disk[end])
    disk[end] = None
disk[end] = copy.deepcopy(disk[freeSpace])
disk[freeSpace] = None

i = 0
total = 0
while disk[i] != None:
    total += i*disk[i]
    i += 1

print(total)