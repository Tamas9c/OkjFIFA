with open("fifa.txt", 'r', encoding='latin2') as f:
    lista = list()
    fejlec = f.readline()
    for sor in f:
        lista.append(sor.strip().split(";"))
        
#3. feladat
print(f'3. feladat: A világranglistán {len(lista)} csapat szerepel')

#4. feladat

öp = sum( [int(sor[3]) for sor in lista] )
öv = len(lista)

átlag = öp/öv

print(f'4. feladat: A csapatokátlagos pontszáma: {átlag} pont')

#5. feladat
valtozas0 = 0
helyezes0 = 0
for csapat, helyezes, valtozas, pontszam in lista:
    if int(valtozas) > valtozas0:
        valtozas0 = int(valtozas)
        #if int(valtozas) > valtozas0:
        pontszam0 = pontszam
        csapat0 = csapat
        helyezes0 = helyezes

print(f'5. feladat: A legtöbbbet javító csapat:')
print(f'        Helyezés: {helyezes0}          ')
print(f'        Csapat: {csapat0}              ')
print(f'        Pontszám: {pontszam0}          ')

#6. feladat
szamlalo = 0
for csapat, helyezes, valtozas, pontszam in lista:
    if csapat == 'Magyarország':
        szamlalo += 1
if szamlalo > 0:
    print(f'6. feladat: A csapatok között van Magyarország')
if szamlalo == 0:
    print(f'6. feladat: A csapatok között nincs Magyarország')

#7. feladat
import collections

gyujto = collections.Counter()

for csapat, helyezes, valtozas, pontszam in lista:
    gyujto[valtozas] += 1
print(f'7. feladat: Statisztika')
for valtozas, darab in gyujto.items():
    if darab > 1:
        print(f'        {valtozas} helyet véltozott: {darab} csapat')