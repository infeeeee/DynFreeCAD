import sys
freecad_bin_path = IN[0]
sys.path.append(freecad_bin_path)

try:
    errorReport = None


    from PySide2.QtWidgets import QApplication

    import FreeCAD
    import FreeCADGui

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    
    FreeCADGui.showMainWindow()

except:
    import traceback
    errorReport = traceback.format_exc()

if errorReport == None:
    output = []

    fc_version = FreeCAD.Version()
    sys_path = sys.path

    for outer in [fc_version, sys_path, FreeCAD, app]:
        output.append(outer)    

    OUT = output
else:
    OUT = errorReport
