import re

with open("test.txt", "r") as f:
    data = [lines.strip("\n").split("|") for lines in f]
rules = data[:data.index([''])]
pages = [x for xs in data[data.index([''])+1:] for x in xs]

regex = re.compile("|".join([".*".join(x[::-1]) for x in rules]))

wrongPages = []
for i in range(len(pages)):
    if re.search(regex, pages[i]):
        wrongPages.append(pages[i])

values = set([x for xs in [x.split(",") for x in pages] for x in xs])
rules = [[x[0] for x in rules], [x[1] for x in rules]]

sorted = []
while len(sorted) != len(values):
    try:
        nextPage = list(values - set(rules[1]))[0]
    except:
        break
    sorted.append(nextPage)
    while nextPage in rules[0]:
        index = rules[0].index(nextPage)
        rules[0].pop(index)
        rules[1].pop(index)
    values.remove(nextPage)

total = 0
wrongPages = [x.split(",") for x in wrongPages]
for i in range(len(wrongPages)):
    sortedPage = []
    for j in range(len(sorted)):
        if sorted[j] in wrongPages[i]:
            sortedPage.append(sorted[j])
    try:
        total += int(sortedPage[len(sortedPage)//2])
    except:
        pass

print(total)