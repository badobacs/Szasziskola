N = int(input())
elozo = 0
counter = 0
for i in range(N):
  bevetel = int(input())
  if bevetel > elozo:
    counter += 1
  elozo = bevetel
print(counter)
