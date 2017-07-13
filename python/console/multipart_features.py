l = iface.activeLayer()
iter = l.getFeatures()
geoms = []
for feature in iter:
    geom = feature.geometry()
    if geom.isMultipart():
        l.select(feature.id())
        geoms.append(geom)

print ('%i multipart features') % len(geoms)