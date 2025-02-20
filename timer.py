import time
from random import *
demande=False
def horloge():
    global demande
    while True:
        for i in range(24):
            if i<10:
                i="0"+str(i)
            for e in range(60):
                if e<10:
                    e="0"+str(e)
                time.sleep(1)
                print(i,":",e,sep='')
horloge()
