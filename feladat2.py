def Lnko(a, b):
    if a == b:
        return a
    if b < a:
        a, b = b, a
    while (0 < a):
        a, b = b % a, a
    return b
a = int(input("Adjon meg egy szamot: "))
b = int(input("Adjon meg egy masik szamot: "))

print(Lnko(a, b))