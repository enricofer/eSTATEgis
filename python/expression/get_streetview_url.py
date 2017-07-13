"""
Define new functions using @qgsfunction. feature and parent must always be the
last args. Use args=-1 to pass a list of values as arguments
"""

from qgis.core import *
from qgis.gui import *
from qgis.utils import iface
import math

@qgsfunction(args=0, group='Custom', usesgeometry=True)
def get_streetview_img(value1, feature, parent):
    vettore = feature.geometry().asPolyline()
    fromP = vettore[0]
    toP = vettore[-1]
    location = '%f,%f' % (transformToWGS84(fromP).y(),transformToWGS84(fromP).x())
    head = heading(fromP,toP)
    size = '600x300'
    key = 'AIzaSyDOPpymqbVXrKcfsYOa48Dsbe6MQVrAgng'
    url = 'https://maps.googleapis.com/maps/api/streetview'
    url += "?location=%s&size=%s&key=%s&heading=%f" % (location,size,key,head)
    return url

def heading(fromP, toP):
    result = math.atan2((toP.x() - fromP.x()),(toP.y() - fromP.y()))
    result = math.degrees(result)
    return (result + 360) % 360
		
def transformToWGS84(pPoint):
    # transformation from the current SRS to WGS84
    crcMappaCorrente = iface.mapCanvas().mapRenderer().destinationCrs() # get current crs
    crsSrc = crcMappaCorrente
    crsDest = QgsCoordinateReferenceSystem(4326)  # WGS 84
    xform = QgsCoordinateTransform(crsSrc, crsDest)
    return xform.transform(pPoint) # forward transformation: src -> dest
