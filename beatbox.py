#!/usr/bin/env python3
import sys
import ttv
import pyglet
import os
import numpy as np
import zipfile


dostepne = []
for i in os.walk("./"):
    if (("song.txt" in i[2]) or ("drum.py" in i[2])):
        dostepne = np.append(dostepne,i[0][2:])
    if i[0] == "./":
        for j in i[2]:
            if j[-4:]==".zip":
                dostepne = np.append(dostepne,j)
if len(sys.argv)==1:
    print("Dostepne moduly:")
    print(dostepne)
    dir = input("Wpisz nazwe modulu \n")
else:
    dir = sys.argv[1]
while( not(dir in dostepne)):
    print("Modul nie istnieje. Dostepne moduly:")
    print(dostepne)
    dir = input("Wpisz poprawna nazwe modulu: \n")
name = dir
dir = './' + dir

if dir[-4:] == '.zip':
    name = dir[:-4]
    zipdir = zipfile.ZipFile(file = dir)
    zipdir.extractall('/tmp/')
    dir = '/tmp/' + dir[2:-4]
    for i in os.walk(dir):
        if not("song.txt" in i[2]):
            sys.exit("Archiwum nie zawiera piosenki")
if dir!="./drum_machine":
    d = open(dir + '/defs.txt', 'r')
    dictionary =  eval(d.read())
    d.close()
    bpm = dictionary['bpm']
    ttv.make_song(dir,bpm,name)

elif dir == "./drum_machine":
    d=open("./drum_machine/drum.py")
    exec(d.read())


