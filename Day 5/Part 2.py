import re

with open("input.txt", "r") as f:
    data = [lines.strip("\n").split("|") for lines in f]
rules = data[:data.index([''])]
pages = [x for xs in data[data.index([''])+1:] for x in xs]

regex = re.compile("|".join([".*".join(x[::-1]) for x in rules]))

wrongPages = []
for i in range(len(pages)):
    if re.search(regex, pages[i]):
        wrongPages.append(pages[i])

wrongPages = [x.split(",") for x in wrongPages]
total = 0
for i in range(len(wrongPages)):
    rules = data[:data.index([''])]

    j = 0
    while j < len(rules):
        if not ((rules[j][0] in wrongPages[i]) and (rules[j][1] in wrongPages[i])):
            rules.pop(j)
        else:
            j += 1
    
    rules = [[x[0] for x in rules], [x[1] for x in rules]]
    sorted = []
    values = set(wrongPages[i])
    while len(sorted) != len(wrongPages[i]):
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
    total += int(sorted[len(sorted)//2])

print(total)