N = int(input())
for _ in range(N):
    erosseg = int(input())
    if erosseg <= 50:
        print(0)
    elif erosseg > 90:
        print(45)
    else:
        print(int((erosseg-46)/5)*5)