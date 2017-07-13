# ESERCITAZIONE

abbiamo un dataset puntuale (nel nostro caso un dataset si siti contaminati)
e vogliamo realizzare un altante in a4 da stampare fronte retro dove ogni punto sia rappresentato in una planimetria di dettaglio, una planimetria di inquadramento, sia identificato con un id e riporti un'immagine panoramica di riferimento.

* creare un atlante
* settare la posizione degli oggetti per il fronte retro
* scaricare un'immagine statica di google streetview
* scaricare la viabilità pubblica da OSM
* creare i punti di vista dalla viabilità pubblica con un virtual layer
* preparare una funzione personalizzata in python per impostare l'url di streetview
* inserire l'immagine nell'atlante

---

## creare un altlante
* aprire il progetto di QGIS test_project.qgs contenuto nel nel [dataset di esempio](./dataset.zip)
* aprire il compositore stampe A4
* selezionare il layer di guida per l'atlante

## settaggio per il fronte_retro
* selezionare un oggetto sul compositore, selezionare lo slot "posizione e dimensione" ed attivare il pulsante felle espressioni
* inserire la seguente espressione:

```
case
 when @atlas_featureid % 2 = 0 then 240
 else 15
end
``` 
* attivazione dell'atlante

---

## scaricare un'immagine statica di google streetview
Google consente di scaricare un'immagine statica di google streetview semplicemente inserendo tra i parametri la latitudine e la longitudinee l'orientamento: (bisogna acquisire una [api key](https://developers.google.com/maps/documentation/streetview/))
<img src="vista.png" width="100%" />

[esempio: https://maps.googleapis.com/maps/api/streetview?location=45.406695,11.875723&size=600x300&key=AIzaSyDOPpymqbVXrKcfsYOa48Dsbe6MQVrAgng&heading=320](https://maps.googleapis.com/maps/api/streetview?location=45.406695,11.875723&size=600x300&key=AIzaSyDOPpymqbVXrKcfsYOa48Dsbe6MQVrAgng&heading=320)

---

## definire i punti di vista e l'orientamento dell'immagine

i parametri fondamentali richiesti sono la latidudine e la longitudine e l'orientamento dell'immagine. Possiamo ricavare questi dati definendo un layer lineare ed usando il primo vertice come punto di vista e l'ultimo vertice come punto di mira, ricavando da questi punti l'orientamento in gradi con origine Nord.

[codice della funzione per espressioni](./python/expression/get_streetview_url.py)

testare la funzione creando o caricando un layer lineare e provando la funzione sulla tabella degli attributi
---

## generare automaticamente i vettori dei punti di vista dalla pubblica viabilità

facciamo riferimento al tutorial di [Totò Fiandaca](https://pigrecoinfinito.wordpress.com/2017/04/28/qgis-minima-distanza-tra-punti-e-linee/)

* importiamo un grafo della pubblica viabilità di padova da OSM (lo riproiettiamo su EPSG:3003 e lo denominiamo grafo_stradale) e lo usiamo per ricavere le distanze minime dai siti contaminati:

```
select p.Id, ST_ShortestLine (l.geometry, p.geometry) as geometry ,st_length (ST_ShortestLine (l.geometry, p.geometry)) as lungh_m
from punti as  p, grafo_stradale as l
group by p.Id
having min ( st_length(shortestline (p.geometry, l.geometry)))
``` 

--

## inserimento dell'immagine nell'atlante

ottenuti i vettori dei punti di vista si può far girare la funzione su tutte le feature ed inserire un'immagine nell'atlante
si può verificare su una tabella ed inserire nel contenuto di un oggetto testuale come HTML

---

#### Master di II livello in "GIScience e sistemi a pilotaggio remoto per la gestione integrata del territorio e dellerisorse naturali"
#### eSTATE gis 2017
#### Workshop "Geoprocessing in python con QGIS"

#### (C) 2017 Enrico Ferreguti
#### I contenuti sono distribuiti con licenza [CC BY-SA](https://creativecommons.org/licenses/by-sa/3.0/it/) ![](CC-BY-SA_icon.svg.png)


* [sezione 1 - introduzione](./workshop_0.html)
* [sezione 2 - estendere QGIS](./estategis_2.html)
* [sezione 3 - il linguaggio Python](./workshop_1.html)
* [sezione 4 - PyQt / PyQGIS](./workshop_2.html)
* [sezione 5 - PyQGIS per esempi](./workshop_3.html)
* [sezione 5 - ESERCITAZIONE](./estategis_3.html)
