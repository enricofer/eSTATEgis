<!-- $theme: default -->

# PYTHON

Python è un linguaggio di programmazione potente e divertente, che trova utilizzo sia nello sviluppo di applicazioni web che di software desktop. E' possibile ritrovarlo come interfaccia di programmazione di librerie tipo GDAL/OGR, JTS e GEOS. Le caratteristiche principali sono:

* chiarezza e leggibilità della sintassi
* orientazione ad oggetti intuitiva
* gestione degli errori in fase di esecuzione
* tipi dato dinamici e di alto livello
* codice modulare e riusabile
* disponibilità sterminata di librerie immediatamente disponibili (https://pypi.python.org/pypi)

---
### VERSIONI
* QGIS2 > Python 2.7
* QGIS3 > Pyhton 3.5
* [informazioni sulla Migrazione](https://docs.python.org/3/howto/pyporting.html)

### CONSOLE

![console](./console.png)

consente di interagire con QGIS usando Python

### PRIMO CODICE

```python
>>> print ("CIAO DA QGIS!") <invio>
```
---

## Numeri

```python
10 	#integer (numero intero)
25.45	#float (numero decimale)

# Per trasformare una stringa in numero
# o troncare un float 
int("10")
int(34.354)

# L'aritmetica ha una notazione convenzionale
10 + 1 
10 * 5
10*(45/3)+8*17

# Divisione tra interi in python 2
5 / 2 #2

# se uno dei numeri è float il risultato è float
10 / 3.0

# questo è equivalente a sopra
10 / float(3)

# in python 3 il risultato è implicito
```
---

## Stringhe
```python
"Ciao da QGIS!"

# Concatenare le stringhe
"Ciao" + " " + "da QGIS!"

# Formattazione di stringhe
"Ciao da %s" % "QGIS!"

# Il testo è racchiuso da virgolette singole o doppie
'Python è "divertente"'

# Stringhe multi-linea
print """Questa stringa
è suddivisa in
varie righe"""

# Caratteri speciale come a capo, la tabulazione o la barra inversa,
# possono essere inseriti per mezzo di una sequenza di escape che inizia
# con una barra inversa "\"

print "Questa stringa\nviene stampata\nin tre righe"
print "C:\\Users\\enrico"

# Si può usare una stringa grezza tralasciando le sequenze di escape
print r"C:\\Users\\enrico"

#Uso del set di caratteri esteso (unicode - UTF8) (Python 2)
print (u"questo è qgis")
```

---

## Operatori Logici *Boolean*
```python
True

False (None, [], {})

# operatori

not True # False

True and True # True

True and False # False

False and False # False

False or True # True

not (True or False) and True #False
```
---

## Variabili
```python

anno = "2017"

anno = 2017

print (anno)

anno_scorso = anno - 1

print (anno_scorso)

```
Le variabili in python hanno non sono "staticamente tipizzate", non devono essere dichiarate prima di usarle ne deve essere dichiarato il tipo. Sono degli oggetti che puntano a dati.

---

## Liste
una lista (list) e' un elenco ordinato di elementi
```python
l = [3, 5, 4, 2, 1]
m = [[[0,3],[4,6],[5,7]],[[4,5],[6,8]]]

# Accesso agli elementi per posizione
# il primo elemento è 0, gli indici negativi partono dalla fine

l[0]       #3
l[0:3]     #[3, 5, 4]
l[-1]      #1
l[2:-2]    #[4, 2]
l[3:]      #[2, 1]
l[:-2]     #[3, 5, 4, 2]
m[0][2][0] #5
m[1][1]    #[6,8]
```
la stessa notazione è valida per ricavare sottostringhe
```python
"abcdefghijklmnopqrstuvwxyz"[-5:] # "vwxyz"
```
---

## Dizionari
un dizionario (dict) è un insieme strutturato di dati
```python
d = {
    "chiave1": 10,
    "chiave2": 234.56,
    "chiave2": "contenuto",
    "chiave3": {
    	"chiave3_1": "abcdef",
        "chiave3_2": "xyz"
    }
}

d["chiave2"]               # 234.56
d["chiave3"]["chiave3_2"]  # "xyz"
```
---
## Manipolazione dei dati strutturati
```python
l0 = [] # lista vuota
l1 = [1, 2]
l2 = [3, 5, 6]

d0 = {} # dizionario vuoto
d1 = {"nome":"giuseppe", "anni": 50}

l1 + l2         # [1, 2, 3, 5, 6]
l1 + 4 + l3     # TypeError
l1.append(10)   # [1, 2, 3, 5, 6, 10]
l1.append(l2)   # [1, 2, [3, 5, 6]]
3 in l2         # True
3 in l1         # False
len(l1 + l2)    # 5

d1["cognome"] = 'verdi'
d1["anni"] = 60 # {"nome":"giuseppe","anni":60,"cognome":"verdi"}
d1.keys()       # ["cognome", "anni", "nome"]
d1.values()     # ["verdi", 60, "giuseppe"]
len(d1)         # 3
```
---

## Controllo del flusso
```python
latitude = 51.5
if latitude >= 0:
   zone_letter = 'N'
else:
   zone_letter = 'S'

print zone_letter
```

* l'indentazione è il sistema con cui Python raggruppa le istruzioni
* L'indentazione viene realizzata con spazi o tabulazioni
* ogni riga all'interno di un blocco base dev'essere indentata in ugual misura
* Usare un buon editor di testo per programmatori! 
---

## Cicli
```python
for carattere in "abcdefg":
    print (carattere)

for numero in [3, 5, 4, 2, 1]:
    print (numero)

testo = "abcdefg"
while testo:
    testo = testo[:-1]
    print (testo)
```
---

## Funzioni
```python
# Funzioni esistenti (o predefinite)
sorted([3, 5, 4, 2, 1])
len(l1 + l2)

# Definizione della propria funzione
def ZonaUtm(longitudine, latitudine):
    numero_zona = ((longitudine + 180) / 6) % 60 + 1
    if latitude >= 0:
        lettera_zona = 'N'
    else:
        lettera_zona = 'S'
    return '%d%s' % (int(numero_zona), lettera_zona)
    
# Uso della funzione
ZonaUtm(11.55,45)   # 32
```
---
## Moduli
```python
# Importa un modulo con chiamata ad una funzione contenuta
import math
math.floor(10.6)

# Importa singoli elementi da un modulo
from os import path
path.join(r'C:\Users', 'Matt')
```
l'organizzazione modulare è una delle caratteristiche del linguaggio. I moduli possono essere:
* predefiniti, già compresi nella dotazione di base del linguaggio
* esterni, contenuti nei path di sistema di Python (PATH, PYTHONPATH). Possono essere preimportati o importati da internet tramite pip/setuptools 
* definiti dall'utente in sottocartelle

---
## Programmazione ad oggetti

* Classe
    * tipo di dato composto definito dall'utente in metodi ad attributi.
* Istanziare
    * creare un'oggetto di una determinata classe.
* Istanza
    * un'oggetto creato che appartiene ad una classe.
* Membri di una classe
    * Metodi
       * funzioni che costituisce un comportamento dell'istanza
    * Attributi
       * valori attribuiti ad un'istanza.
* Costruttore
    * metodo usato per definire nuovi oggetti.
---
# Classi in Python
```python
class rettangolo:
   
   def __init__(self, l, h):
      self.l = l
      self.h = h
   
   def area(self)
      return l*h
   
   def perimetro(self)
      return(l+h)*2
   
   def scala(self, scala)
      self.l = l*scala
      self.h = h*scala
 
 r = rettangolo(10,5) #istanziazione di un oggetto rettangolo
 r.area()             #50
 r.scala(2)           
 r.perimetro()        #60
 r.l                  #20
 r.h                  #10
```   

---
---
# PyQGIS
QGIS è programmato in modo modulare in C++ ed espone classi e metodi di funzionamento in PyQGIS
```python
# iface è l'oggetto principale di QGIS da cui derivano
# tutti gli altri oggetti che ne permettono il funzionamento
# è un "singleton" un oggetto con unica istanza 
# della classe QgisInterface, istanziato come oggetto iface
iface.activeLayer().name()

# la maggior parte dei metodi richiamano altri oggetti
iface.activeLayer()

# quali metodi o attributi per un'oggetto:
dir(iface.activeLayer())
```   

---

## Risorse
* [Il tutorial ufficiale di Python](http://docs.python.it/html/tut/tut.html)
* [Pensare da informatico. Versione Python](http://www.python.it/doc/Howtothink/Howtothink-html-it/index.htm)
* [Dive into Python - Python per programmatori esperti](http://it.diveintopython.net/toc/index.html)
* [Google Python Course](https://developers.google.com/edu/python/)

## Riferimenti
* [Cheatsheet - riferimento rapido python 2.7](http://www.astro.up.pt/~sousasag/Python_For_Astronomers/Python_qr.pdf)
* [Cheatsheet - riferimento rapido python 3.5](https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf)
* [Python per esempi](https://github-production-release-asset-2e65be.s3.amazonaws.com/29447438/1da4d7ca-6837-11e6-8ab3-ae7821a7032a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20170615%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20170615T063202Z&X-Amz-Expires=300&X-Amz-Signature=504b5df4c21540c43f13c9fe6bd01a866031acbffff1f6827bf9fb8d6dbf49a7&X-Amz-SignedHeaders=host&actor_id=7544963&response-content-disposition=attachment%3B%20filename%3Dbeginners_python_cheat_sheet_pcc_all.pdf&response-content-type=application%2Foctet-stream )

---

#### Master di II livello in "GIScience e sistemi a pilotaggio remoto per la gestione integrata del territorio e dellerisorse naturali"
#### eSTATE gis 2017
#### Workshop "Geoprocessing in python con QGIS"

#### (C) 2017 Enrico Ferreguti
#### I contenuti sono distribuiti con licenza [CC BY-SA](https://creativecommons.org/licenses/by-sa/3.0/it/) ![](CC-BY-SA_icon.svg.png)

* [sezione 1 - introduzione](./workshop_0.html)
* [sezione 2 - il linguaggio Python](./workshop_1.html)
* [sezione 3 - PyQt / PyQGIS](./workshop_2.html)
* [sezione 4 - PyQGIS per esempi](./workshop_3.html)