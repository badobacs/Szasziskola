# Kiíráshoz print függvény
# Szöveg literál "" közt
print("hello")

# Egyszerű matematikai műveletek működnek
print(5*5)
print(5/2)
# a % a moduló operátor.
# Maradékos osztásnál a maradékot adja meg
print(5 % 2)

# változó
# Nem matematikai =
# Fontos, hogy a változó neve van a bal oldalon
eletkor = 25

# 25 = eletkor hibás kifejezls

# Változó innentől a kapott értéket tartlmazza
print(eletkor)

# Lehet szöveget is változóban tárolni
nev = "Dezső"

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# Pythonban a szám és szöveg összeabása hejtelen
# print(25+"Dezső")

# Type konverzió
# Az str függvény megpróbál az eletkorbol stringet csinálni
# Így már összeadható
print("Dezső " + str(eletkor))
print(nev+" " + str(eletkor))
