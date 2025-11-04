import matplotlib
matplotlib.use('QtAgg')
import matplotlib.pyplot as plt

import cv2 as cv2
import os as os
import numpy as np
from random import randint
from time import time
"""
nameordner = input("Name: ")
os.mkdir(nameordner)
"""
start = time()
def genAdder(werte1,werte2,blendSec,fps):
    x = np.array([(werte2-werte1)/(blendSec*fps)])
    return x
def add(wert,werte1,werte2,blendSec,fps,s):
    x = np.array([(genAdder(werte1,werte2,blendSec,fps)*s+wert)])
    return x
def genPicTureVal(werte,blendSec,fps):
    #enthält alle matritzen 
    geswerte = np.array([[werte[0]]])
    
    for i in range(np.shape(werte)[0]):
        try:
            
            
            for s in range(blendSec*fps):
                
                geswerte = np.vstack((geswerte,add(werte[i],werte[i],werte[i+1],blendSec,fps,s)))
                
        except IndexError:
            pass
    print(geswerte)
    return geswerte
def genSaveDia(werte,punkte,ordnername,may,step):
    
    
    os.mkdir(ordnername)
    x = np.array([])
    for i in range(np.shape(punkte)[0]):
        x = np.append(x,i)
    
    for i in range(np.shape(werte)[0]):
        """ print(werte[i][0][0])"""
        
        plt.plot(werte[i][0])
       
        plt.scatter(x,punkte)
        plt.yticks(np.arange(0,may+step,step))
        plt.savefig(ordnername+"/"+str(i)+".png")
        print(werte[i][0])
        plt.clf()



def genVideo(pfad,fps):
    # 🔹 Ordner mit PNG-Bildern
    image_folder = pfad    # z. B. ./frames/
    output_file = 'video.mp4'    # Name des Videos
                        # Bildrate

    # 🔹 Alle PNG-Dateien sortieren
    images = [img for img in os.listdir(image_folder) if img.endswith('.png')]
    """images.sort()"""

    # 🔹 Erstes Bild lesen, um die Größe zu bestimmen
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape
    size = (width, height)

    # 🔹 VideoWriter initialisieren
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')   # Codec für MP4
    out = cv2.VideoWriter(output_file, fourcc, fps, size)

    # 🔹 Alle Frames hinzufügen
    for filename in images:
        frame = cv2.imread(os.path.join(image_folder, filename))
        out.write(frame)

    out.release()

werte = np.array([[3,3],[3,3],[3,3],[3,3],[3,3],[3,3],[3,3]])
werte = np.array([[33,70,53,33,70,53,33,70,53,33,70,53,33,70,53,33,70,53,33,70,53,33,70,53,33,70,53,33,70,53]])
mini = np.array([[]])
for i in range(8):
    mini = np.array([])
    for s in range(30):
        mini = np.append(mini,randint(0,100))
        print(mini)
    werte = np.vstack((werte,mini))
blendSec = 3
fps = 30

x = genPicTureVal(werte,blendSec,fps)
genSaveDia(x,np.array([3,2,8,3,2,62,23,57,21,38,3,2,8,3,2,62,23,57,21,38,3,2,8,3,2,62,23,57,21,38]),"Video",100,10)

genVideo("Video",30)
print(str(time()-start)+" Sekunden")
print(x)