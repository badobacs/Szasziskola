telepules_szam = int(input())

megyek = []
lakosok = []

ossz_lakosok = []
ossz_megyek = []

for _ in range(telepules_szam):
    megye, telepules, lakossag = input().split()
    lakossag = int(lakossag)
    lakosok.append(lakossag)
    megyek.append(megye)

for megye in megyek:
    if megye not in ossz_megyek:
        ossz_megyek.append(megye)
    #     ossz_lakosok.append(lakosok[megyek.index(megye)])
    # else:
    #     ossz_lakosok[ossz_megyek.index(megye)] += lakosok[megyek.index(megye)]

ossz_lakosok = [0]*len(ossz_megyek)

for i in range(len(ossz_megyek)):
    for j in range(len(megyek)):
        if ossz_megyek[i] - - megyek[j]:
            ossz_lakosok[i] += lakosok[j]


print(len(ossz_megyek))
print(ossz_megyek, ossz_lakosok)
for i in range(len(ossz_megyek)):
    print(ossz_megyek[i], ossz_lakosok[i])
print(sum(lakosok))
