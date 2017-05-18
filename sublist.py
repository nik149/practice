a = [1,2,3,4]

mainset = []

for i in a:
    subset = []
    subset.append(a)
    for j in a[i+1:]:
        subset.append(j)
        mainset.append(subset)

print mainset
