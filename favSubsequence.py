def sublists(l):
        return [l[m:n+1] for m in range(0,len(l)) for n in range(m,len(l))]

S = "cacaabc"

na = [i for i in range(0, len(S)) if S[i] == 'a']
nb = [i for i in range(0, len(S)) if S[i] == 'b']
nc = [i for i in range(0, len(S)) if S[i] == 'c']

count = 0
naa = sublists(na)
nbb = sublists(nb)
ncc = sublists(nc)
print "na"
print naa
count = 0
sets = []
for ela in naa:
    for elb in nbb:
        for elc in ncc:
                if ela[-1]<elb[0] and elb[-1] < elc[0]:
                        count+= 1
                        sets.append(ela + elb + elc)

print count
print sets
