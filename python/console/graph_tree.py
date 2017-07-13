from qgis.core import QGis, QgsMapLayerRegistry, QgsFeature, QgsVectorLayer

def touchesLayer(point, exclude_id, layer):
    for feature in layer.getFeatures():
        vertex_list = feature.geometry().asPolyline()
        if feature.id() != exclude_id and point.compare(vertex_list[0]) or point.compare(vertex_list[-1]):
            return True
    return False

intersectionLayer = QgsVectorLayer("Point?crs=epsg:3857&field=rif_id:integer", "nodi", "memory")
if layer.geometryType() == QGis.Line:
    features = []
    for feature in layer.getFeatures():
        vertex_list = feature.geometry().asPolyline()
        for node in (vertex_list[0], vertex_list[-1]):
            if touchesLayer(node, feature.id(), layer):
                new_feature = QgsFeature(intersectionLayer.pendingFields())
                new_feature.setAttribute('rif_id',feature.id())
                new_feature. setGeometry(QgsGeometry.fromPoint(node))
                features.append(new_feature)
    intersectionLayer.dataProvider().addFeatures(features)
    QgsMapLayerRegistry.instance().addMapLayer(intersectionLayer)
