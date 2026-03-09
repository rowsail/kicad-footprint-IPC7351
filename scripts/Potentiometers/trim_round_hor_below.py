#
# SCRIPT to generate 3D models
#



 # Potentiometer_Piher_PT-6-V_Vertical_Hole
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '0'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-5.65'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '6.3'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# clbody_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var clbody_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'clbody_fab')
# ctbody_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var ctbody_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-2.5'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'ctbody_fab')
# cdbody_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var cdbody_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '6.3'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'cdbody_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A8', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B8', '2'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'dscrew')
# dshaft
App.ActiveDocument.Spreadsheet.set('A9', 'var dshaft = '); App.ActiveDocument.Spreadsheet.set('B9', '1.8'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dshaft')
# rmx
App.ActiveDocument.Spreadsheet.set('A10', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B10', '5'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A11', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B11', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A12', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B12', '0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A13', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B13', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A14', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B14', '0.6000000000000001'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A15', 'var height = '); App.ActiveDocument.Spreadsheet.set('B15', '4'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'height')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A16', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A17', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B17', '15'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'mh_rmy')
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

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_PT-6-V_Vertical_Hole.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_PT-6-V_Vertical_Hole.FCStd")
print("created Potentiometer_Piher_PT-6-V_Vertical_Hole")


 # Potentiometer_Piher_PT-10-V10_Vertical_Hole
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '0'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-7.65'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '10.0'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# clbody_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var clbody_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '5'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'clbody_fab')
# ctbody_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var ctbody_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-2.6500000000000004'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'ctbody_fab')
# cdbody_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var cdbody_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '10.3'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'cdbody_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A8', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B8', '3.5'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'dscrew')
# dshaft
App.ActiveDocument.Spreadsheet.set('A9', 'var dshaft = '); App.ActiveDocument.Spreadsheet.set('B9', '3'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dshaft')
# rmx
App.ActiveDocument.Spreadsheet.set('A10', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B10', '10'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A11', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B11', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A12', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B12', '0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A13', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B13', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A14', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B14', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A15', 'var height = '); App.ActiveDocument.Spreadsheet.set('B15', '5.3'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'height')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A16', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A17', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B17', '15'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'mh_rmy')
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

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_PT-10-V10_Vertical_Hole.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_PT-10-V10_Vertical_Hole.FCStd")
print("created Potentiometer_Piher_PT-10-V10_Vertical_Hole")


 # Potentiometer_Piher_PT-10-V05_Vertical
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-2.65'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-7.65'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '10.0'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# clbody_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var clbody_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '2.5000000000000004'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'clbody_fab')
# ctbody_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var ctbody_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-2.5'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'ctbody_fab')
# cdbody_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var cdbody_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '10.3'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'cdbody_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A8', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B8', '3.5'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'dscrew')
# dshaft
App.ActiveDocument.Spreadsheet.set('A9', 'var dshaft = '); App.ActiveDocument.Spreadsheet.set('B9', '3'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dshaft')
# rmx
App.ActiveDocument.Spreadsheet.set('A10', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B10', '5'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A11', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B11', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A12', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B12', '0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A13', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B13', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A14', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B14', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A15', 'var height = '); App.ActiveDocument.Spreadsheet.set('B15', '5.3'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'height')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A16', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A17', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B17', '15'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'mh_rmy')
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

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_PT-10-V05_Vertical.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_PT-10-V05_Vertical.FCStd")
print("created Potentiometer_Piher_PT-10-V05_Vertical")


 # Potentiometer_Piher_PT-15-V02_Vertical_Hole
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '0'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-12.5'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '10.0'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# clbody_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var clbody_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '7.5'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'clbody_fab')
# ctbody_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var ctbody_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-5.0'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'ctbody_fab')
# cdbody_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var cdbody_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '15'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'cdbody_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A8', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B8', '6'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'dscrew')
# dshaft
App.ActiveDocument.Spreadsheet.set('A9', 'var dshaft = '); App.ActiveDocument.Spreadsheet.set('B9', '4.4'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dshaft')
# rmx
App.ActiveDocument.Spreadsheet.set('A10', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B10', '12.5'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A11', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B11', '5'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A12', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B12', '0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A13', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B13', '10'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A14', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B14', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A15', 'var height = '); App.ActiveDocument.Spreadsheet.set('B15', '5.5'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'height')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A16', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A17', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B17', '15'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A18', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B18', '0'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A19', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B19', '-10'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_PT-15-V02_Vertical_Hole.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_PT-15-V02_Vertical_Hole.FCStd")
print("created Potentiometer_Piher_PT-15-V02_Vertical_Hole")


 # Potentiometer_Piher_PT-15-V15_Vertical_Hole
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '0'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-12.5'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '15.0'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# clbody_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var clbody_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '7.5'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'clbody_fab')
# ctbody_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var ctbody_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-5.0'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'ctbody_fab')
# cdbody_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var cdbody_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '15'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'cdbody_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A8', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B8', '6'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'dscrew')
# dshaft
App.ActiveDocument.Spreadsheet.set('A9', 'var dshaft = '); App.ActiveDocument.Spreadsheet.set('B9', '4.4'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dshaft')
# rmx
App.ActiveDocument.Spreadsheet.set('A10', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B10', '15'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A11', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B11', '5'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A12', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B12', '0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A13', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B13', '10'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A14', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B14', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A15', 'var height = '); App.ActiveDocument.Spreadsheet.set('B15', '5.5'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'height')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A16', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A17', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B17', '15'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A18', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B18', '0'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A19', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B19', '-10'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_PT-15-V15_Vertical_Hole.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_PT-15-V15_Vertical_Hole.FCStd")
print("created Potentiometer_Piher_PT-15-V15_Vertical_Hole")


 # Potentiometer_ACP_CA9-V10_Vertical_Hole
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '0'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-7.4'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '10.0'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '9.8'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# clbody_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var clbody_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'clbody_fab')
# ctbody_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var ctbody_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-2.5'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'ctbody_fab')
# cdbody_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var cdbody_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'cdbody_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A8', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B8', '3'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'dscrew')
# dshaft
App.ActiveDocument.Spreadsheet.set('A9', 'var dshaft = '); App.ActiveDocument.Spreadsheet.set('B9', '2.1'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dshaft')
# rmx
App.ActiveDocument.Spreadsheet.set('A10', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B10', '10'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A11', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B11', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A12', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B12', '0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A13', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B13', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A14', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B14', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A15', 'var height = '); App.ActiveDocument.Spreadsheet.set('B15', '7.2'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'height')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A16', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A17', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B17', '15'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'mh_rmy')
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

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_ACP_CA9-V10_Vertical_Hole.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_ACP_CA9-V10_Vertical_Hole.FCStd")
print("created Potentiometer_ACP_CA9-V10_Vertical_Hole")


 # Potentiometer_ACP_CA14V-15_Vertical_Hole
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '0.5'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-12.0'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '14.0'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '14.0'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# clbody_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var clbody_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '7.5'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'clbody_fab')
# ctbody_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var ctbody_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-5.0'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'ctbody_fab')
# cdbody_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var cdbody_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'cdbody_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A8', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B8', '6'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'dscrew')
# dshaft
App.ActiveDocument.Spreadsheet.set('A9', 'var dshaft = '); App.ActiveDocument.Spreadsheet.set('B9', '5'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dshaft')
# rmx
App.ActiveDocument.Spreadsheet.set('A10', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B10', '15'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A11', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B11', '5'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A12', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B12', '0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A13', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B13', '10'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A14', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B14', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A15', 'var height = '); App.ActiveDocument.Spreadsheet.set('B15', '7.2'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'height')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A16', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A17', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B17', '15'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A18', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B18', '0'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A19', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B19', '-10'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_ACP_CA14V-15_Vertical_Hole.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_ACP_CA14V-15_Vertical_Hole.FCStd")
print("created Potentiometer_ACP_CA14V-15_Vertical_Hole")
