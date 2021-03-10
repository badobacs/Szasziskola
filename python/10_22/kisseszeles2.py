N, M, K, = list(map(int, input()))
napok = []

for i in range(N):
    a = int(input())
    napok.append(a)

mo=filter(lambda a: 0<a and a<M, napok)
#print(list(mo))

megoldas = len(list(mo))
print(megoldas)