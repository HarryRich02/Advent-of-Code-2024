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

#print("antennae:", antennae)
nodes=[]
for x in antennae:
    for i in range(len(antennae[x])-1):
        A = np.array(antennae[x][i])
        #print("A:", A)
        for j in range(i+1, len(antennae[x])):
            B = np.array(antennae[x][j])
            #print("B:", B)
            AB = B-A
            #print("AB:", AB)
            point = A-AB
            #print("A-AB:", point)
            if 0<=point[0]<width and 0<=point[1]<height:
                nodes.append(point)
            '''point = A+(1/3)*AB
            if 0<=point[0]<width and point[0]==int(point[0]) and 0<=point[1]<height and point[1]==int(point[1]):
                nodes.append(point)
            point = A+(2/3)*AB
            if 0<=point[0]<width and point[0]==int(point[0]) and 0<=point[1]<height and point[1]==int(point[1]):
                nodes.append(point)'''
            point = A+2*AB
            #print("A+2AB:", point)
            if 0<=point[0]<width and 0<=point[1]<height:
                nodes.append(point)

'''data = [list(i for i in x) for x in data]
for i in range(len(nodes)):
    data[int(nodes[i][0])][int(nodes[i][1])] = "#"
print("data:")
for i in range(len(data)):
    print(data[i])'''
#print("nodes:", nodes)
print(len(set(tuple(x) for x in nodes)))