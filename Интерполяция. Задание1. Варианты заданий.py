import random as rd
for j in range(1, 20):       # цикл [0, 9]
    y = []  # пустой массив
    for i in range(0, 8):       # цикл [0, 9]
        a = rd.randrange(1, 9)  # число a генерируется в диапазоне [0, 3]
        y.append(a)              # добавить чсло a в массив y
    print(j, '. Y=', y)




