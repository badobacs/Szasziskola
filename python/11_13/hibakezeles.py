def szam_beolvasas1():
    while True:
        try:
            a = int(input())
            break
        except Exception as e:
            print("Nem szamot adtal meg")


def szam_beolvasas(min,max):
    sikeres=False
    while not sikeres:
        try:
            a=int(input())
            sikeres=a<=max and a>=min
            if not sikeres:
                print(f"{max} nál kisebb szám kell, és {min} nél nagyobb")
        except Exception as e:
            print("Nem szamot adtal meg")
            print(e)
    return a

a=szam_beolvasas(2,500)

print(a)
print("Hello")
