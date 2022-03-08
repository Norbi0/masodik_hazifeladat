lista = []
szam = 1
while szam != 0:
    szam = int(input())
    if szam != 0:
        lista.append(szam)
        atlag = sum(lista)/len(lista)
    else:
        atlag = sum(lista) / len(lista)
print(atlag)