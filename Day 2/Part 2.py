fList = open("test.txt").read().split("\n")
safe = 0
for i in range(len(fList)):
    line = fList[i].split()
    increasing = int(line[0]) < int(line[1])
    unsafe = 0
    for j in range(len(line)-1):
        if increasing:
            if int(line[j]) >= int(line[j+1]) or int(line[j+1]) - int(line[j]) > 3:
                unsafe += 1
        else:
            if int(line[j]) <= int(line[j+1]) or int(line[j]) - int(line[j+1]) > 3:
                unsafe += 1
        print(unsafe)
    if unsafe < 2:
        safe += 1
print(safe)