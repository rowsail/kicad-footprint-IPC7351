#
# SCRIPT to generate 3D models
#



 # Potentiometer_Bourns_3296W_Vertical
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-7.305'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-2.41'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '9.53'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '4.83'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '0.9550000000000001'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '1.15'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '2.19'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '2.19'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A9', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B9', '2.19'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dscrew')
# wscrew
App.ActiveDocument.Spreadsheet.set('A10', 'var wscrew = '); App.ActiveDocument.Spreadsheet.set('B10', '2.19'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'wscrew')
# rmxtwo
App.ActiveDocument.Spreadsheet.set('A11', 'var rmxtwo = '); App.ActiveDocument.Spreadsheet.set('B11', '-2.54'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmxtwo')
# rmytwo
App.ActiveDocument.Spreadsheet.set('A12', 'var rmytwo = '); App.ActiveDocument.Spreadsheet.set('B12', '0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'rmytwo')
# rmxthree
App.ActiveDocument.Spreadsheet.set('A13', 'var rmxthree = '); App.ActiveDocument.Spreadsheet.set('B13', '-5.08'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmxthree')
# rmythree
App.ActiveDocument.Spreadsheet.set('A14', 'var rmythree = '); App.ActiveDocument.Spreadsheet.set('B14', '0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmythree')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '7.305'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '2.41'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.5'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '10.03'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# offsetx
App.ActiveDocument.Spreadsheet.set('A19', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B19', '-7.305'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A20', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B20', '-2.41'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3296W_Vertical.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3296W_Vertical.FCStd")
print("created Potentiometer_Bourns_3296W_Vertical")


 # Potentiometer_Bourns_3296Y_Vertical
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-7.305'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-1.14'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '9.53'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '4.83'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '0.9550000000000001'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '2.42'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '2.19'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '2.19'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A9', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B9', '2.19'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dscrew')
# wscrew
App.ActiveDocument.Spreadsheet.set('A10', 'var wscrew = '); App.ActiveDocument.Spreadsheet.set('B10', '2.19'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'wscrew')
# rmxtwo
App.ActiveDocument.Spreadsheet.set('A11', 'var rmxtwo = '); App.ActiveDocument.Spreadsheet.set('B11', '-2.54'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmxtwo')
# rmytwo
App.ActiveDocument.Spreadsheet.set('A12', 'var rmytwo = '); App.ActiveDocument.Spreadsheet.set('B12', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'rmytwo')
# rmxthree
App.ActiveDocument.Spreadsheet.set('A13', 'var rmxthree = '); App.ActiveDocument.Spreadsheet.set('B13', '-5.08'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmxthree')
# rmythree
App.ActiveDocument.Spreadsheet.set('A14', 'var rmythree = '); App.ActiveDocument.Spreadsheet.set('B14', '0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmythree')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '7.305'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '1.14'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.5'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '10.03'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# offsetx
App.ActiveDocument.Spreadsheet.set('A19', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B19', '-7.305'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A20', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B20', '-1.14'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3296Y_Vertical.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3296Y_Vertical.FCStd")
print("created Potentiometer_Bourns_3296Y_Vertical")


 # Potentiometer_Bourns_3299W_Vertical
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-7.305'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-1.91'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '9.53'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '6.1'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '0.9550000000000001'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '2.92'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '2.19'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '2.19'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A9', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B9', '2.19'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dscrew')
# wscrew
App.ActiveDocument.Spreadsheet.set('A10', 'var wscrew = '); App.ActiveDocument.Spreadsheet.set('B10', '2.19'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'wscrew')
# rmxtwo
App.ActiveDocument.Spreadsheet.set('A11', 'var rmxtwo = '); App.ActiveDocument.Spreadsheet.set('B11', '-2.54'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmxtwo')
# rmytwo
App.ActiveDocument.Spreadsheet.set('A12', 'var rmytwo = '); App.ActiveDocument.Spreadsheet.set('B12', '0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'rmytwo')
# rmxthree
App.ActiveDocument.Spreadsheet.set('A13', 'var rmxthree = '); App.ActiveDocument.Spreadsheet.set('B13', '-5.08'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmxthree')
# rmythree
App.ActiveDocument.Spreadsheet.set('A14', 'var rmythree = '); App.ActiveDocument.Spreadsheet.set('B14', '0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmythree')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '7.305'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '1.91'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.5'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '10.03'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# offsetx
App.ActiveDocument.Spreadsheet.set('A19', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B19', '-7.305'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A20', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B20', '-1.91'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3299W_Vertical.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3299W_Vertical.FCStd")
print("created Potentiometer_Bourns_3299W_Vertical")


 # Potentiometer_Bourns_3299Y_Vertical
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-7.305'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-1.91'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '9.53'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '6.1'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '0.9550000000000001'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '2.92'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '2.19'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '2.19'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A9', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B9', '2.19'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dscrew')
# wscrew
App.ActiveDocument.Spreadsheet.set('A10', 'var wscrew = '); App.ActiveDocument.Spreadsheet.set('B10', '2.19'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'wscrew')
# rmxtwo
App.ActiveDocument.Spreadsheet.set('A11', 'var rmxtwo = '); App.ActiveDocument.Spreadsheet.set('B11', '-2.54'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmxtwo')
# rmytwo
App.ActiveDocument.Spreadsheet.set('A12', 'var rmytwo = '); App.ActiveDocument.Spreadsheet.set('B12', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'rmytwo')
# rmxthree
App.ActiveDocument.Spreadsheet.set('A13', 'var rmxthree = '); App.ActiveDocument.Spreadsheet.set('B13', '-5.08'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmxthree')
# rmythree
App.ActiveDocument.Spreadsheet.set('A14', 'var rmythree = '); App.ActiveDocument.Spreadsheet.set('B14', '0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmythree')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '7.305'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '1.91'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.5'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '10.03'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# offsetx
App.ActiveDocument.Spreadsheet.set('A19', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B19', '-7.305'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A20', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B20', '-1.91'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3299Y_Vertical.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3299Y_Vertical.FCStd")
print("created Potentiometer_Bourns_3299Y_Vertical")


 # Potentiometer_Bourns_3266Y_Vertical
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-5.895'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-2.16'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '6.71'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '4.5'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '-0.40499999999999936'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '1.0699999999999998'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '1.78'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '1.78'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A9', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B9', '1.78'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dscrew')
# wscrew
App.ActiveDocument.Spreadsheet.set('A10', 'var wscrew = '); App.ActiveDocument.Spreadsheet.set('B10', '1.78'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'wscrew')
# rmxtwo
App.ActiveDocument.Spreadsheet.set('A11', 'var rmxtwo = '); App.ActiveDocument.Spreadsheet.set('B11', '-2.54'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmxtwo')
# rmytwo
App.ActiveDocument.Spreadsheet.set('A12', 'var rmytwo = '); App.ActiveDocument.Spreadsheet.set('B12', '0'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'rmytwo')
# rmxthree
App.ActiveDocument.Spreadsheet.set('A13', 'var rmxthree = '); App.ActiveDocument.Spreadsheet.set('B13', '-5.08'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmxthree')
# rmythree
App.ActiveDocument.Spreadsheet.set('A14', 'var rmythree = '); App.ActiveDocument.Spreadsheet.set('B14', '0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmythree')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '5.895'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '2.16'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.5'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '6.71'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# offsetx
App.ActiveDocument.Spreadsheet.set('A19', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B19', '-5.895'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A20', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B20', '-2.16'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3266Y_Vertical.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3266Y_Vertical.FCStd")
print("created Potentiometer_Bourns_3266Y_Vertical")


 # Potentiometer_Bourns_3266W_Vertical
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-5.895'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-1.02'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '6.71'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '4.5'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '-0.45500000000000007'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '2.21'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '1.78'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '1.78'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A9', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B9', '1.78'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dscrew')
# wscrew
App.ActiveDocument.Spreadsheet.set('A10', 'var wscrew = '); App.ActiveDocument.Spreadsheet.set('B10', '1.78'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'wscrew')
# rmxtwo
App.ActiveDocument.Spreadsheet.set('A11', 'var rmxtwo = '); App.ActiveDocument.Spreadsheet.set('B11', '-2.54'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmxtwo')
# rmytwo
App.ActiveDocument.Spreadsheet.set('A12', 'var rmytwo = '); App.ActiveDocument.Spreadsheet.set('B12', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'rmytwo')
# rmxthree
App.ActiveDocument.Spreadsheet.set('A13', 'var rmxthree = '); App.ActiveDocument.Spreadsheet.set('B13', '-5.08'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmxthree')
# rmythree
App.ActiveDocument.Spreadsheet.set('A14', 'var rmythree = '); App.ActiveDocument.Spreadsheet.set('B14', '0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmythree')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '5.895'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '1.02'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.5'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '6.71'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# offsetx
App.ActiveDocument.Spreadsheet.set('A19', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B19', '-5.895'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A20', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B20', '-1.02'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3266W_Vertical.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3266W_Vertical.FCStd")
print("created Potentiometer_Bourns_3266W_Vertical")
