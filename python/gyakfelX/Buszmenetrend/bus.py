N = int(input())
x = 0
for i in range(N):
    varos, erkezes, indulas = input().split()

    if varos == "Szekszard" and erkezes == "-1":
        x += 1
    else:
        pass

if x:
    print("VAN")
else:
    print("NINCS")