import os

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path,file)):
            yield file


f=open("bg.txt","w")

for file in files("/Users/ηγηπ/Documents/NTUA/ΔΙΚΤΥΑ/NS22η Εργασία"):
    print(file)
    f.write(file)
    f.write("\n")


f.close()
