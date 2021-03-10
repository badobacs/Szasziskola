datum, viz, telep, folyo=[],[],[],[],

with open("vizallas.txt", "r") as file:
    for sor in file:
       sor=sor.rstrip().split()
       datum.append(sor[0])
       viz.append(int(sor[1]))
       telep.append(sor[2])
       folyo.append(sor[3])
    #    akt=vizallas(sor[0], sor[1], sor[2]),

    #    vizallasok.append(akt)
    #    telepulesek
    #    viz.app
    print(len(set(telep)))
    legnagyobb_viz=max(viz)
    legnagyobb_viz_index=viz.index(legnagyobb_viz)
    print(f"{legnagyobb_viz}")

    for d in range(len(datumok)):
        if datumok[i]==datum:
            string=f"{datumok[i]}\y{viz[i]}"
            print(string)
            ofile.write(string)
