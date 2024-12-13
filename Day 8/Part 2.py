import copy
import numpy as np
import re

with open("Day 8/input.txt", "r") as f:
    data = [line.strip("\n") for line in f]

width = len(data[0])
height = len(data)

antennae = {x:[] for x in set([x for xs in [set(x) for x in data] for x in xs])-set(".")}
for x in antennae:
    for j in range(len(data)):
        antennae[x].extend([[m.start(), j] for m in re.finditer(x, data[j])])

nodes=[]
for x in antennae:
    for i in range(len(antennae[x])-1):
        A = np.array(antennae[x][i])
        for j in range(i+1, len(antennae[x])):
            B = np.array(antennae[x][j])
            AB = B-A
            AB = AB/(np.gcd.reduce(AB))
            AB = AB.astype(int)
            point = copy.deepcopy(A)
            while 0<=point[0]<width and 0<=point[1]<height:
                value = copy.deepcopy(point)
                nodes.append(value)
                point -= AB
            point = copy.deepcopy(A)
            while 0<=point[0]<width and 0<=point[1]<height:
                value = copy.deepcopy(point)
                nodes.append(value)
                point += AB

print(len(set(tuple(x) for x in nodes)))