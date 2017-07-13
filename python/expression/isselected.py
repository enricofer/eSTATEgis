from qgis.utils import iface

@qgsfunction(args=0, group='Custom')
def isSelected(value1,feature, parent):
    selected_ids = []
    for f in iface.activeLayer().selectedFeatures()
        selected_ids = f.id()
    return feature.id() in selected_ids
