import re
import copy
import itertools
with open("input.txt", "r") as f:
    data = f.readlines()

total = 0
total += len([x for xs in [re.findall("XMAS", x) for x in data] for x in xs])
total += len([x for xs in [re.findall("SAMX", x) for x in data] for x in xs])
total += len([x for xs in [re.findall("XMAS", x) for x in ["".join(x) for x in zip(*data)]] for x in xs])
total += len([x for xs in [re.findall("SAMX", x) for x in ["".join(x) for x in zip(*data)]] for x in xs])

lData = copy.deepcopy(data)
rData = copy.deepcopy(data)
for i in range(len(data)):
    for j in range(i):
        lData[i] = "Q" + lData[i]
    for j in range(len(data)-i):
        rData[i] = "Q" + rData[i]

total += len([x for xs in [re.findall("XMAS", x) for x in ["".join(x) for x in itertools.zip_longest(*lData, fillvalue = "Q")]] for x in xs])
total += len([x for xs in [re.findall("SAMX", x) for x in ["".join(x) for x in itertools.zip_longest(*lData, fillvalue = "Q")]] for x in xs])
total += len([x for xs in [re.findall("XMAS", x) for x in ["".join(x) for x in itertools.zip_longest(*rData, fillvalue = "Q")]] for x in xs])
total += len([x for xs in [re.findall("SAMX", x) for x in ["".join(x) for x in itertools.zip_longest(*rData, fillvalue = "Q")]] for x in xs])

print(total)