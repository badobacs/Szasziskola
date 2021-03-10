N = (int(input))
eso = []
for i in range(N):
    eso.append(int(input))

nap = 0
for x in eso:
    if x > 0:
        nap += 1
print(nap)
