import bevezetes
import sorozat
import beolvasas


#1
bevezetes.udvozles()

#2
dobasok = sorozat.dobasok()
print(f"II/A, B, C:\n\t{sorozat.kiiras(dobasok)}")
fejek = sorozat.fejek_szama(dobasok)
sorozat.konzol_kiir(fejek)
sorozat.file_kiir(fejek)


#3
beolvasas.beolv()

print(f"III/A, B:")
print(f"\t Az épületek száma: {beolvasas.epuletek_szama()}")

print(f"III/C:")
print(f"\t Az 555 lábnál magasabb épületek száma: {beolvasas.magas_epuletek()}")

print(f"III/D:")
print(f"\t A legöregebb épület országa: {beolvasas.legidosebb_epulet()}")