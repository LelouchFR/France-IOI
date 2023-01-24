sortedMatters = []
for i in range(int(input())):
    matter = input()
    sortedMatters.append(matter)

sortedMatters.sort()
for sortedMatter in sortedMatters:
    print(sortedMatter)