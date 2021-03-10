N = int(input())
jegvastagsag = []
for i in range(N):
    jegvastagsag.append(int(input()))

napok = 0

for x in range(len(jegvastagsag)):
    if jegvastagsag[x] > 0:
        napok = napok + 1


print(napok)
