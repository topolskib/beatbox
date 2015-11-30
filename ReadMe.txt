1. Wywolywanie programu
Aby rozpoczac dzialanie programu, uruchamiamy skrypt beatbox.py. Mozemy podac argument, ale nie musimy - jesli nie podamy go, lub podamy zly, to aplikacja zwroci liste dostepnych piosenek (i nie tylko piosenek, ale o tym pozniej). 
Co ważne, lista dostepnych piosenek nie jest ustalona - jesli stworzymy nowy folder z pikiem song.txt, to rowniez zostanie on rozpoznany. Oczywiscie nie swiadczy to o tym, ze z zawartosci tego folderu da sie zrobic piosenke, ale pozwala na rozroznianie folderow z modulami od folderow z piosenkami.
UWAGA - argument podajemy bez slasha na koncu, tzn piosenka, a nie piosenka/ 

2. Features - ogółem
Przy tworzeniu wlasnych piosenek mamy do wyboru sporą ilosc parametrów - od czestotliwosci dzwieku, wyboru i definicji instrumentu, az po dlugosc jego trwania - ostatnie dwie cyfry w komorkach plikow trackXX.txt mowia, przez ile wierszy ma byc odtwarzany dany dzwiek.
Mamy do wyvoru dwa typy komorek:
XX - dwuelementowa, XX odpowiada numerowi sampla w formacie wav. Dozwolone są sample w stereo, 44100 Hz. 
XX:YYY:ZZ - rozwiniecie wymagan na 100% - oprocz numeru sampla w formacie .txt (XX), wysokosci dzwieku (YYY) mamy tez do dyspozycji dlugosc dzwieku wyrazona w ilosciach wierszy pliku, czyli w szesnastkach. 

3. Definiowanie instrumentów
Definiowanie instrumentów odbywa sie za pomocą 5 parametrów: 
- type - wektor okreslajacy typ poszczegolnych skladowych dzwiekow, do wyboru "sin", "sq" i "saw" 
- attack - wektor okreslajacy wzgledna dlugosc narastania dzwieku dla poszczegolnych skladowych
- decay -wektor okreslajacy wzgledna dlugosc wyciszania dzwieku dla poszczegolnych skladowych
- coef - wektor wspolczynnikow przy sumowaniu skladowych - mozemy zrobic niektore skladowe glosniejsze, a niektore cichsze
- cutoff - wzgledny czas, ktory utniemy ze stworzonego dzwieku

WAŻNE - parametry type, attack, decay i coef musza byc podane jako wektory - nawet jesli sa jednoelementowe. Cutoff jest z kolei stosowany po zlozeniu wszystkich skladowych, wiec jest to wartosc liczbowa.

4. Czytanie archiwów
Program obsluguje rowniez czytanie archiwów zip. Warunek - jego struktura to archiwum -> folder -> pliki. Tak domyslnie pakuje ubuntu. Pliki sa rozpakowywane w systemowym tmp, skad sa potem usuwane samoczynnie. 

5. Bonus
Dla posiadaczy pakietu pyglet - ./beatbox.py drum_machine uruchamia maly bonus. 
