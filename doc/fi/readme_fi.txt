Razttthon

Copyright Eetu 'Razbit' Pesonen, 2014

Lisensoitu GNU General Public License -lisenssin 3. version mukaisin ehdoin. Lue LICENSE.txt.

T‰m‰n dokumentoinnin sis‰ltˆ voi muuttua ilman erillist‰ ilmoitusta.

1. Ohjelman esittely ja analysointi
---------------------------------------------
Razttthon on (taas yksi) ristinollapeli. Sit‰ voi pelata kaveria tai tietokonetta vastaan, se pit‰‰ kirjaa voitoista, h‰viˆist‰ sek‰ kesken j‰‰neist‰ ja tasapeliin loppuneista peleist‰. Ohjelma tallentaa ja lukee pelaajien tiedot (nimi, pelattujen pelien m‰‰r‰, voitot, h‰viˆt ja kesken j‰tˆt) k‰ytt‰m‰ll‰ tiedostoa 'players.save'. Peli‰ voisi jatkaa lis‰‰m‰ll‰ mahdollisuuden verkon v‰lityksell‰ toimivalle pelaamiselle, jonkinlaisen client-server j‰rjestelm‰n kautta, mutta se on t‰m‰n ohjelmointiprojektin tarkoituksen ulkopuolella.

2. Syˆtteet ja tulosteet sek‰ tiedostot
--------------------------------------------------
Ohjelmaa k‰ytet‰‰n seuraavilla komennoilla:
    - h, help: listaa komennot
    - q, quit: poistuu pelist‰
    - p, play: aloita uusi peli
    - s, stats <nimi>: n‰ytt‰‰ pelaajan <nimi> tilastot
    - l, leader [w, wins; l, losses; g, games]: n‰ytt‰‰ pistetulukon j‰rjestettyn‰ voittojen, h‰viˆiden tai pelattujen pelien m‰‰r‰n mukaan.

Jos kirjoitat 'play', kysyy ohjelma sinulta pelimuodon (1: yksinpeli, 2: kaksinpeli) ja nimesi sek‰ mahdollisesti pelikaverisi nimen.

Nimet ja pelimenestys tallennetaan players.save -tiedostoon muodossa <nimi> <pelatut pelit> <voitot> <h‰viˆt> <keskeytykset>, esimerkiksi Matti 2 1 1 0. Jos tiedosto puuttuu, luo ohjelma uuden. Mik‰li tiedostossa on vikaa (kuten Matti 2 1 1 a), poistaa ohjelma rivin ja luo uuden.

3. Ohjelman toiminta
----------------------------
Kun ohjelma avataan, k‰y se players.save ñtiedoston l‰pi ensimm‰isen‰ ja tallentaa sen playerlist ñlistamuuttujaan. T‰m‰n j‰lkeen siirryt‰‰n îkomentosilmukkaanî, jossa k‰ytt‰j‰lt‰ odotetaan komentoa (ks. ylemp‰‰). Kun k‰ytt‰j‰n antama komento tunnistetaan, siirryt‰‰n silmukasta pois suorittamaan komennon toimintoja. Kun toiminto on suoritettu loppuun, palataan komentosilmukkaan.  Mik‰li k‰ytt‰j‰ kirjoittaa íquití, poistuu ohjelma silmukasta, tallettaa muutokset players.save ñtiedostoon, tuhoaa muuttujat ja sulkeutuu.

Pelin toiminta on kuvattu vuokaaviossa peli.png
Pelin lopetuskoodit ovat -1 (Lopetettu komennolla s), 0 (pelaaja 0 voitti pelin), 1(pelaaja 1 voitti pelin) ja 2 (peli loppui tasapeliin, kun lauta t‰yttyi).

Pelin p‰‰tytty‰ lopetuskoodi l‰hetet‰‰n tilastoluokalle (cPlayerHandler), joka p‰ivitt‰‰ pelaajalistaan koodin mukaiset tiedot: pelaajille yksi peli lis‰‰, voittajalle voitto, h‰vi‰j‰lle h‰viˆ. Jos peli lopetettiin tahallaan (s ñkomennolla), molemmille yksi pelattu peli, h‰viˆ sek‰ lopetus lis‰‰. T‰m‰n j‰lkeen palataan komentosilmukkaan.

Mik‰li pelataan yksinpeli‰, tietokone on pelaaja 0. Sen teko‰ly toimii kuvan ai.png mukaisesti.

4. Osien kuvaus
---------------------
4.1 Luokkahierarkia
--------------------------
Ks. hierarkia.png

4.2 Luokkien ja funktioiden esittely
----------------------------------------------
4.2.1 cMain (mainc.py)
------------------------------
Pit‰‰ sis‰ll‰‰n globaaleja muuttujia.
Sis‰ltˆ:
  - playerlist: pit‰‰ sis‰ll‰‰n listan pelaajista sek‰ heid‰n pisteist‰‰n
  - nPlayers: pelaajien m‰‰r‰

4.2.2 cPlayerHandler (player.py)
--------------------------------------------
K‰sittelee pelaajiin liittyvi‰ tietoja, k‰yttˆliittym‰ cMain.playerlist ñlistalle.
Sis‰ltˆ:
  - getPlayers: palauttaa pelaajien m‰‰r‰n
  - getPID(nimi): palauttaa pelaajanumeron pelaajalle <nimi> (cMain.playerlist ñlistan indeksi). Palauttaa -1, mik‰li pelaajaa ei lˆydy.
  - getName(pid): palauttaa nimen pelaajanumerolle pid
  - getGames(pid): palauttaa pelaajan pelaamien pelien m‰‰r‰n
  - getWins(pid): palauttaa pelaajan voittamien pelien m‰‰r‰n
  - getLosses(pid): palauttaa pelaajan h‰vi‰mien pelien m‰‰r‰n
  - getQuits(pid): palauttaa pelaajan keskeytt‰mien pelien m‰‰r‰n
  - getData(pid): palauttaa kaiken yll‰mainitun datan (nimest‰ keskeytyksiin)
  - addPlayer(nimi): lis‰‰ uuden pelaajan nimelt‰ <nimi> cMain.playerlist ñlistaan, palauttaa PID:n
  - addGame(pid): kasvattaa pelaajan pelaamien pelien m‰‰r‰‰ yhdell‰, palauttaa False mik‰li jokin virhe sattuisi tulemaan.
  - addWin(pid): kasvattaa pelaajan voittamien pelien m‰‰r‰‰ yhdell‰, palauttaa False mik‰li jokin virhe sattuisi tulemaan.
  - addLose(pid): kasvattaa pelaajan h‰vittyjen pelien m‰‰r‰‰ yhdell‰, palauttaa False mik‰li jokin virhe sattuisi tulemaan.
  - addQuit(pid): kasvattaa pelaajan keskeytt‰mien pelien m‰‰r‰‰ yhdell‰, palauttaa False mik‰li jokin virhe sattuisi tulemaan.

4.2.3 Game (gameloop.py)
-----------------------------------
Pit‰‰ sis‰ll‰‰n itse pelin.
Sis‰ltˆ:
  - getNames(): palauttaa pelaajien nimet
  - printGame(): tulostaa cGame.gameGrid ñmuuttujan sis‰llˆn (pelilauta) n‰ytˆlle ruudukkoon muotoiltuna.
  - stop(status): asettaa cGame.cont ñmuuttujan arvoksi False, tyhjent‰‰ ruudun, kutsuu printGame() ñfunktiota ja asettaa muuttujan cGame.status arvoksi parametrina saamansa muuttujan status arvon. Kutsuu cPlayerHandler ñluokan funktioita p‰ivitt‰‰kseen pelaajien tiedot.
  - over(player): tarkistaa onko pelaaja player voittanut pelin (kolme per‰kk‰ist‰ pelimerkki‰), siin‰ tapauksessa kutsuu stop() funktiota muuttujalla player. Mik‰li pelaaja ei ole voittanut, tarkistaa onko lauta tyhj‰ ja niin ollessa kutsuu stop() funkiota arvolla 2 (tasapeli)
  - turn(player): tarkistaa muuttujan player arvon. Mik‰li se on 0 (PID 0 on varattu CPU ñpelaajalle eli tietokoneelle), toimii funktio edell‰ kuvatun teko‰lyn mukaisesti. Muussa tapauksessa pelaajalta kysyt‰‰n sijaintia uudelle pelimerkille. Mik‰li annettu sijainti on tyhj‰, asetetaan siihen pelaajan pelimerkki (x tai o). Muuten kysyt‰‰n uudestaan.
  - twoInaRow(mode): Jos mode = 0, tarkistaa voiko tietokone voittaa yhdell‰ merkill‰ (onko sill‰ kaksi pelimerkki‰ riviss‰ ja yksi tyhj‰ samalla rivill‰). Mik‰li n‰in on, asettaa se siihen pelimerkin. Mik‰li mode = 1, tarkistaa funktio vastapelaajan merkit ja katsoo voiko h‰n voittaa yhdell‰ merkill‰. Mik‰li n‰in on, asettaa funktio pelimerkin siten, ett‰ se est‰‰ vastustajaa voittamasta.
  - loop(): kutsuu turn(), over() ja printGame() ñfunktioita kunnes cGame.cont ñmuuttuja asetetaan arvoon False esimerekiksi kutsumalla funktiota stop()
  - __init__(pid1, pid2): alustaa luokan sis‰iset muuttujat ja kutsuu loop() ñfunktiota.

4.2.4 cRazttthon (mainc.py)
------------------------------------
Sis‰lt‰‰ p‰‰funktiot ohjelman toimintojen k‰yttˆˆn.
Sis‰ltˆ:
  - parsePlayerFile(): tallentaa players.save ñtiedoston sis‰llˆn cMain.playerlist ñmuuttujaan. Korjaa tiedostossa olevat mahdolliset virheet ja alustaa listan, mik‰li tiedosto puuttuu.
  - savePlayerFile(): tallentaa cMain.playerlist ñmuuttujan sis‰llˆn tiedostoon players.save
  - newGame(): kysyy k‰ytt‰j‰lt‰ pelimuotoa sek‰ pelaajien nimi‰. Kutsuu saamillaan tiedoilla cGame.__init__() ñfunktiota.
  - stats(name): kutsuu cPlayerHandler.getData() ñfunktiota ja tulostaa muotoiltuna saamansa tilastot pelaajalle name.
  - leaderboard(strMode): kutsuu cPlayerHandler.getData() ñfunktiota jokaisella pelaajalla, j‰rjest‰‰ tiedot saamansa parametrin (strMode) mukaan ja tulostaa ne.

Lis‰ksi ohjelmasta lˆytyy oman razlib ñkirjastoni funktioita, mutten selosta niit‰ t‰ss‰, koska ne ovat hyvin teknisi‰.

5. Testaus
-------------
Ohjelmaa olen testannut oikeilla ja v‰‰rill‰ syˆtteill‰ sek‰ korruptoituneella ja puuttuneella players.save ñtiedostolla, enk‰ ole bugeja tai virheit‰ lˆyt‰nyt. Mik‰li niit‰ lˆytyd‰t, olen pahoillani ja pyyd‰n ilmoittamaan minulle niist‰ osoitteeseen razclocker@gmail.com.
