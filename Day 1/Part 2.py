nums1 = []
nums2 = []
total = 0

fList = open("input.txt").read().split('\n')
for i in range(len(fList)):
    line = fList[i].split("   ")
    nums1.append(int(line[0]))
    nums2.append(int(line[1]))
for i in range(len(nums1)):
    total += abs(nums1[i]*nums2.count(nums1[i]))

print(total)