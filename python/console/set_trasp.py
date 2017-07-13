def trasp(t=50):
    layer = iface.mapCanvas().currentLayer()
    if layer.layerTransparency() == t:
        layer.setLayerTransparency(0)  # int tra 0 e 100
    else:
        layer.setLayerTransparency(t)
    iface.mapCanvas().refresh()