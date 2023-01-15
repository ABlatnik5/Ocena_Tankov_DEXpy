# Ocena Tankov (DEXpy)

Avtor: Aljaž Blatnik

[Fakulteta za informacijske študije v Novem mestu](https://www.fis.unm.si/).

Študijski program: Računalništvo in spletne tehnologije, 2. stopnja.

Študijsko leto 2022/2023.

## Model

Pri spletni aplikaciji uporabljamo model ocene tankov, ki je bil ustvarjen v [programskem orodju DEXi](https://kt.ijs.si/MarkoBohanec/dexi.html). Model je dostopen v mapi [Original_Dex_Model](https://github.com/ABlatnik5/Ocena_Tankov_DEXpy/tree/main/Original_Dex_Model). Podroben opis je napisan v obliki seminarske naloge in je dostopen v obliki [PDF datoteke](https://github.com/ABlatnik5/Ocena_Tankov_DEXpy/blob/main/ABlatnik_Ocena_Tankov.pdf).

Model je bil strukturiran na podlagi informacij, ki so javno znane. Glede na to, da so vse variante tankov, ki so bile uporabljene pri ocenjevanju, še v uporabi, se lahko podatki rahlo razlikujejo od dejanskih specifikacij določenega tanka. Model je zelo preprost in predstavlja ogrodje za gradnjo bolj kompleksnih modelov, kjer se upošteva več dodatnih, bolj podrobnih parametrov.
 
## Namestitev aplikacije

1. Kloniramo ali prenesemo repozitorij Ocena_Tankov_DEXpy.
2. Za uspešno uporabo potrebujemo [Python 3.11](https://www.python.org/downloads/release/python-3110/), [django 4.1.5](https://docs.djangoproject.com/en/4.1/topics/install/) ter po potrebi še dodatne knjižnice, na katere nas opozori ukazni poziv.
3. V ukaznem pozivu (CMD) navigiramo do lokacije repozitorija (kjer se nahaja manage.py, to je v mapi Ocena_Tankov_DEXpy).
4. Uporabimo ukaz `py manage.py runserver`.
5. Ko se strežnik zažene, v poljubnem brskalniku v naslovno vrstico vpišemo naslov `https://127.0.0.1:8000/ocena/main`. Delovanje aplikacije je bilo testirano na brskalniku Google Chrome (različica 109.0.5414.74).
6. Naslov `https://127.0.0.1:8000/ocena/main` vsebuje obrazec na podlagi katere se potem oceni model, naslov `https://127.0.0.1:8000/ocena/final` pa vsebuje rezultate, ki temeljijo na vhodnih parametrih, ki jih vnesemo na naslovu, ki vsebuje obrazec.

## Viri in literatura

- [War Thunder wiki](https://wiki.warthunder.com/Ground_vehicles) : Stran je bila uporabljena za približne ocene oklepa tankov.
- [Begelj, A. (2010). Večparametrski odločitveni model za podporo odločanju trenerjem pri vodenju košarkarske ekipe. *Zbornik 7. festivala raziskovanja ekonomije in managementa, str. 605-611.*](https://www.fm-kp.si/zalozba/ISBN/978-961-266-122-9/prispevki/070.pdf) : Teoretična izhodišča pri načrtovanju modela. 
- [Bohanec, M. & Rajkovič, V. (b. l. ). Večparametrski odločitveni modeli.](https://kt.ijs.si/MarkoBohanec/org95/) : Teoretična izhodišča pri načrtovanju modela. 
- [Jereb, B. (2015). *Večparametrski odločitveni model za logistike z dodanimi večpredstavnimi vsebinami: visokošolski učbenik z recenzijo.* Celje: Fakulteta za logistiko.](http://labinf.fl.uni-mb.si/vecparametrski-odlocitveni-model/VPOM.pdf) : Teoretična izhodišča pri načrtovanju modela. 
- [Šetina, S. (2009). *Odločitveni model za pomoč pri izbiri najprimernejšega ponudnika CNC obdelovalnega centra* (diplomska naloga). Univerza v Mariboru: Fakulteta za organizacijske vede.](https://core.ac.uk/reader/67531520) : Teoretična izhodišča pri načrtovanju modela. 
- [Vrč, G. (2004). *Računalniško podprt večparametrski odločitveni model za ugotavljanje problemov izdelkov v razvojni fazi* (magistrska naloga). Univerza v Ljubljani: Ekonomska fakulteta.](http://www.cek.ef.uni-lj.si/magister/verc390.pdf) : Teoretična izhodišča pri načrtovanju modela. 
