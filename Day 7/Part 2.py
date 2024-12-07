#===FUNCTIONS===
def trySolve(line, i, total):
    #===BASE-CASE===
    if i == len(line[1])-1:
        if total + line[1][i] == line[0]:
            return True
        elif total * line[1][i] == line[0]:
            return True
        elif int(str(total) + str(line[1][i])) == line[0]:
            return True
        else:
            return False
    
    #===RECURSION===
    if total + line[1][i] <= line[0]:
        if trySolve(line, i+1, total+line[1][i]):
            return True
    if total * line[1][i] <= line[0]:
        if trySolve(line, i+1, total*line[1][i]):
            return True
    if int(str(total) + str(line[1][i])) <= line[0]:
        if trySolve(line, i+1, int(str(total) + str(line[1][i]))):
            return True
    
    #===ELSE===
    return False

#===FILE-HANDLING===
with open("input.txt", "r") as f:
    data = [[int(x[0]), [int(y) for y in x[1].split()]] for x in [lines.strip("\n").split(":") for lines in f]]

#===MAIN===
total = 0
for i in range(len(data)):
    if trySolve(data[i], 1, data[i][1][0]):
        total += data[i][0]
    print(i)

#===OUTPUT===
print(total)