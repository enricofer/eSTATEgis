##Linee=vector line
##nodi=output vector
##grafo=output vector

from qgis.core import QgsGeometry, QgsField, QgsFeature, QGis 
from PyQt4.QtCore import QVariant
from processing.tools.vector import VectorWriter

def aggiungi_nodo(nuovo_nodo):
    for i,nodo in enumerate(lista_nodi):
        if nodo.compare(nuovo_nodo):
            return i
    lista_nodi.append(nuovo_nodo)
    return len(lista_nodi)-1

linee_layer = processing.getObject(Linee)

grafo_fields = [
    QgsField("rif_id", QVariant.Int), 
    QgsField("in_id", QVariant.Int), 
    QgsField("out_id", QVariant.Int)
]
grafo_writer = VectorWriter(grafo, None, grafo_fields, QGis.WKBMultiLineString, linee_layer.crs())

nodi_fields = [QgsField("nodo_id", QVariant.Int)]
nodi_writer = VectorWriter(nodi, None, nodi_fields, QGis.WKBMultiPoint, linee_layer.crs())

i = 0
n = linee_layer.featureCount()
lista_nodi = []
progress.setText("Individuazione dei vertici degli archi del grafo ...")

for k,feature in enumerate(processing.features(linee_layer)):
    progress.setPercentage(int(100*i/n))
    i += 1
    lista_vertici = feature.geometry().asPolyline()
    grafo_feature = QgsFeature()
    attributi =[feature.id()]
    grafo_feature.setGeometry(feature.geometry())
    for campo, estremo in ({1:lista_vertici[0],2:lista_vertici[-1]}).items():
        id_nodo = aggiungi_nodo(estremo)
        attributi.append(id_nodo)
    grafo_feature.setAttributes(attributi)
    grafo_writer.addFeature(grafo_feature)

i = 0
n = len(lista_nodi)
progress.setText("Creazione dei nodi ...")

for i, nodo in enumerate(lista_nodi):
    progress.setPercentage(int(100*i/n))
    nodo_feature = QgsFeature()
    nodo_feature.setAttributes([i])
    nodo_feature.setGeometry(QgsGeometry.fromPoint(nodo))
    nodi_writer.addFeature(nodo_feature)

del nodi_writer
del grafo_writer