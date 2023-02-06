"""
Az epulet.txt forrásállomány, épületek adatait tartalmazza, a feladatok megoldása során ezeket az adatokat használja!
Az epulet.txt állomány szerkezete:
·         az épület neve: pl: Centrum LIM
·         az épület városa: pl.: Varsó
·         az épület országa: pl.: Lengyelország
·         az épület magassága m-ben: pl.: 140
·         az épület emeleteinek a száma, pl.: 43
·	az épület építésének az éve, pl.1949
Az állomány első sora a mezőneveket tartalmazza „$” jellel elválasztva.
A megoldás mintája:
III/A, B:
            	Az épületek száma: 8
III/C:
            	Az 555 lábnál magasabb épületek száma: 2.
III/D:
            	A legöregebb épület országa: Lengyelország.            	
A.	Olvassa be osztály segítségével (utóbbit hozza létre külön modulban) a epulet.txt fájlból a játékosok adatait, és tárolja el összetett adatszerkezetben, ami elősegíti a további feladatok könnyű megoldását! Ügyeljen arra, hogy az állomány első sora az adatok fejlécét tartalmazza! (7p)
B.	Írassa ki az épületek számát a mintának megfelelően a konzolra! (2p)
C.	Adja meg az 555 lábnál magasabb épületek számát, ha 1 m = 3.280839895 láb! (4p)
D.	Írassa ki konzolra a mintának megfelelően a legöregebb épület (ha több is van, akkor az első legöregebb adatait) országát. (4p)

"""


from Epuletek import Epuletek
epulet_lista = []

def beolv():
    fajl = open("epulet.txt", "r", encoding="UTF-8")
    fejlec = fajl.readline()
    szoveg = fajl.readlines()
    fajl.close
    
    i = 0
    while i < len(szoveg):
        sor = szoveg[i].strip().split("$")
        epulet_lista.append(Epuletek(sor))
        i += 1
    
    #próba: print(epulet_lista[2].magassag)

def epuletek_szama():
    return len(epulet_lista)

def magas_epuletek():
    mennyi = 0
    i = 0
    while i < len(epulet_lista):
        if (epulet_lista[i].magassag) * 3.280839895 > 555:
            mennyi += 1
        i += 1
    return mennyi
        
def legidosebb_epulet():
    legoregebb = 0
    i = 0
    while i < len(epulet_lista):
        if (epulet_lista[legoregebb].epult) > (epulet_lista[i].epult):
            legoregebb = i
        i += 1
    return epulet_lista[legoregebb].orszag