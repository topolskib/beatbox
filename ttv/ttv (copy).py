import sys
import dodaj
import dzwiek
import numpy as np
import scipy.io.wavfile
from scipy import signal

def table_to_track(dir, track_no ,bpm, nuty):
    f = open('./' + dir + '/track' + track_no + '.txt', 'r')
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
            file = open("./" + dir + "/sample" + i[:2] + ".txt")
            kod = file.read()
            file.close()
            code = compile("f=" + str(nuty[i[3:6]]) + "\n" + "T=" + str(int(i[7:])) + "*(60/bpm)/4\n"  + kod, '<string>', 'exec')
            eval(code)
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

def make_song(dir, bpm):    
    f_nuty = open("slownik-nuty.txt")
    nuty = eval(f_nuty.read())
    f_nuty.close()
    f = open('./' + dir + '/song.txt', 'r')
    data = f.readlines()
    output = np.zeros((1,2))
    end=0
    for line in data:
        track,end_nowy = table_to_track(dir, line.split()[0], bpm, nuty)        
        output = dodaj.dodaj_dzwiek(output, track, end)
        end += end_nowy  
    scipy.io.wavfile.write(dir +'.wav', 44100, np.int16(output/np.amax(abs(output))*32767))  
    print("Pomyslnie utworzono plik " + dir +".wav")


