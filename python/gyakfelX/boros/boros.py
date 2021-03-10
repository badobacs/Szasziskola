evek_szama = int(input())

arak = []

for _ in range(evek_szama):
    mennyiseg, ar = input().split(" ")
    ar = int(ar)
    # print(ar)
    arak.append(ar)

# print(arak)

duplicates = set()

for i in arak:
    if i not in duplicates:
        duplicates.add(i)

print(len(duplicates))