import os

basedir = "/home/enrico/Dropbox/COMMESSE/ACQUE-INTERNE/01_QC"

for root,subfolders,files in os.walk(basedir):
    for file in files:
        filename, extension = os.path.splitext(file)
        if extension == ".shp":
            shp_file = os.path.join(root,file)
            print ("loading layer %s ...") % shp_file
            shp_layer = QgsVectorLayer(shp_file, filename, 'ogr')
            QgsMapLayerRegistry.instance().addMapLayer(shp_layer)