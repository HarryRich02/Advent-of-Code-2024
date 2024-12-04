import re
with open("input.txt", "r") as f:
    data = f.readlines()

M_M = [[m.start(0) for m in re.finditer("(?=M.M)", x)] for x in data]
M_S = [[m.start(0) for m in re.finditer("(?=M.S)", x)] for x in data]
S_M = [[m.start(0) for m in re.finditer("(?=S.M)", x)] for x in data]
S_S = [[m.start(0) for m in re.finditer("(?=S.S)", x)] for x in data]

total = 0
for i in range(len(data)):
    for j in range(len(M_M[i])):
        try:
            if re.match(".A.", data[i+1][M_M[i][j]:M_M[i][j]+3]) and re.match("S.S", data[i+2][M_M[i][j]:M_M[i][j]+3]):
                total += 1
        except:
            pass
    for j in range(len(M_S[i])):
        try:
            if re.match(".A.", data[i+1][M_S[i][j]:M_S[i][j]+3]) and re.match("M.S", data[i+2][M_S[i][j]:M_S[i][j]+3]):
                total += 1
        except:
            pass
    for j in range(len(S_M[i])):
        try:
            if re.match(".A.", data[i+1][S_M[i][j]:S_M[i][j]+3]) and re.match("S.M", data[i+2][S_M[i][j]:S_M[i][j]+3]):
                total += 1
        except:
            pass
    for j in range(len(S_S[i])):
        try:
            if re.match(".A.", data[i+1][S_S[i][j]:S_S[i][j]+3]) and re.match("M.M", data[i+2][S_S[i][j]:S_S[i][j]+3]):
                total += 1
        except:
            pass

print(total)