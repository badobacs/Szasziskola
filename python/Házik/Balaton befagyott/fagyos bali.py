N = int(input())

jegvastag = []

for i in range(N):
    jegvastag.append(int(input()))
napok = 0

for x in range(len(jegvastag)):
    if jegvastag(x) > 0:
        napok = napok+1

print(napok)

