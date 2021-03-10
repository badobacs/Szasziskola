bemenet = input().split(" ")
napok_szama, szel_hatar = int(bemenet[0]), int(bemenet[1])

counter = 0

for _ in range(napok_szama):
    szel_sebesseg = int(input())
    if szel_sebesseg < szel_hatar and szel_sebesseg > 0:
        counter += 1
print(counter)
