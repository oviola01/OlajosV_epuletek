"""minta
(a stílus kialakítása nem része a feladatnak, de a sorszámok és betűjelek kiíratása igen):
I/A:
Játékos neve: Gandalf
szerepkör: varázsló
 
I/B:
Üdvözlünk Gandalf, 2 életed van!
A.	Kérje be az alábbi adatokat a fenti mintának megfelelően:
Játékos neve és szerepköre!  (2p)
B.	A program az adatbekérés után írasson ki egy üdvözlést az alábbiak alapján!
Amennyiben „varázsló” a játékosunk, 2 élete van.
Amennyiben „harcos” a játékosunk, 10 életereje van.
Amennyiben ismeretlen a játékosunk szerepköre, 8 életereje van. (4p)
A mintának megfelelően jelenítette meg az eredményt, és kérte be az adatokat. (1p)

"""
jatekos = ""
szerep = ""
elet = 0

def bekeres():
    jatekos = input("Játékos neve: ")
    szerep = input("szerepkör: ")
    print(f"I/A:\n\tJátékos neve: {jatekos}\n\tszerepkör: {szerep}")
    return jatekos, szerep

def udvozles():
    jatekos, szerep = bekeres()
    if szerep == "varázsló":
        elet = 2
    elif szerep == "harcos":
        elet = 10
    else:
        elet = 8
    print(f"I/B:\n\tÜdvözlünk {jatekos}, {elet} életed van!")
