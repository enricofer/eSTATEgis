from qgis.utils import iface
from qgis.core import QgsGeometry, QgsPoint

@qgsfunction(args=0, group='Custom')
def mapCenter(value1,feature, parent):
  x = iface.mapCanvas().extent().center().x()
  y = iface.mapCanvas().extent().center().y()
  return QgsGeometry.fromPoint(QgsPoint(x,y))
