import copy

with open("input.txt", "r") as f:
    data = [list(map(int, x)) for x in [line.strip().split(" ") for line in f]]

total = 0

for i in range(len(data)):
    for j in range(len(data[i])+1):
        safe = True

        if j >= len(data[i]):
            tempData = data[i]
        else:
            tempData = copy.deepcopy(data[i])
            tempData.pop(j)

        increasing = tempData[0] < tempData[1]

        for k in range(len(tempData)-1):
            if increasing:
                if not (-1 >= tempData[k] - tempData[k+1] >= -3):
                    safe = False
                    break
            else:
                if not (1 <= tempData[k] - tempData[k+1] <= 3):
                    safe = False
                    break
        
        if safe:
            total += 1
            break

                


print(total)