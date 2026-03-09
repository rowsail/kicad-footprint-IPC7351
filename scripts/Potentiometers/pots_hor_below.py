#
# SCRIPT to generate 3D models
#



 # Potentiometer_Piher_T-16L_Single_Vertical_Hole
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-0.5'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-13.0'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '3.0'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '16.0'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# clbody_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var clbody_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '10.0'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'clbody_fab')
# ctbody_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var ctbody_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-5.0'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'ctbody_fab')
# cdbody_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var cdbody_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '16'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'cdbody_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A8', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B8', '7'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'dscrew')
# dshaft
App.ActiveDocument.Spreadsheet.set('A9', 'var dshaft = '); App.ActiveDocument.Spreadsheet.set('B9', '4'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dshaft')
# rmx
App.ActiveDocument.Spreadsheet.set('A10', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B10', '7.5'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A11', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B11', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A12', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B12', '0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A13', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B13', '10.0'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A14', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B14', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A15', 'var height = '); App.ActiveDocument.Spreadsheet.set('B15', '21'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'height')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A16', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A17', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B17', '15'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A18', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B18', '0'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A19', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B19', '-10.0'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_T-16L_Single_Vertical_Hole.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_T-16L_Single_Vertical_Hole.FCStd")
print("created Potentiometer_Piher_T-16L_Single_Vertical_Hole")


 # Potentiometer_Bourns_PTV09A-1_Single_Vertical
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '1'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-7.35'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '12.0'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '9.7'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# clbody_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var clbody_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '7.5'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'clbody_fab')
# ctbody_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var ctbody_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-2.5'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'ctbody_fab')
# cdbody_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var cdbody_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'cdbody_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A8', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B8', '6.8'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'dscrew')
# dshaft
App.ActiveDocument.Spreadsheet.set('A9', 'var dshaft = '); App.ActiveDocument.Spreadsheet.set('B9', '6'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dshaft')
# rmx
App.ActiveDocument.Spreadsheet.set('A10', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B10', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A11', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B11', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A12', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B12', '0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A13', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B13', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A14', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B14', '0.7'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A15', 'var height = '); App.ActiveDocument.Spreadsheet.set('B15', '15.5'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'height')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A16', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A17', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B17', '8.8'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A18', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B18', '0'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A19', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B19', '-5.0'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_PTV09A-1_Single_Vertical.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_PTV09A-1_Single_Vertical.FCStd")
print("created Potentiometer_Bourns_PTV09A-1_Single_Vertical")


 # Potentiometer_Alps_RK09K_Single_Vertical
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '1'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-7.4'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '12.0'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '9.8'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# clbody_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var clbody_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '7.5'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'clbody_fab')
# ctbody_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var ctbody_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-2.5'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'ctbody_fab')
# cdbody_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var cdbody_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'cdbody_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A8', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B8', '6.5'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'dscrew')
# dshaft
App.ActiveDocument.Spreadsheet.set('A9', 'var dshaft = '); App.ActiveDocument.Spreadsheet.set('B9', '6'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dshaft')
# rmx
App.ActiveDocument.Spreadsheet.set('A10', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B10', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A11', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B11', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A12', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B12', '0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A13', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B13', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A14', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B14', '0.7'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A15', 'var height = '); App.ActiveDocument.Spreadsheet.set('B15', '12.0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'height')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A16', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A17', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B17', '8.8'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A18', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B18', '0'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A19', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B19', '-5.0'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Alps_RK09K_Single_Vertical.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Alps_RK09K_Single_Vertical.FCStd")
print("created Potentiometer_Alps_RK09K_Single_Vertical")


 # Potentiometer_Alps_RK09L_Single_Vertical
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '1'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-8.55'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '11.35'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '12.1'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# clbody_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var clbody_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '7.5'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'clbody_fab')
# ctbody_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var ctbody_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-2.5'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'ctbody_fab')
# cdbody_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var cdbody_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'cdbody_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A8', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B8', '9'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'dscrew')
# dshaft
App.ActiveDocument.Spreadsheet.set('A9', 'var dshaft = '); App.ActiveDocument.Spreadsheet.set('B9', '6'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dshaft')
# rmx
App.ActiveDocument.Spreadsheet.set('A10', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B10', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A11', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B11', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A12', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B12', '0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A13', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B13', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A14', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B14', '0.7'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A15', 'var height = '); App.ActiveDocument.Spreadsheet.set('B15', '11.6'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'height')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A16', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A17', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B17', '9.5'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A18', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B18', '0'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A19', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B19', '-5.0'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Alps_RK09L_Single_Vertical.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Alps_RK09L_Single_Vertical.FCStd")
print("created Potentiometer_Alps_RK09L_Single_Vertical")


 # Potentiometer_Alps_RK09L_Double_Vertical
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '1'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-8.55'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '11.35'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '12.1'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# clbody_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var clbody_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '7.5'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'clbody_fab')
# ctbody_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var ctbody_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-2.5'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'ctbody_fab')
# cdbody_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var cdbody_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'cdbody_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A8', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B8', '9'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'dscrew')
# dshaft
App.ActiveDocument.Spreadsheet.set('A9', 'var dshaft = '); App.ActiveDocument.Spreadsheet.set('B9', '6'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dshaft')
# rmx
App.ActiveDocument.Spreadsheet.set('A10', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B10', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A11', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B11', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A12', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B12', '0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A13', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B13', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A14', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B14', '0.7'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A15', 'var height = '); App.ActiveDocument.Spreadsheet.set('B15', '11.6'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'height')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A16', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A17', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B17', '9.5'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A18', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B18', '0'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A19', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B19', '-5.0'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Alps_RK09L_Double_Vertical.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Alps_RK09L_Double_Vertical.FCStd")
print("created Potentiometer_Alps_RK09L_Double_Vertical")


 # Potentiometer_Bourns_3339P_Vertical
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-6.35'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '7.62'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# clbody_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var clbody_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'clbody_fab')
# ctbody_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var ctbody_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-2.54'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'ctbody_fab')
# cdbody_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var cdbody_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '7.62'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'cdbody_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A8', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B8', '5'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'dscrew')
# dshaft
App.ActiveDocument.Spreadsheet.set('A9', 'var dshaft = '); App.ActiveDocument.Spreadsheet.set('B9', '0'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dshaft')
# rmx
App.ActiveDocument.Spreadsheet.set('A10', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B10', '-2.54'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A11', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B11', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A12', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B12', '0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A13', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B13', '5.08'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A14', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B14', '0.39999999999999997'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A15', 'var height = '); App.ActiveDocument.Spreadsheet.set('B15', '6.35'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'height')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A16', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A17', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B17', '15'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A18', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B18', '0'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A19', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B19', '-5.08'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3339P_Vertical.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3339P_Vertical.FCStd")
print("created Potentiometer_Bourns_3339P_Vertical")


 # Potentiometer_Bourns_3339H_Vertical
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '3.5921024484276614'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-5.6060512242138305'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '7.62'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# clbody_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var clbody_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '1.7960512242138307'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'clbody_fab')
# ctbody_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var ctbody_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-1.796051224213831'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'ctbody_fab')
# cdbody_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var cdbody_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '7.62'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'cdbody_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A8', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B8', '5'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'dscrew')
# dshaft
App.ActiveDocument.Spreadsheet.set('A9', 'var dshaft = '); App.ActiveDocument.Spreadsheet.set('B9', '0'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dshaft')
# rmx
App.ActiveDocument.Spreadsheet.set('A10', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B10', '1.7960512242138307'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A11', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B11', '1.7960512242138307'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A12', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B12', '0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A13', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B13', '3.5921024484276614'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A14', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B14', '0.39999999999999997'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A15', 'var height = '); App.ActiveDocument.Spreadsheet.set('B15', '6.35'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'height')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A16', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A17', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B17', '15'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A18', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B18', '0'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A19', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B19', '-3.5921024484276614'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3339H_Vertical.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3339H_Vertical.FCStd")
print("created Potentiometer_Bourns_3339H_Vertical")


 # Potentiometer_Vishay_T7-YA_Single_Vertical
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-2.54'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-6.04'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '7.0'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# clbody_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var clbody_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '-0.040000000000000036'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'clbody_fab')
# ctbody_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var ctbody_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-2.54'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'ctbody_fab')
# cdbody_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var cdbody_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '7'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'cdbody_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A8', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B8', '4.1'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'dscrew')
# dshaft
App.ActiveDocument.Spreadsheet.set('A9', 'var dshaft = '); App.ActiveDocument.Spreadsheet.set('B9', '0'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dshaft')
# rmx
App.ActiveDocument.Spreadsheet.set('A10', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B10', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A11', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B11', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A12', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B12', '0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A13', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B13', '5.08'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A14', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B14', '0.5'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A15', 'var height = '); App.ActiveDocument.Spreadsheet.set('B15', '5.85'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'height')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A16', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A17', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B17', '15'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A18', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B18', '0'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A19', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B19', '-5.08'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Vishay_T7-YA_Single_Vertical.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Vishay_T7-YA_Single_Vertical.FCStd")
print("created Potentiometer_Vishay_T7-YA_Single_Vertical")


 # Potentiometer_Bourns_3386P_Vertical
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-4.78'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-7.305'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '9.53'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '9.53'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# clbody_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var clbody_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '-0.8900000000000006'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'clbody_fab')
# ctbody_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var ctbody_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-2.54'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'ctbody_fab')
# cdbody_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var cdbody_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'cdbody_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A8', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B8', '3.15'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'dscrew')
# dshaft
App.ActiveDocument.Spreadsheet.set('A9', 'var dshaft = '); App.ActiveDocument.Spreadsheet.set('B9', '0'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dshaft')
# rmx
App.ActiveDocument.Spreadsheet.set('A10', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B10', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A11', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B11', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A12', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B12', '0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A13', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B13', '5.08'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A14', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B14', '0.5'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A15', 'var height = '); App.ActiveDocument.Spreadsheet.set('B15', '4.83'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'height')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A16', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A17', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B17', '15'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A18', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B18', '0'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A19', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B19', '-5.08'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3386P_Vertical.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3386P_Vertical.FCStd")
print("created Potentiometer_Bourns_3386P_Vertical")


 # Potentiometer_Bourns_3386F_Vertical
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-2.1099999999999994'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-7.305'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '9.53'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '9.53'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# clbody_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var clbody_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '1.7800000000000002'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'clbody_fab')
# ctbody_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var ctbody_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-2.54'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'ctbody_fab')
# cdbody_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var cdbody_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'cdbody_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A8', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B8', '3.15'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'dscrew')
# dshaft
App.ActiveDocument.Spreadsheet.set('A9', 'var dshaft = '); App.ActiveDocument.Spreadsheet.set('B9', '0'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dshaft')
# rmx
App.ActiveDocument.Spreadsheet.set('A10', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B10', '5.08'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A11', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B11', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A12', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B12', '0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A13', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B13', '5.08'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A14', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B14', '0.5'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A15', 'var height = '); App.ActiveDocument.Spreadsheet.set('B15', '4.83'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'height')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A16', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A17', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B17', '15'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A18', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B18', '0'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A19', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B19', '-5.08'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3386F_Vertical.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3386F_Vertical.FCStd")
print("created Potentiometer_Bourns_3386F_Vertical")


 # Potentiometer_Vishay_T73YP_Vertical
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-3.56'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-5.84'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '7.0'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '6.6'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# clbody_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var clbody_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '0.23999999999999977'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'clbody_fab')
# ctbody_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var ctbody_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-2.54'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'ctbody_fab')
# cdbody_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var cdbody_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'cdbody_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A8', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B8', '3'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'dscrew')
# dshaft
App.ActiveDocument.Spreadsheet.set('A9', 'var dshaft = '); App.ActiveDocument.Spreadsheet.set('B9', '0'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dshaft')
# rmx
App.ActiveDocument.Spreadsheet.set('A10', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B10', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A11', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B11', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A12', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B12', '0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A13', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B13', '5.08'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A14', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B14', '0.5'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A15', 'var height = '); App.ActiveDocument.Spreadsheet.set('B15', '7'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'height')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A16', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A17', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B17', '15'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A18', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B18', '0'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A19', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B19', '-5.08'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Vishay_T73YP_Vertical.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Vishay_T73YP_Vertical.FCStd")
print("created Potentiometer_Vishay_T73YP_Vertical")
