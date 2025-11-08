 

h2h_table=dict()

with open("/Users/kim-eunseo/Desktop/Digital/hw2/hanja2hangeul.txt") as fp:
    for line in fp:
        hanja,sound=line.split()
        h2h_table[hanja]=sound
with open("/Users/kim-eunseo/Desktop/Digital/hw2/hanja2hangeul_table.py","wt") as fp:
    print("hanja2hangeul_table =",str(h2h_table).replace(", ",",\n"),file=fp)