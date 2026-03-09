#
# SCRIPT to generate 3D models
#



 # Potentiometer_Omeg_PC16BU_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-3.000000000000001'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-13.45'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '9.3'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '16.9'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '6.3'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-8.5'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '6.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '7.0'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '12.3'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '-7.0'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '44.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '4.0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '10.0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '21'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '12.5'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '-10.0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Omeg_PC16BU_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Omeg_PC16BU_Horizontal.FCStd")
print("created Potentiometer_Omeg_PC16BU_Horizontal")


 # Potentiometer_Vishay_248GJ-249GJ_Single_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-2.5199999999999996'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-8.79'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '7.6'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '12.5'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '5.08'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-7.302499999999999'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '9.5'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '9.524999999999999'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '14.58'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '-5.715'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '12.719999999999999'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '6.35'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '7.62'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '5.08'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.7'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '13.1'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '6.949999999999999'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '-5.08'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Vishay_248GJ-249GJ_Single_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Vishay_248GJ-249GJ_Single_Horizontal.FCStd")
print("created Potentiometer_Vishay_248GJ-249GJ_Single_Horizontal")


 # Potentiometer_Vishay_248BH-249BH_Single_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-2.5199999999999996'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-8.79'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '7.6'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '12.5'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '5.08'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-5.715'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '9.5'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '6.35'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '14.58'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '-4.13'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '9.55'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '3.18'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '7.62'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '5.08'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.7'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '13.1'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '6.949999999999999'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '-5.08'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Vishay_248BH-249BH_Single_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Vishay_248BH-249BH_Single_Horizontal.FCStd")
print("created Potentiometer_Vishay_248BH-249BH_Single_Horizontal")


 # Potentiometer_Vishay_148-149_Single_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-3.75'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-8.79'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '8.83'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '12.5'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '5.08'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-5.715'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '6.35'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '6.35'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '11.43'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '-4.125'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '6.450000000000001'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '3.17'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '7.62'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '5.08'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.7'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '13.1'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '6.85'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '-5.08'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Vishay_148-149_Single_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Vishay_148-149_Single_Horizontal.FCStd")
print("created Potentiometer_Vishay_148-149_Single_Horizontal")


 # Potentiometer_Vishay_148E-149E_Single_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-7.139999999999999'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-8.79'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '12.219999999999999'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '12.5'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '5.08'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-5.715'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '6.35'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '6.35'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '11.43'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '-4.125'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '6.450000000000001'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '3.17'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '7.62'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '5.08'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.7'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '13.1'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '6.85'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '10.2'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '10.16'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '-5.08'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Vishay_148E-149E_Single_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Vishay_148E-149E_Single_Horizontal.FCStd")
print("created Potentiometer_Vishay_148E-149E_Single_Horizontal")


 # Potentiometer_Vishay_148-149_Dual_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-11.37'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-8.79'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '16.45'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '12.5'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '5.08'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-5.715'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '7.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '6.35'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '12.08'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '-4.125'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '6.450000000000001'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '3.17'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '7.62'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '5.08'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.7'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '13.1'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '6.85'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '-5.08'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Vishay_148-149_Dual_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Vishay_148-149_Dual_Horizontal.FCStd")
print("created Potentiometer_Vishay_148-149_Dual_Horizontal")


 # Potentiometer_Vishay_148E-149E_Dual_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-14.76'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-8.79'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '19.84'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '12.5'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '5.08'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-5.715'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '7.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '6.35'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '12.08'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '-4.125'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '6.450000000000001'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '3.17'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '7.62'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '5.08'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.7'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '13.1'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '6.85'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '17.82'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '10.16'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '-5.08'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Vishay_148E-149E_Dual_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Vishay_148E-149E_Dual_Horizontal.FCStd")
print("created Potentiometer_Vishay_148E-149E_Dual_Horizontal")


 # Potentiometer_Piher_PC-16_Single_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-1.5'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-13.0'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '8.0'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '16.0'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '6.5'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-10.0'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '9.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '10.0'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '15.5'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '-8.0'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '16.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '6.0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '7.5'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '10.0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '20.5'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '12.5'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '-10.0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_PC-16_Single_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_PC-16_Single_Horizontal.FCStd")
print("created Potentiometer_Piher_PC-16_Single_Horizontal")


 # Potentiometer_Piher_PC-16_Dual_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-9.5'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-13.0'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '16.0'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '16.0'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '6.5'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-10.0'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '9.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '10.0'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '15.5'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '-8.0'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '16.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '6.0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '7.5'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '10.0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '20.5'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '12.5'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '-10.0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_PC-16_Dual_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_PC-16_Dual_Horizontal.FCStd")
print("created Potentiometer_Piher_PC-16_Dual_Horizontal")


 # Potentiometer_Piher_PC-16_Triple_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-17.5'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-13.0'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '24.0'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '16.0'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '6.5'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-10.0'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '9.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '10.0'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '15.5'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '-8.0'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '16.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '6.0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '7.5'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '10.0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '20.5'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '12.5'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '-10.0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_PC-16_Triple_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_PC-16_Triple_Horizontal.FCStd")
print("created Potentiometer_Piher_PC-16_Triple_Horizontal")


 # Potentiometer_Piher_T-16H_Single_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-6.0'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-13.0'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '7.5'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '16.0'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '1.5'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-8.5'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '7.0'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '6.5'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '-7.0'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '10.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '4.0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '7.5'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '10.0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '21'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '12.5'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '-10.0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_T-16H_Single_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_T-16H_Single_Horizontal.FCStd")
print("created Potentiometer_Piher_T-16H_Single_Horizontal")


 # Potentiometer_Piher_T-16H_Double_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-13.5'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-13.0'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '15.0'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '16.0'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '1.5'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-8.5'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '7.0'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '6.5'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '-7.0'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '10.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '4.0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '7.5'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '10.0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '21'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '12.5'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '-10.0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_T-16H_Double_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Piher_T-16H_Double_Horizontal.FCStd")
print("created Potentiometer_Piher_T-16H_Double_Horizontal")


 # Potentiometer_Alps_RK163_Single_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-6.7'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-13.95'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '10.5'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '17.9'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '3.8'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-8.5'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '7.0'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '8.8'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '-8.0'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '10.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '6.0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '10.0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '21'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '12.5'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '-10.0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Alps_RK163_Single_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Alps_RK163_Single_Horizontal.FCStd")
print("created Potentiometer_Alps_RK163_Single_Horizontal")


 # Potentiometer_Alps_RK163_Dual_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-8.3'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-13.95'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '12.1'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '17.9'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '3.799999999999999'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-8.5'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '7.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '7.0'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '10.799999999999999'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '-8.0'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '10.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '6.0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '10.0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '1.0'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '21'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '12.5'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '-10.0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Alps_RK163_Dual_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Alps_RK163_Dual_Horizontal.FCStd")
print("created Potentiometer_Alps_RK163_Dual_Horizontal")


 # Potentiometer_Alps_RK097_Single_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-2.05'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-7.25'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '7.05'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '9.5'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-6.0'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '7.0'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '10.0'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '-5.5'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '10.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '6.0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.7'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '11.6'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '6.75'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '-5.0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Alps_RK097_Single_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Alps_RK097_Single_Horizontal.FCStd")
print("created Potentiometer_Alps_RK097_Single_Horizontal")


 # Potentiometer_Alps_RK097_Dual_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-4.550000000000001'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-7.25'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '9.55'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '9.5'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-6.0'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '7.0'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '10.0'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '-5.5'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '10.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '6.0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.7'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '11.6'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '6.75'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '-5.0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Alps_RK097_Dual_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Alps_RK097_Dual_Horizontal.FCStd")
print("created Potentiometer_Alps_RK097_Dual_Horizontal")


 # Potentiometer_Bourns_PTV09A-2_Single_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-1.5'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-7.35'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '9.7'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '3.5'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-5.9'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '0.8'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '6.8'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '4.3'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '-5.5'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '9.2'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '6.0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.7'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '15.5'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '10'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '10'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '-5.0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_PTV09A-2_Single_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_PTV09A-2_Single_Horizontal.FCStd")
print("created Potentiometer_Bourns_PTV09A-2_Single_Horizontal")


 # Potentiometer_Alps_RK09K_Single_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-3.4'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-7.4'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '6.8'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '9.8'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '3.4'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-5.75'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '0.8'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '6.5'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '4.2'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '-5.5'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '7.3999999999999995'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '6.0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.7'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '12.0'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '6.5'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '10'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '-5.0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Alps_RK09K_Single_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Alps_RK09K_Single_Horizontal.FCStd")
print("created Potentiometer_Alps_RK09K_Single_Horizontal")


 # Potentiometer_Alps_RK09L_Single_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-2.45'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-8.55'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '7.45'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '12.1'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-7.0'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '9.0'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '10.0'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '-5.5'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '10.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '6.0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.7'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '11.6'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '6.75'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '9.5'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '-5.0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Alps_RK09L_Single_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Alps_RK09L_Single_Horizontal.FCStd")
print("created Potentiometer_Alps_RK09L_Single_Horizontal")


 # Potentiometer_Alps_RK09L_Double_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-4.140000000000001'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-8.55'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '9.14'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '12.1'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-7.0'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '9.0'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '10.0'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '-5.5'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '10.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '6.0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.7'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '11.6'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '6.75'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '9.5'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '-5.0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Alps_RK09L_Double_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Alps_RK09L_Double_Horizontal.FCStd")
print("created Potentiometer_Alps_RK09L_Double_Horizontal")


 # Potentiometer_Alps_RK09Y11_Single_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-1.9500000000000002'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-7.25'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '5.4'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '9.5'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '3.45'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-6.0'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '7.0'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# lshaft_fab
App.ActiveDocument.Spreadsheet.set('A9', 'var lshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B9', '8.45'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'lshaft_fab')
# tshaft_fab
App.ActiveDocument.Spreadsheet.set('A10', 'var tshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B10', '-5.0'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'tshaft_fab')
# wshaft_fab
App.ActiveDocument.Spreadsheet.set('A11', 'var wshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B11', '7.0'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'wshaft_fab')
# hshaft_fab
App.ActiveDocument.Spreadsheet.set('A12', 'var hshaft_fab = '); App.ActiveDocument.Spreadsheet.set('B12', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'hshaft_fab')
# rmx
App.ActiveDocument.Spreadsheet.set('A13', 'var rmx = '); App.ActiveDocument.Spreadsheet.set('B13', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmx')
# rmy
App.ActiveDocument.Spreadsheet.set('A14', 'var rmy = '); App.ActiveDocument.Spreadsheet.set('B14', '2.5'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmy')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '0'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.7'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '11.35'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# screwzpos
App.ActiveDocument.Spreadsheet.set('A19', 'var screwzpos = '); App.ActiveDocument.Spreadsheet.set('B19', '6.5'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'screwzpos')
# mh_rmx
App.ActiveDocument.Spreadsheet.set('A20', 'var mh_rmx = '); App.ActiveDocument.Spreadsheet.set('B20', '0'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'mh_rmx')
# mh_rmy
App.ActiveDocument.Spreadsheet.set('A21', 'var mh_rmy = '); App.ActiveDocument.Spreadsheet.set('B21', '15'); App.ActiveDocument.Spreadsheet.setAlias('B21', 'mh_rmy')
# offsetx
App.ActiveDocument.Spreadsheet.set('A22', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B22', '0'); App.ActiveDocument.Spreadsheet.setAlias('B22', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A23', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B23', '-5.0'); App.ActiveDocument.Spreadsheet.setAlias('B23', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Alps_RK09Y11_Single_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Alps_RK09Y11_Single_Horizontal.FCStd")
print("created Potentiometer_Alps_RK09Y11_Single_Horizontal")
