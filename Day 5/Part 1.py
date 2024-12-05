import re

with open("input.txt", "r") as f:
    data = [lines.strip("\n").split("|") for lines in f]
rules = data[:data.index([''])]
pages = [x for xs in data[data.index([''])+1:] for x in xs]

regex = re.compile("|".join([".*".join(x[::-1]) for x in rules]))

total = 0
for i in range(len(pages)):
    if not re.search(regex, pages[i]):
        pages[i] = pages[i].split(",")
        total += int(pages[i][len(pages[i])//2])

print(total)