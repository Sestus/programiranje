README.md

A. IZVRŠNI SAŽETAK (EXECUTIVE SUMMARY)

Ovaj projekt bavi se analizom podataka prikupljenih s područja kratera Jezero s ciljem izrade automatiziranog navigacijskog sustava za autonomnog robota. Ulazni podaci uključuju informacije o temperaturi tla, pH vrijednosti, udjelu vode, prisutnosti metana te geoprostorne koordinate uzoraka. Korištenjem algoritama za obradu i filtriranje podataka identificiraju se relevantne lokacije za daljnje istraživanje. Krajnji rezultat projekta je generiranje strukturiranog JSON navigacijskog naloga koji robot koristi za kretanje i izvršavanje zadataka na terenu.


B. METODOLOGIJA OBRADE PODATAKA (DATA WRANGLING)

Podaci su učitani iz CSV datoteka korištenjem definiranog separatora (“;”) i decimalnog formata (“,”), čime je osigurana ispravna interpretacija numeričkih vrijednosti. Spajanje datasetova provedeno je preko jedinstvenog identifikatora “ID_Uzorka”.

Za uklanjanje senzorskog šuma definiran je skup logičkih uvjeta:
- temperatura tla mora biti u rasponu od -100 do 40 °C
- pH vrijednost mora biti između 0 i 14
- udio vode mora biti između 0% i 100%

Podaci koji ne zadovoljavaju ove uvjete klasificirani su kao anomalije i izdvojeni u zasebnu datoteku. Time je osigurana pouzdanost analize i eliminacija nerealnih mjerenja.

Dodatno, provedena je normalizacija tekstualnih vrijednosti (npr. uklanjanje razmaka i standardizacija zapisa “Pozitivno”) kako bi se izbjegle greške u filtriranju i klasifikaciji podataka.


C. GEOPROSTORNA ANALIZA I VIZUALIZACIJA

Analiza uključuje više grafičkih prikaza:

1. Scatter graf temperature i udjela vode:
   Omogućuje uvid u potencijalnu korelaciju između temperature tla i prisutnosti vode, uz dodatnu klasifikaciju prema metanu.

2. Karta dubine bušenja:
   Vizualizira raspodjelu dubine uzorkovanja pomoću kolor mape, čime se identificiraju zone s dubljim analizama.

3. Distribucija metana:
   Prikazuje prostornu raspodjelu pozitivnih i negativnih detekcija metana, što je ključno za detekciju potencijalnih bioloških ili geokemijskih aktivnosti.

4. Karta kandidata:
   Ističe lokacije gdje su istovremeno detektirani metan i organske molekule. Takve točke označene su kao prioritetne za daljnje istraživanje.

5. Satelitska mapa (EXTENT mapiranje):
   Satelitska slika je georeferencirana korištenjem minimalnih i maksimalnih GPS koordinata iz skupa podataka. Parametar “extent” omogućuje preslikavanje slike u stvarni koordinatni sustav, čime se podaci precizno pozicioniraju na kartu. Ovaj pristup omogućuje pouzdanu orijentaciju robota u stvarnom prostoru.


D. KOMUNIKACIJSKI PROTOKOL (JSON UPLINK)

Za komunikaciju s vanjskim sustavima koristi se JSON format. Struktura uključuje listu kandidata s njihovim koordinatama i pripadajućim akcijama.

Primjer:

{
  "kandidati": [
    {
      "ID_Uzorka": 101,
      "GPS_LAT": 18.38,
      "GPS_LONG": 77.58,
      "akcije": [
        {"tip": "NAVIGACIJA"},
        {"tip": "SONDIRANJE"},
        {"tip": "SLANJE_PODATAKA"}
      ]
    }
  ]
}

Generiranje ovog JSON-a automatizirano je pomoću petlje koja prolazi kroz filtrirane podatke. Time se izbjegava ručno definiranje naredbi i omogućuje skalabilnost sustava.


E. INŽENJERSKI DNEVNIK (TROUBLESHOOTING LOG)

Problem 1: Neispravno spajanje tablica
Uzrok: Pogrešan separator u CSV datotekama doveo je do nepravilnog učitavanja podataka.
Rješenje: Eksplicitno definiran separator “;” prilikom učitavanja datoteka.

Problem 2: Pogrešni tipovi podataka
Uzrok: Numeričke vrijednosti učitane su kao string, što je uzrokovalo greške u analizi.
Rješenje: Primijenjena konverzija tipova i provjera strukture podataka.

Problem 3: Neispravna klasifikacija metana
Uzrok: Nekonzistentni tekstualni zapisi (npr. “Pozitivno ” s razmakom).
Rješenje: Normalizacija string vrijednosti korištenjem funkcija za obradu teksta.

Problem 4: Pogrešno pozicioniranje na karti
Uzrok: Neusklađenost dimenzija slike i koordinata.
Rješenje: Korištenje “extent” parametra za pravilno mapiranje GPS granica na sliku.
