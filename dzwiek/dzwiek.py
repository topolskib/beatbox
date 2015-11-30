"""
Modul zawiera funkcje tworzace macierze reprezentujace dzwieki o roznych wlasnosciach.
"""
import numpy as np
from scipy import signal

def sin_custom(f,T,a=0,b=0):
    """
    Funkcja zwraca macierz reprezentujaca dzwiek stworzony za pomoca fali sinusoidalnej.
    
    Argumenty wejsciowe:
    f - czestotliwosc w Hz
    T - czas w sekundach
    a - wzgledny czas narastania liniowego dzwieku, 0<=a<=1
    b - wzgledny czas wygaszania liniowego dzwieku, 0<=b<=1
    """
    fs=44100
    t=np.linspace(0,T,T*fs)
    A=np.floor(a*fs*T)
    D=np.floor(b*fs*T)
    S1=np.linspace(0,1,A)
    S2=np.ones(T*fs-A-D)
    S3=np.linspace(1,0,D)
    S0=np.sin(2*np.pi*f*t)    
    return(np.hstack((S1,S2,S3))*S0)

def saw_custom(f,T,a=0,b=0):
    """
    Funkcja zwraca macierz reprezentujaca dzwiek stworzony za pomoca fali typu sawtooth.
    
    Argumenty wejsciowe:
    f - czestotliwosc w Hz
    T - czas w sekundach
    a - wzgledny czas narastania liniowego dzwieku, 0<=a<=1
    b - wzgledny czas wygaszania liniowego dzwieku, 0<=b<=1
    """
    fs=44100
    t=np.linspace(0,T,T*fs)
    A=np.floor(a*fs*T)
    D=np.floor(b*fs*T)
    S1=np.linspace(0,1,A)
    S2=np.ones(T*fs-A-D)
    S3=np.linspace(1,0,D)
    S0=signal.sawtooth(2 * np.pi * f * t)    
    return(np.hstack((S1,S2,S3))*S0)
def sq_custom(f,T,a=0,b=0):
    """
    Funkcja zwraca macierz reprezentujaca dzwiek stworzony za pomoca fali typu square.
    
    Argumenty wejsciowe:
    f - czestotliwosc w Hz
    T - czas w sekundach
    a - wzgledny czas narastania liniowego dzwieku, 0<=a<=1
    b - wzgledny czas wygaszania liniowego dzwieku, 0<=b<=1
    """
    fs=44100
    t=np.linspace(0,T,T*fs)
    A=np.floor(a*fs*T)
    D=np.floor(b*fs*T)
    S1=np.linspace(0,1,A)
    S2=np.ones(T*fs-A-D)
    S3=np.linspace(1,0,D)
    S0=signal.square(2 * np.pi * f * t)
    return(np.hstack((S1,S2,S3))*S0)

def custom_sound(type_of, attack, decay, cutoff, coef, time, freq):
    """
    Funkcja zwraca macierz reprezentujaca dzwiek stworzony za pomoca kombinacji roznych fal.
    
    Argumenty wejsciowe:
    type_of - wektor reprezentujacy typt fal skladowych. 
    
    attack - wektor wzglednych czasow narastania liniowego kolejnych dzwiekow, 0<=a<=1 dla a in attack
    
    decay - wektor wzglednych czasow wygaszania liniowego kolejnych dzwiekow, 0<=d=1 dla d in decay
    
    cutoff - liczba reprezuntajaca wzgledny moment uciecia dzwieku. Wazne - parametry attack i decay odnosza sie do czasu przd ucieciem.
    
    coef - wspolczynniki przy sumie kolejnych skladowych - jesli chcemy, zeby pierwsza skladowa byla dwa razy glosniejsza     
    niz druga, to dajemy [1,2]. 
    
    time - czas trwania w sekundach
    
    freq - czestotliwosc w Hz
    
    Funkcja na koncu normuje macierz do 1, w celu wyeliminowania przesterow.
    """
    dzw = np.zeros(time*44100)
    l=0
    for i in type_of:
        if i=="sin":
            dzw+= coef[l]*sin_custom(freq,time,attack[l],decay[l])
        if i=="sq":
            dzw+= coef[l]*sq_custom(freq,time,attack[l],decay[l])
        if i=="saw":
            dzw+= coef[l]*saw_custom(freq,time,attack[l],decay[l])
        l+=1    
    dzw[(1-cutoff)*time*44100 -1:]==0
    dzw = np.repeat(dzw,2).reshape(len(dzw),2)
    dzw = dzw/np.amax(dzw)
    return(dzw)
