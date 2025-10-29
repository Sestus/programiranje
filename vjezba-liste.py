"""
moja_lista = [10,20,30]

prvi_element = moja_lista[0]

print (prvi_element)

moja_lista.append(40)

print (moja_lista)

dio_liste = moja_lista[1:3]

print (dio_liste)
"""
"""
voce = ["jabuke", "banane", "kruške"]

prvi_element = voce[0]
print(prvi_element)
voce.append("naranča")
print(voce)
"""
ormar = [
    ['majica', 'kapa', 'sal'],   # 0. redak (polica)
    ['hlace', 'carape','remen'], # 1. redak
    ['jakna', 'cipele', 'cizme'],# 2.redak
]
"""
print (f"hlače? {ormar[1][0]}")
print (ormar [0][1])
print (ormar [1][1])
print (ormar [2][1])
"""
"""
for odjeca in ormar:
    print (odjeca[1])

for redak in ormar:
    print (f"sadržaj redaka: {redak}")

    for element in redak:
        print (f"element: {element}")
"""

def pronadji_broj (lista,broj):
    print (f"tražim broj {trazeni_broj} u listi {lista}")
    for element in lista:
        if element == trazeni_broj:
            print (f"broj {trazeni_broj} se nalazi u listi.")
            break
        else:
            print (f"broj {trazeni_broj} se ne nalazi u listi.")


lista = [10, 20, 30, 40, 50]
trazeni_broj = 30
pronadji_broj (lista, trazeni_broj)