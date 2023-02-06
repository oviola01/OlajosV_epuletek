"""II/A, B, C:
           	FEJ-ÍRÁS-ÍRÁS-ÍRÁS-FEJ-ÍRÁS-ÍRÁS
II/D, E:
           	A fejek száma: 2.  	
A fejek.txt tartalma:
II/F:
A fejek száma: 2. 	
 
A.	Írasson ki a konzolra kötőjellel (-) elválasztva 7 pénzérmével való dobást véletlen számsorozat alapján a mintának megfelelően! (4p)
B.	A generált értékeket tárolja lista adatszerkezetben logikai típusokkal (0: írás, 1: fej)! (1p)
C.	A „–” jel csak az értékek között szerepeljen (a végén ne)! (2p)
D.	Írjon függvényt fejek_szama néven, amiben számolja meg, hogy hány olyan elem van, ami fej (1). A visszatérési érték legyen egy egész szám! (3p)
E.	A fejek_szama függvény eredményét írassa ki a mintának megfelelően a konzolra, amit konzol_kiir nevű metódusban fogalmazzon meg! (2p)
F.	A fejek_szama függvény eredményét írassa ki a mintának megfelelően a fejek.txt nevű fájlba, amit file_kiir nevű metódusban fogalmazzon meg! (2p)
"""
import random

def dobasok():
    lista = []
    i = 0
    while i < 7:
        dobas = int(random.random()*2)
        lista.append(dobas)
        i += 1
    return lista

def kiiras(lista):
    szoveg = ""
    i = 0
    while i < len(lista):
        if lista[i] == True:
            szoveg += "FEJ"
        else:
            szoveg += "ÍRÁS"
        if i < len(lista)-1:
            szoveg += "-"
        i += 1
    return szoveg

def fejek_szama(lista):
    osszeg = 0
    i = 0
    while i < len(lista):
        if lista[i] == True:
            osszeg += 1
        i += 1
    return osszeg

def konzol_kiir(konzolra):
    szoveg = f"II/D, E:\n\tA fejek száma: {konzolra}"
    print(szoveg)
    return szoveg

def file_kiir(mentesre):
    fajl = open("fejek.txt", "w", encoding="UTF-8")
    fajl.write(str(mentesre))
    fajl.close
    print(f"A fejek.txt tartalma:\nII/F:\n\tA fejek száma: {mentesre}")