list1 = []
list2 = []
mergedlist = list1 + list2
noduplicateslist = []

for a in mergedlist:
    if a not in noduplicateslist:
        noduplicateslist.append(a)

print (str(noduplicateslist))