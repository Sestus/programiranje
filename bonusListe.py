print("\n--- Bonus Izazov: Priprema za projekt ---")
# Ovo je struktura koju smo dobili u Fazi 3
rezultati = [('hlapić', 15), ('gita', 12), ('majstor', 10)]

# 1. Kreiramo novu listu. Njen prvi element je lista koja predstavlja zaglavlje.
tablica = [['Riječ', 'Frekvencija']]
print(f"Tablica na početku (samo zaglavlje): {tablica}")

for rezultat in rezultati:
    lista_elemenata = list(rezultat) # Ovo će stvoriti ['hlapić', 15]
    tablica.append(lista_elemenata)

    print(f"tablica nakon dodavanja elemaenata: {tablica}")

    for red in tablica:
        print(red)