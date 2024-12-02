fList = open("input.txt").read().split("\n")
safe = 0
for i in range(len(fList)):
    line = fList[i].split()
    increasing = int(line[0]) < int(line[1])
    unsafe = False
    for j in range(len(line)-1):
        if increasing:
            unsafe = unsafe or (int(line[j]) >= int(line[j+1]) or int(line[j+1]) - int(line[j]) > 3)
        else:
            unsafe = unsafe or (int(line[j]) <= int(line[j+1]) or int(line[j]) - int(line[j+1]) > 3)
    if not unsafe:
        safe += 1
print(safe)