import numpy as np
from random import randint
from time import time
import werte as val
"""
die formel die die rechnungen für neuronen ausführt 
wert ist der eingabe wert
bias der adder wert wie viel zum neuron addiert wird
multiplier um viel der eingabe wert multipliziert wird
relu der wert der überschritten werden muss damit das neuron feuert
reluels der wert den das neuron feuert wenn es nicht feuert
"""
def formel(wert,bias,multiplier,relu):
    x = wert*multiplier+bias
    if x >=relu:
        return x
    else:
        return 0
    

#funktion die das netz ausführt
"""
1.Eine variable die immer um das ergebniss der formel fürs aktuelle neuron mit dem x ten wert der vorherigen liste addiert wird
damit dieser wert zusammengefasst in die tampslist hinzugefügt werden kann

2.Eine schleife die so lange an hält wie viele schichten das netz hat 
diese schleife hat den zweck alle schichten durchzugehen


3.Eine variable die die ergebnisse der einzelnen neuronen rechnungen temporär speichert


4.Eine Schleife die solange anhält wie viele neuronen die nächste schicht hat
damit die durchgegangen werden und die für die formel angewendtet werden können 

5.Setzt den adder wieder auf 0


6.Eine schleife die so lange geht wie die vorherige schicht damit alle ergebniss dieser schicht weitergegeben
werden


7.



"""

   
def genneuronen( neuronenanz,schichtenanz, parameteranz):
    return np.ones((schichtenanz*sum(neuronenanz)*parameteranz))
    


def run(werte,netz,neuronenanz,schichtanz):
    print("run:"+str(netz))
    cord = 0
    for i in range(schichtanz):
        adder = 0
        tempwert = np.array([])
        for x in range(neuronenanz[i]):
            
            for s in range(len(werte)):
                adder +=  formel(werte[s],netz[cord*3+1],netz[cord*3],netz[cord*3+2])
                
        
                cord += 0
            tempwert = np.append(tempwert,adder)
        werte = tempwert

    return tempwert
def fehlerwert(expectedvalue,calcedvalue):
    return (sum(expectedvalue)/sum(calcedvalue))-1






def error(netz,eingabewerte,ausgabewerte,neuronenanz,schichtanz):
    print("error:"+str(netz))
    errorvalue = np.array([])
    
    for x in range(len(eingabewerte)):
        calcedvalue = run(eingabewerte[x],netz,neuronenanz,schichtanz)
        errorvalue = np.append(errorvalue,fehlerwert(calcedvalue,ausgabewerte[x]))


    return sum(errorvalue)/len(errorvalue)


def thebest(netz,counttrainval,eingabewert,ausgabewert,learningrate,neuronenanz,schichtanz):
    changednetz = netz
    error = np.array([])
    temperror = np.array([])
    values = np.array([])
    for i in range(len(netz)):
        changednetz = netz
        for x in range(2):
            for s in range(counttrainval):
                if x == 0:
                    changednetz[i] += learningrate
                    temperror = 
                    
                else:
                    changednetz[i] -= learningrate
            


def optimize(netz,eingabewerte,ausgabewerte,neuronenanz,schichtanz,netzcount,cycle,betrag):
    #generriert multinetz
    multinetz = np.array([[]])
    for i in range(netzcount):
        if i== 0:
            multinetz = np.append(multinetz,netz)
        else:
            
            
            mininetz = np.random.rand(len(netz))
            multinetz = np.append(multinetz,mininetz)




zeit = time()
#test

"""
for i in range(1000):
    x = randint(1,100)
    werteliste = np.array([])
    neuronenanzahl = np.array([],dtype=int)
        
    for s in range(x):
        werteliste = np.append(werteliste,randint(1,4))
    neuronenanzahl = np.append(neuronenanzahl,len(werteliste))
    
    for v in range(x):
        neuronenanzahl = np.append(neuronenanzahl,randint(1,4))
    print("werte"+str(werteliste))
    print("neuronenanz"+str(neuronenanzahl))
    print(run(werteliste,genneuronen(neuronenanzahl,len(neuronenanzahl),3),neuronenanzahl,len(neuronenanzahl)))
print(time()-zeit)
"""

netz = np.array([1,1,1,1,1,1,1,1,1])
eingabewerte =np.array([[2,3],[2,3]])
ausgabewerte = np.array([[2],[2]])
neuronenanz = np.array([2,1])
schichtanz= 2
netzcount=6
cycle=10
betrag= 0.1
print(optimize(netz,eingabewerte,ausgabewerte,neuronenanz,schichtanz,netzcount,cycle,betrag))