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


# funkcija za uklanjanje čestih riječi
def stop_words(lista_rijeci, ceste_rijeci):
    # Kod za uklanjanje čestih riječi ide ovdje
    lista_rijeci = ceste_rijeci.lower()
    stop_words = ['ako', 'i', 'u', 'na', 'je', 'ali', 'a', 'o', 'li', 'te', 'se', 'za', 'su', 'to', 'sa', 'od', 'do', 'što']
    for rijec in stop_words:
        if rijec in lista_rijeci:
            stop_words.remove(rijec)
    return lista_rijeci



 

def broji_rijeci(lista_rijeci):
    #riječnik u koji ćemo spremiti svaku riječ i koliko se puta ta riječ ponovila u tekstu
    brojac_rijeci={}
    for rijec in lista_rijeci:
        if rijec in brojac_rijeci:
            brojac_rijeci[rijec] += 1
        else:
            brojac_rijeci[rijec] = 1


 
    
    if ucitani_tekst:
        print("Očišćeni tekst je:")
        print(ucitani_tekst)
        # Brojanje riječi i ispis rječnika
        brojac_rijeci = broji_rijeci(ucitani_tekst)
        print("Brojač riječi je:")
        print(brojac_rijeci)
    else:
        print("Greška pri očišćavanju teksta.")
  
