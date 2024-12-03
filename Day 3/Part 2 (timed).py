import re
def solution():
    with open("input.txt", "r") as f: sum(x for xs in [list(map(lambda x: int(x[0])*int(x[1]), x)) for x in [re.findall("mul\((\d+),(\d+)\)", x) for x in [x for xs in [re.split("(?=don?'?t?\(\))", "".join([lines.strip("\n") for lines in f]))] for x in xs] if not re.match("don't\(\).*", x)]] for x in xs)

import timeit
print(timeit.timeit(solution, number=1000)/1000)