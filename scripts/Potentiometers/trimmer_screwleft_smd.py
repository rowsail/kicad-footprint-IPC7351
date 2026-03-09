#
# SCRIPT to generate 3D models
#



 # Potentiometer_Bourns_3214G_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-2.3000000000000003'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-2.4'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '4.6'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '4.8'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '-2.3000000000000003'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-2.02'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '1.78'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A9', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B9', '1.78'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dscrew')
# wscrew
App.ActiveDocument.Spreadsheet.set('A10', 'var wscrew = '); App.ActiveDocument.Spreadsheet.set('B10', '0'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'wscrew')
# rmxtwo
App.ActiveDocument.Spreadsheet.set('A11', 'var rmxtwo = '); App.ActiveDocument.Spreadsheet.set('B11', '-5.2'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmxtwo')
# rmytwo
App.ActiveDocument.Spreadsheet.set('A12', 'var rmytwo = '); App.ActiveDocument.Spreadsheet.set('B12', '1.15'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'rmytwo')
# rmxthree
App.ActiveDocument.Spreadsheet.set('A13', 'var rmxthree = '); App.ActiveDocument.Spreadsheet.set('B13', '0'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmxthree')
# rmythree
App.ActiveDocument.Spreadsheet.set('A14', 'var rmythree = '); App.ActiveDocument.Spreadsheet.set('B14', '2.3'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmythree')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '4.9'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '1.25'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.5'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '3.71'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# offsetx
App.ActiveDocument.Spreadsheet.set('A19', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B19', '-2.3000000000000003'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A20', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B20', '-2.4'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3214G_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3214G_Horizontal.FCStd")
print("created Potentiometer_Bourns_3214G_Horizontal")


 # Potentiometer_Bourns_3214J_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-2.3'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-2.4'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '4.6'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '4.8'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '-2.3'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-2.02'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '1.78'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A9', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B9', '1.78'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dscrew')
# wscrew
App.ActiveDocument.Spreadsheet.set('A10', 'var wscrew = '); App.ActiveDocument.Spreadsheet.set('B10', '0'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'wscrew')
# rmxtwo
App.ActiveDocument.Spreadsheet.set('A11', 'var rmxtwo = '); App.ActiveDocument.Spreadsheet.set('B11', '-4'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmxtwo')
# rmytwo
App.ActiveDocument.Spreadsheet.set('A12', 'var rmytwo = '); App.ActiveDocument.Spreadsheet.set('B12', '1.15'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'rmytwo')
# rmxthree
App.ActiveDocument.Spreadsheet.set('A13', 'var rmxthree = '); App.ActiveDocument.Spreadsheet.set('B13', '0'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmxthree')
# rmythree
App.ActiveDocument.Spreadsheet.set('A14', 'var rmythree = '); App.ActiveDocument.Spreadsheet.set('B14', '2.3'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmythree')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '4.3'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '1.25'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.5'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '3.71'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# offsetx
App.ActiveDocument.Spreadsheet.set('A19', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B19', '-2.3'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A20', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B20', '-2.4'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3214J_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3214J_Horizontal.FCStd")
print("created Potentiometer_Bourns_3214J_Horizontal")


 # Potentiometer_Bourns_3314R-1_Vertical_Hole
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-2.5'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-2.25'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '4.5'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '2.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '2.0'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A9', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B9', '2.0'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dscrew')
# wscrew
App.ActiveDocument.Spreadsheet.set('A10', 'var wscrew = '); App.ActiveDocument.Spreadsheet.set('B10', '0'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'wscrew')
# rmxtwo
App.ActiveDocument.Spreadsheet.set('A11', 'var rmxtwo = '); App.ActiveDocument.Spreadsheet.set('B11', '-1.15'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmxtwo')
# rmytwo
App.ActiveDocument.Spreadsheet.set('A12', 'var rmytwo = '); App.ActiveDocument.Spreadsheet.set('B12', '5.5'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'rmytwo')
# rmxthree
App.ActiveDocument.Spreadsheet.set('A13', 'var rmxthree = '); App.ActiveDocument.Spreadsheet.set('B13', '-2.3'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmxthree')
# rmythree
App.ActiveDocument.Spreadsheet.set('A14', 'var rmythree = '); App.ActiveDocument.Spreadsheet.set('B14', '0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmythree')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '3.65'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '-0.5'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '2.9000000000000004'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '2.55'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# offsetx
App.ActiveDocument.Spreadsheet.set('A19', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B19', '-2.5'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A20', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B20', '-2.25'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3314R-1_Vertical_Hole.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3314R-1_Vertical_Hole.FCStd")
print("created Potentiometer_Bourns_3314R-1_Vertical_Hole")


 # Potentiometer_Bourns_3314R-GM5_Vertical
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-2.5'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-2.25'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '5.0'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '4.5'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '2.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '2.0'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A9', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B9', '2.0'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dscrew')
# wscrew
App.ActiveDocument.Spreadsheet.set('A10', 'var wscrew = '); App.ActiveDocument.Spreadsheet.set('B10', '0'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'wscrew')
# rmxtwo
App.ActiveDocument.Spreadsheet.set('A11', 'var rmxtwo = '); App.ActiveDocument.Spreadsheet.set('B11', '-1.155'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmxtwo')
# rmytwo
App.ActiveDocument.Spreadsheet.set('A12', 'var rmytwo = '); App.ActiveDocument.Spreadsheet.set('B12', '6.25'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'rmytwo')
# rmxthree
App.ActiveDocument.Spreadsheet.set('A13', 'var rmxthree = '); App.ActiveDocument.Spreadsheet.set('B13', '-2.31'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmxthree')
# rmythree
App.ActiveDocument.Spreadsheet.set('A14', 'var rmythree = '); App.ActiveDocument.Spreadsheet.set('B14', '0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmythree')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '3.6550000000000002'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '-0.875'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '2.9000000000000004'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '2.55'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# offsetx
App.ActiveDocument.Spreadsheet.set('A19', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B19', '-2.5'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A20', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B20', '-2.25'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3314R-GM5_Vertical.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3314R-GM5_Vertical.FCStd")
print("created Potentiometer_Bourns_3314R-GM5_Vertical")


 # Potentiometer_Bourns_3314S_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-2.505'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-2.25'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '5.01'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '4.5'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-1.0'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '2.0'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A9', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B9', '2.0'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dscrew')
# wscrew
App.ActiveDocument.Spreadsheet.set('A10', 'var wscrew = '); App.ActiveDocument.Spreadsheet.set('B10', '0'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'wscrew')
# rmxtwo
App.ActiveDocument.Spreadsheet.set('A11', 'var rmxtwo = '); App.ActiveDocument.Spreadsheet.set('B11', '-1.15'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmxtwo')
# rmytwo
App.ActiveDocument.Spreadsheet.set('A12', 'var rmytwo = '); App.ActiveDocument.Spreadsheet.set('B12', '4.05'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'rmytwo')
# rmxthree
App.ActiveDocument.Spreadsheet.set('A13', 'var rmxthree = '); App.ActiveDocument.Spreadsheet.set('B13', '-2.3'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmxthree')
# rmythree
App.ActiveDocument.Spreadsheet.set('A14', 'var rmythree = '); App.ActiveDocument.Spreadsheet.set('B14', '0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmythree')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '3.655'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '0.2250000000000001'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '2.9000000000000004'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '5.61'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# offsetx
App.ActiveDocument.Spreadsheet.set('A19', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B19', '-2.505'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A20', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B20', '-2.25'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3314S_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3314S_Horizontal.FCStd")
print("created Potentiometer_Bourns_3314S_Horizontal")


 # Potentiometer_Bourns_3224G_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-2.3000000000000003'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-2.4'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '4.6'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '4.8'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '-2.3000000000000003'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-2.02'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '1.78'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A9', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B9', '1.78'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dscrew')
# wscrew
App.ActiveDocument.Spreadsheet.set('A10', 'var wscrew = '); App.ActiveDocument.Spreadsheet.set('B10', '0'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'wscrew')
# rmxtwo
App.ActiveDocument.Spreadsheet.set('A11', 'var rmxtwo = '); App.ActiveDocument.Spreadsheet.set('B11', '-5.2'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmxtwo')
# rmytwo
App.ActiveDocument.Spreadsheet.set('A12', 'var rmytwo = '); App.ActiveDocument.Spreadsheet.set('B12', '1.15'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'rmytwo')
# rmxthree
App.ActiveDocument.Spreadsheet.set('A13', 'var rmxthree = '); App.ActiveDocument.Spreadsheet.set('B13', '0'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmxthree')
# rmythree
App.ActiveDocument.Spreadsheet.set('A14', 'var rmythree = '); App.ActiveDocument.Spreadsheet.set('B14', '2.3'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmythree')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '4.9'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '1.25'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.5'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '3.71'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# offsetx
App.ActiveDocument.Spreadsheet.set('A19', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B19', '-2.3000000000000003'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A20', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B20', '-2.4'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3224G_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3224G_Horizontal.FCStd")
print("created Potentiometer_Bourns_3224G_Horizontal")


 # Potentiometer_Bourns_3224J_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-2.3'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-2.4'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '4.6'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '4.8'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '-2.3'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-2.02'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '0.0'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '1.78'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A9', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B9', '1.78'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dscrew')
# wscrew
App.ActiveDocument.Spreadsheet.set('A10', 'var wscrew = '); App.ActiveDocument.Spreadsheet.set('B10', '0'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'wscrew')
# rmxtwo
App.ActiveDocument.Spreadsheet.set('A11', 'var rmxtwo = '); App.ActiveDocument.Spreadsheet.set('B11', '-4'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmxtwo')
# rmytwo
App.ActiveDocument.Spreadsheet.set('A12', 'var rmytwo = '); App.ActiveDocument.Spreadsheet.set('B12', '1.15'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'rmytwo')
# rmxthree
App.ActiveDocument.Spreadsheet.set('A13', 'var rmxthree = '); App.ActiveDocument.Spreadsheet.set('B13', '0'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmxthree')
# rmythree
App.ActiveDocument.Spreadsheet.set('A14', 'var rmythree = '); App.ActiveDocument.Spreadsheet.set('B14', '2.3'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmythree')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '4.3'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '1.25'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.5'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '3.71'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# offsetx
App.ActiveDocument.Spreadsheet.set('A19', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B19', '-2.3'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A20', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B20', '-2.4'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3224J_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3224J_Horizontal.FCStd")
print("created Potentiometer_Bourns_3224J_Horizontal")


 # Potentiometer_Bourns_3269X_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-3.175'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-2.165'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '6.35'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '4.32'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '-4.695'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-0.2549999999999999'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '1.52'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '1.78'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A9', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B9', '1.78'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dscrew')
# wscrew
App.ActiveDocument.Spreadsheet.set('A10', 'var wscrew = '); App.ActiveDocument.Spreadsheet.set('B10', '1.52'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'wscrew')
# rmxtwo
App.ActiveDocument.Spreadsheet.set('A11', 'var rmxtwo = '); App.ActiveDocument.Spreadsheet.set('B11', '-2.54'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmxtwo')
# rmytwo
App.ActiveDocument.Spreadsheet.set('A12', 'var rmytwo = '); App.ActiveDocument.Spreadsheet.set('B12', '4.83'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'rmytwo')
# rmxthree
App.ActiveDocument.Spreadsheet.set('A13', 'var rmxthree = '); App.ActiveDocument.Spreadsheet.set('B13', '-5.08'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmxthree')
# rmythree
App.ActiveDocument.Spreadsheet.set('A14', 'var rmythree = '); App.ActiveDocument.Spreadsheet.set('B14', '0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmythree')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '5.715'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '-0.25'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.5'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '7.44'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# offsetx
App.ActiveDocument.Spreadsheet.set('A19', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B19', '-3.175'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A20', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B20', '-2.165'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3269X_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3269X_Horizontal.FCStd")
print("created Potentiometer_Bourns_3269X_Horizontal")


 # Potentiometer_Bourns_3269P_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-3.2250000000000005'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-3.175'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '6.35'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '6.35'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '-4.745000000000001'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-2.795'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '1.52'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '1.78'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A9', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B9', '1.78'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dscrew')
# wscrew
App.ActiveDocument.Spreadsheet.set('A10', 'var wscrew = '); App.ActiveDocument.Spreadsheet.set('B10', '1.52'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'wscrew')
# rmxtwo
App.ActiveDocument.Spreadsheet.set('A11', 'var rmxtwo = '); App.ActiveDocument.Spreadsheet.set('B11', '-6.4'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmxtwo')
# rmytwo
App.ActiveDocument.Spreadsheet.set('A12', 'var rmytwo = '); App.ActiveDocument.Spreadsheet.set('B12', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'rmytwo')
# rmxthree
App.ActiveDocument.Spreadsheet.set('A13', 'var rmxthree = '); App.ActiveDocument.Spreadsheet.set('B13', '0'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmxthree')
# rmythree
App.ActiveDocument.Spreadsheet.set('A14', 'var rmythree = '); App.ActiveDocument.Spreadsheet.set('B14', '5.08'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmythree')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '6.425000000000001'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '0.6349999999999998'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.5'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '5.21'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# offsetx
App.ActiveDocument.Spreadsheet.set('A19', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B19', '-3.2250000000000005'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A20', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B20', '-3.175'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3269P_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3269P_Horizontal.FCStd")
print("created Potentiometer_Bourns_3269P_Horizontal")
