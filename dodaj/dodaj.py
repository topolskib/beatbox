"""
Modul zawiera funkcje, ktora do jednego dzwieku dodaje funkcje z odpowiednim opoznieniem. 
"""

import numpy as np
import scipy.io.wavfile
from scipy import signal

def dodaj_dzwiek(old, new, delay):
    """
    Argumenty wejsciowe: 
    old - macierz o dwoch kolumnach, reprezentujaca dzwiek stereo o czestotliwosci probkowania 44100 hz. 
    Jest to dzwiek "bazowy", tzn. do niego funkcja dodaje kolejny.
    
    new - macierz o dwoch kolumnach, reprezentujaca dzwiek stereo o czestotliwosci probkowania 44100 hz. 
    Jest to dzwiek ktory funkcja dodaje.
    
    delay - liczba typu float, reprezentuje opoznienie drugiego dzwieku wzgledem pierwszego wyrazone w sekundach.
    """
    l_old = np.shape(old)[0]
    l_new = np.shape(new)[0]
    l_delay = int(delay*44100)
    if l_old <=l_delay + l_new:
        output = np.zeros((l_delay + l_new,2))
        output = np.vstack((old,np.zeros((l_delay + l_new - l_old,2)))) + np.vstack((np.zeros((l_delay,2)), new))
        return output
    elif l_old >=l_delay + l_new:
        old += np.vstack(((np.zeros((l_delay,2)), new, np.zeros((l_old - l_new -l_delay,2)))))
        return old
    
    
    
