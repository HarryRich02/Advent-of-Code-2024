import re
with open("input.txt", "r") as f:
    print(sum(x for xs in [list(map(lambda x: int(x[0])*int(x[1]), x)) for x in [re.findall("mul\((\d+),(\d+)\)", line) for line in f]] for x in xs))