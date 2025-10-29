list=['a', 'b', 2, 4, 2, 'c', 'j', 1, 'b', 'd', 'c', 4, 1]
filterlist=[]

for filter in list:
    if filter not in filterlist:
        filterlist.append(filter)
print(filterlist)
    