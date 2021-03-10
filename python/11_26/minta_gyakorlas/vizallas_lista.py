datumok,  viz, telep, folyo=[],[],[],[]



with open("vizallas.txt","r") as file:
    for sor in file:
        sor=sor.strip().split()
        datumok.append(sor[0])
        viz.append(int(sor[1]))
        telep.append(sor[2])
        folyo.append(sor[3])


# print(datum)
# print(viz)
# print(telep)
# print(folyo)

print(len(set(telep)))

legnagyobb_viz=max(viz)
legnagyobb_viz_index=viz.index(legnagyobb_viz)
print(f"{legnagyobb_viz} a {folyo[legnagyobb_viz_index]}")


datum=input("Add meg a keresett evet: ").strip()

with open("ki2.txt", "w") as ofile:
    for i in range(len(datumok)):
        if datumok[i]==datum:
            string=f"{datumok[i]}\t{viz[i]}..\n"
            print(string)
            ofile.write(string)

