with open("input.txt", "r") as f:
    data = [list(map(int, x)) for x in [line.strip().split(" ") for line in f]]

total = 0

for i in range(len(data)):
    print(data[i]) #@@@REMOVE

    safe = True

    dampener = False
    for k in range(2):
        increasing = data[i][0] < data[i][1]

        for j in range(len(data[i])-1):
            if increasing:
                if data[i][j] >= data[i][j+1] or data[i][j+1] - data[i][j] > 3:
                    if dampener:
                        safe = False
                    else:
                        data[i].pop(j+1)
                        dampener = True
                        break
            else:
                if data[i][j] <= data[i][j+1] or data[i][j] - data[i][j+1] > 3:
                    if dampener:
                        safe = False
                    else:
                        data[i].pop(j+1)
                        dampener = True
                        break
    
    print(safe)
    input()

    if safe:
        total += 1

print(total)