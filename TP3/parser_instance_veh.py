import numpy as np

def parser(filename):
    fic = open(filename, "r")
    lines = fic.readlines()[4:]
    infos = np.zeros((len(lines), 2))
    i = 0
    lines[-1] = lines[-1][:-2]
    for line in lines:
        s = line.split("\t")
        infos[i,0] = int(s[0])
        s = s[1].split("\n")
        try:
            infos[i,1] = int(s[0])
        except:
            print(s[0])
            infos[i,1] = int(s[0][:-1])
        i += 1
    return infos
