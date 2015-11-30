"""
Modul zawiera funkcje make_song, ktora tworzy piosenke majac dany katalog, oraz
table_to_track, ktora tworzy macierz reprezentujaca dzwiek stworzony na podstawie danego pliku trackXX.txt
"""
import sys
import dodaj
import dzwiek
import numpy as np
import scipy.io.wavfile
from scipy import signal

def table_to_track(dir, track_no ,bpm, nuty):
    """
    Funkcja zwraca macierz reprezentujaca dzwiek stereo stworzony na podstawie danego pliku trackXX.txt.
    
    Argumenty wejsciowe:
    dir - string reprezentujacy folder w ktorym operujemy.
    track_no - string zawierajacy numer tracka, ktory chcemy analizowac.
    bpm - liczba reprezentujaca bpm danej piosenki
    nuty - slownik z definicjami nut
    """
    f = open(dir + '/track' + track_no + '.txt', 'r')
    data = f.readlines()
    # zapisujemy wczesniej sample, zeby potem sie tylko odwolywac bez ponownego wczytywania
    content = np.unique([x.split() for x in data])
    lengs = np.array([len(x) for x in content])
    sample_no = content[np.where(lengs==2)[0]]
    instr_no = content[np.where(lengs==9)[0]]
    dict_sample={}
    for i in sample_no: 
        if(i=='--'):
            continue
        fs,sample = scipy.io.wavfile.read(dir + '/sample' + i + ".wav")
        dict_sample[i] = sample/np.amax(abs(sample))
    for i in instr_no: 
        if(i!='---------'):
            file = open(dir + "/sample" + i[:2] + ".txt")
            defs = eval(file.read())
            file.close()
            f=nuty[i[3:6]]
            T=int(i[7:])*(60/bpm)/4
            dzw = dzwiek.custom_sound(defs['type'], defs['attack'], defs['decay'], defs['cutoff'], defs['coef'], T, f)
            dict_sample[i] = dzw
    t=0
    output = np.zeros((1,2))
    for lines in data:
        linia = lines.split()
        for i in range(0,len(linia)):
            if (linia[i]!="--" and linia[i]!="---------"):
                output = dodaj.dodaj_dzwiek(output, dict_sample[linia[i]], t)
        t+= (60/bpm) /4 # szesnastki
    end = np.shape(data)[0]* (60/bpm)/4
    return((output,end))    

def make_song(dir, bpm,name):
    """
    Funkcja tworzy piosenke na podstawie plikow znajdujacych sie w katalogu dir.
    
    Argumenty wejsciowe:
    dir - string reprezentujacy folder w ktorym operujemy.
    bpm - liczba reprezentujaca bpm danej piosenki
    name - nazwa piosenki
    """   
    f = open(dir + '/song.txt', 'r')
    data = f.readlines()
    output = np.zeros((1,2))
    end=0
    f = open("slownik-nuty.txt")
    nuty = eval(f.read())
    f.close()
    for line in data:
        track,end_nowy = table_to_track(dir, line.split()[0], bpm, nuty)        
        output = dodaj.dodaj_dzwiek(output, track, end)
        end += end_nowy    
    scipy.io.wavfile.write("./"+ name +'.wav', 44100, np.int16(output/np.amax(abs(output))*32767))  
    print("Pomyslnie utworzono plik " + name +".wav")


