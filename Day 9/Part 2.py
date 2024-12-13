import copy

with open("Day 9/test.txt", "r") as f:
    diskMap = f.readline()

files = diskMap[0::2]
freeSpaces = diskMap[1::2]

disk = [0 for x in range(files[0])]
for i in range(1, len(files)):
    for j in range(len(files)-1, i):
        if freeSpaces[i-1] >= files[j]:
            for k in range(files[j]):
                disk.append(files[j])
            for k in range(freeSpaces[i-1]-files[j]):
                disk.append(None)

print(files)
print(freeSpaces)