def read_file(filename):
    data=[]
    try:
        with open(filename, "r") as kateg_file:
            for _ in range(15):
                sor=kateg_file.readline().strip()
                data.append(sor)
            kateg_file.close()
    except:
        data=[]
    return data

data=read_file("foglaltsag.txt")
print(data)