ketto_hatvanyok=[]

for i in range(20):
    ketto_hatvanyok.append(2**i)

ketto_hatvanyok2=[2**i for i in range(20)]

print(ketto_hatvanyok)
print(ketto_hatvanyok2)

lista0=[0]*5

print(lista0)
lista0[2]+=1
print(lista0)


# Ez nem működik
# matrix=[[0]*5]*5
# print(matrix)
# matrix[0][0]=1
# print(matrix)

matrix=[[0]*5 for i in range(5)]
print(matrix)
matrix[0][0]=1
print(matrix)


