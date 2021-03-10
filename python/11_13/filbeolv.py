def read_file(filename):
    data=[]
    try:
        with open(filename, "r") as ofile:
            for sor in ofile:
                data.append(sor.strip())
            ofile.close()
    except:
        print("A fajl nem talalható")
    return data


data=read_file("foglaltsg.txt")
print(data)
