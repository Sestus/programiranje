# Funkcija za učitavanje teksta iz datoteke
def ucitaj_tekst(filepath):
    try:
        # ovdje ide logika za citanje datoteke
        with open (filepath, "r", encoding="utf-8") as file:
            sadrzaj=file.read()
        return sadrzaj
    except FileNotFoundError:
        print(f"Datoteka '{filepath}' nije pronađena.")
        return None # Vratiti ćemo "ništa" ako datoteka ne postoji
# funkcija za pročišćavanje tesksta
def ocisti_tekst(tekst):
    # Kod za pročišćavanje teksta ide ovdje
    tekst = tekst.lower()
    interpunkcija = ['.', ',', '!', '?', ':', ';', '"', "'", '(', ')']
    for znak in interpunkcija:
        tekst = tekst.replace(znak, '')

    lista_rijeci = tekst.split()
        


    return lista_rijeci

if __name__ == "__main__":
    filepath = "tekst.txt"
    print(f"Učitavam tekst iz datoteke: {filepath}")
    ucitani_tekst = ucitaj_tekst(filepath)
    if ucitani_tekst:
        print("Učitani tekst je:")
        print(ucitani_tekst)
    else:
        print("Greška pri učitavanju datoteke.")
    
    ucitani_tekst = ocisti_tekst(ucitani_tekst)
    
    if ucitani_tekst:
        print("Očišćeni tekst je:")
        print(ucitani_tekst)
    else:
        print("Greška pri očišćavanju teksta.")
  
