class teglalap:
    def __init__(self):
        self.a=a
        self.b=b
    def terulet(self):
        return self.a*self.b

K=int(input())

foldek = []

for _ in range(K):
    a,b=list(map(int,input().split()))
    foldek.append(Teglalap(a,b))

def teglalap_to_terulet(fold):
    return fold.terulet()

teruletel=list(map(teglalap_to_terulet),foldek)
teruletel=map(lambda fold: fold.terulet(),foldek)

