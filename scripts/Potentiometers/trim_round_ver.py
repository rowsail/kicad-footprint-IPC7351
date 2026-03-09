#
# SCRIPT to generate 3D models
#



 # Potentiometer_Bourns_3339S_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-3.4299999999999997'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-1.5250000000000004'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '5.97'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '8.13'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-1.27'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '2.0300000000000002'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '7.62'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '4.57'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '0.54'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '4.0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '-2.54'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.5'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '9.53'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '5.54'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3339S_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3339S_Horizontal.FCStd")
print("created Potentiometer_Bourns_3339S_Horizontal")


 # Potentiometer_Bourns_3339W_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-0.8899999999999997'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-1.5250000000000004'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '5.97'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '8.13'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '5.08'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-1.27'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '2.0300000000000002'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '7.62'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '7.11'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '0.54'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '4.0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.5'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '9.53'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '5.54'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3339W_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3339W_Horizontal.FCStd")
print("created Potentiometer_Bourns_3339W_Horizontal")


 # Potentiometer_Bourns_3386X_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-1.145'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-2.2249999999999996'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '4.83'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '9.53'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '-1.145'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '0.9649999999999999'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '3.15'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '-1.145'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.5'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '9.53'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '5.33'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3386X_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3386X_Horizontal.FCStd")
print("created Potentiometer_Bourns_3386X_Horizontal")


 # Potentiometer_Bourns_3386C_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-2.415'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-2.2249999999999996'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '4.83'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '9.53'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '-2.415'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '0.9649999999999999'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '3.15'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '-2.415'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '0'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.5'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '9.53'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '5.33'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3386C_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3386C_Horizontal.FCStd")
print("created Potentiometer_Bourns_3386C_Horizontal")


 # Potentiometer_Vishay_T73XX_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-1.02'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-0.7599999999999998'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '4.7'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '6.6'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '-1.02'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '1.04'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '3.0'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '-1.02'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.5'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '7'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '3.8'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Vishay_T73XX_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Vishay_T73XX_Horizontal.FCStd")
print("created Potentiometer_Vishay_T73XX_Horizontal")


 # Potentiometer_Vishay_T73XW_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-2.35'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-0.7599999999999998'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '4.7'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '6.6'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '-2.35'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '1.04'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '3.0'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '-2.35'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '0'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.5'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '7'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '3.8'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Vishay_T73XW_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Vishay_T73XW_Horizontal.FCStd")
print("created Potentiometer_Vishay_T73XW_Horizontal")


 # Potentiometer_Piher_PT-6-H_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-0.6499999999999999'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '3.5'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '6.3'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '1.5'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '3.5'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '2.0'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '3.5'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '1.6'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '1.8'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.6000000000000001'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '7.65'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '4.5'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_PT-6-H_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_PT-6-H_Horizontal.FCStd")
print("created Potentiometer_Piher_PT-6-H_Horizontal")


 # Potentiometer_Piher_PT-10-H01_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-2.6500000000000004'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '4.8'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '10.3'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '0.75'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '4.8'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '3.5'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '4.8'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '3.0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '12.1'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '7'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_PT-10-H01_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_PT-10-H01_Horizontal.FCStd")
print("created Potentiometer_Piher_PT-10-H01_Horizontal")


 # Potentiometer_Piher_PT-10-H05_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-2.6500000000000004'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '4.8'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '10.3'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '0.75'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '4.8'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '3.5'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '4.8'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '3.0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '5'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '12.1'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '7'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_PT-10-H05_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_PT-10-H05_Horizontal.FCStd")
print("created Potentiometer_Piher_PT-10-H05_Horizontal")


 # Potentiometer_Piher_PT-15-H05_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '0'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-2.5'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '15.0'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '0'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '2.0'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '6.0'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '5'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '2.8'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '4.4'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '5'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '17.5'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '10'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_PT-15-H05_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_PT-15-H05_Horizontal.FCStd")
print("created Potentiometer_Piher_PT-15-H05_Horizontal")


 # Potentiometer_Piher_PT-15-H01_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '0'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-2.5'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '15.0'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '0'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '2.0'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '6.0'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '5'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '2.8'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '4.4'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '5'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '17.5'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '10'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_PT-15-H01_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_PT-15-H01_Horizontal.FCStd")
print("created Potentiometer_Piher_PT-15-H01_Horizontal")


 # Potentiometer_Piher_PT-15-H06_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '0'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-3.0999999999999996'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '15.0'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '0'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '1.4000000000000004'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '6.0'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '5'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '2.2'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '4.4'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '4'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '4.4'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '17.1'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '9.6'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_PT-15-H06_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_PT-15-H06_Horizontal.FCStd")
print("created Potentiometer_Piher_PT-15-H06_Horizontal")


 # Potentiometer_Piher_PT-15-H25_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '0'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-2.5'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '15.0'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '0'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '2.0'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '6.0'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '5'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '2.8'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '4.4'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '5'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '5'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '20'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '12.5'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_PT-15-H25_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_PT-15-H25_Horizontal.FCStd")
print("created Potentiometer_Piher_PT-15-H25_Horizontal")


 # Potentiometer_ACP_CA6-H2,5_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-0.6499999999999999'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '3.5'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '6.3'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '1.5'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '3.5'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '2.0'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '3.5'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '1.6'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '1.8'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.6000000000000001'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '7.65'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '4.5'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_ACP_CA6-H2,5_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_ACP_CA6-H2,5_Horizontal.FCStd")
print("created Potentiometer_ACP_CA6-H2,5_Horizontal")


 # Potentiometer_ACP_CA9-H2,5_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-2.4000000000000004'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '4.8'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '9.8'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '4.8'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '3.0'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '4.8'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '1.4500000000000002'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '2.1'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '12'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '7'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_ACP_CA9-H2,5_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_ACP_CA9-H2,5_Horizontal.FCStd")
print("created Potentiometer_ACP_CA9-H2,5_Horizontal")


 # Potentiometer_ACP_CA9-H3,8_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-2.4000000000000004'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '4.8'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '9.8'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '4.8'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '3.0'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '4.8'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '1.4500000000000002'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '2.1'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '3.8'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '12'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '7'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_ACP_CA9-H3,8_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_ACP_CA9-H3,8_Horizontal.FCStd")
print("created Potentiometer_ACP_CA9-H3,8_Horizontal")


 # Potentiometer_ACP_CA9-H5_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-2.4000000000000004'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '4.8'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '9.8'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '4.8'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '3.0'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '4.8'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '1.4500000000000002'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '2.1'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '5'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '12'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '7'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_ACP_CA9-H5_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_ACP_CA9-H5_Horizontal.FCStd")
print("created Potentiometer_ACP_CA9-H5_Horizontal")


 # Potentiometer_ACP_CA14-H2,5_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-2.0'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '14.0'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '2.0'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '6.0'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '5'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '17'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '10'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_ACP_CA14-H2,5_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_ACP_CA14-H2,5_Horizontal.FCStd")
print("created Potentiometer_ACP_CA14-H2,5_Horizontal")


 # Potentiometer_ACP_CA14-H4_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-2.0'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '14.0'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '2.0'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '6.0'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '4'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '5'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '17'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '10'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_ACP_CA14-H4_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_ACP_CA14-H4_Horizontal.FCStd")
print("created Potentiometer_ACP_CA14-H4_Horizontal")


 # Potentiometer_ACP_CA14-H5_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-2.0'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '14.0'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '2.0'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '6.0'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '5'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '5'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '17'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '10'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_ACP_CA14-H5_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_ACP_CA14-H5_Horizontal.FCStd")
print("created Potentiometer_ACP_CA14-H5_Horizontal")
