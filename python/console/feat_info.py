from qgis.core import QGis, QgsPoint
#layer = iface.addVectorLayer("/path.shp", "nome", "ogr")
layer = iface.activeLayer() #caricamento
if not layer or not layer.isValid():
  print "Layer non valido!"
QgsMapLayerRegistry.instance().addMapLayer(layer) #registrazione
informazioni=[]
for feature in layer.getFeatures(): #accesso alle features
    info = [feature.id()]
    geom = feature.geometry()
    if geom.type() == QGis.Point:
        info.append("distanza")
        info.append(geom.distance(QgsPoint(0,0)))
    elif geom.type() == QGis.Line:
        info.append("Lunghezza")
        info.append(geom.length())
    elif geom.type() == QGis.Polygon:
        info.append("Area")
        info.append(geom.area)
    info += feature.attributes()
    informazioni.append(info)
print informazioni
