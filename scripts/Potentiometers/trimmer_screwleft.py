#
# SCRIPT to generate 3D models
#



 # Potentiometer_Bourns_3005_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-16'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-3.3'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '19.3'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '4.06'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '-17.52'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-2.77'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '1.52'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '3.0'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A9', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B9', '3'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dscrew')
# wscrew
App.ActiveDocument.Spreadsheet.set('A10', 'var wscrew = '); App.ActiveDocument.Spreadsheet.set('B10', '1.52'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'wscrew')
# rmxtwo
App.ActiveDocument.Spreadsheet.set('A11', 'var rmxtwo = '); App.ActiveDocument.Spreadsheet.set('B11', '-7.62'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmxtwo')
# rmytwo
App.ActiveDocument.Spreadsheet.set('A12', 'var rmytwo = '); App.ActiveDocument.Spreadsheet.set('B12', '-2.54'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'rmytwo')
# rmxthree
App.ActiveDocument.Spreadsheet.set('A13', 'var rmxthree = '); App.ActiveDocument.Spreadsheet.set('B13', '-12.7'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmxthree')
# rmythree
App.ActiveDocument.Spreadsheet.set('A14', 'var rmythree = '); App.ActiveDocument.Spreadsheet.set('B14', '0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmythree')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '16'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '3.3'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.7'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '7.87'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# offsetx
App.ActiveDocument.Spreadsheet.set('A19', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B19', '-16'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A20', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B20', '-3.3'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3005_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3005_Horizontal.FCStd")
print("created Potentiometer_Bourns_3005_Horizontal")


 # Potentiometer_Vishay_43_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-16'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-3.67'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '19.0'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '4.8'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '-17.52'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-2.45'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '1.52'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '2.36'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A9', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B9', '2.36'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dscrew')
# wscrew
App.ActiveDocument.Spreadsheet.set('A10', 'var wscrew = '); App.ActiveDocument.Spreadsheet.set('B10', '1.52'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'wscrew')
# rmxtwo
App.ActiveDocument.Spreadsheet.set('A11', 'var rmxtwo = '); App.ActiveDocument.Spreadsheet.set('B11', '-7.62'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmxtwo')
# rmytwo
App.ActiveDocument.Spreadsheet.set('A12', 'var rmytwo = '); App.ActiveDocument.Spreadsheet.set('B12', '-2.54'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'rmytwo')
# rmxthree
App.ActiveDocument.Spreadsheet.set('A13', 'var rmxthree = '); App.ActiveDocument.Spreadsheet.set('B13', '-12.7'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmxthree')
# rmythree
App.ActiveDocument.Spreadsheet.set('A14', 'var rmythree = '); App.ActiveDocument.Spreadsheet.set('B14', '0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmythree')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '16'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '3.67'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.7'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '6.35'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# offsetx
App.ActiveDocument.Spreadsheet.set('A19', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B19', '-16'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A20', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B20', '-3.67'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Vishay_43_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Vishay_43_Horizontal.FCStd")
print("created Potentiometer_Vishay_43_Horizontal")


 # Potentiometer_Bourns_3006P_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-16'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-3.685'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '19.05'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '4.83'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '-17.52'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-2.45'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '1.52'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '2.36'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A9', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B9', '2.36'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dscrew')
# wscrew
App.ActiveDocument.Spreadsheet.set('A10', 'var wscrew = '); App.ActiveDocument.Spreadsheet.set('B10', '1.52'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'wscrew')
# rmxtwo
App.ActiveDocument.Spreadsheet.set('A11', 'var rmxtwo = '); App.ActiveDocument.Spreadsheet.set('B11', '-7.62'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmxtwo')
# rmytwo
App.ActiveDocument.Spreadsheet.set('A12', 'var rmytwo = '); App.ActiveDocument.Spreadsheet.set('B12', '-2.54'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'rmytwo')
# rmxthree
App.ActiveDocument.Spreadsheet.set('A13', 'var rmxthree = '); App.ActiveDocument.Spreadsheet.set('B13', '-12.7'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmxthree')
# rmythree
App.ActiveDocument.Spreadsheet.set('A14', 'var rmythree = '); App.ActiveDocument.Spreadsheet.set('B14', '0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmythree')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '16'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '3.685'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.7'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '6.35'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# offsetx
App.ActiveDocument.Spreadsheet.set('A19', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B19', '-16'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A20', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B20', '-3.685'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3006P_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3006P_Horizontal.FCStd")
print("created Potentiometer_Bourns_3006P_Horizontal")


 # Potentiometer_Bourns_3006W_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-16'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-4.98'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '19.05'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '4.83'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '-17.52'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-3.745'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '1.52'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '2.36'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A9', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B9', '2.36'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dscrew')
# wscrew
App.ActiveDocument.Spreadsheet.set('A10', 'var wscrew = '); App.ActiveDocument.Spreadsheet.set('B10', '1.52'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'wscrew')
# rmxtwo
App.ActiveDocument.Spreadsheet.set('A11', 'var rmxtwo = '); App.ActiveDocument.Spreadsheet.set('B11', '-7.62'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmxtwo')
# rmytwo
App.ActiveDocument.Spreadsheet.set('A12', 'var rmytwo = '); App.ActiveDocument.Spreadsheet.set('B12', '-5.06'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'rmytwo')
# rmxthree
App.ActiveDocument.Spreadsheet.set('A13', 'var rmxthree = '); App.ActiveDocument.Spreadsheet.set('B13', '-12.7'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmxthree')
# rmythree
App.ActiveDocument.Spreadsheet.set('A14', 'var rmythree = '); App.ActiveDocument.Spreadsheet.set('B14', '0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmythree')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '16'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '4.98'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.7'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '6.35'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# offsetx
App.ActiveDocument.Spreadsheet.set('A19', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B19', '-16'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A20', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B20', '-4.98'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3006W_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3006W_Horizontal.FCStd")
print("created Potentiometer_Bourns_3006W_Horizontal")


 # Potentiometer_Bourns_3006Y_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-18.42'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-3.685'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '19.05'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '4.83'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '-19.94'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-2.45'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '1.52'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '2.36'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A9', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B9', '2.36'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dscrew')
# wscrew
App.ActiveDocument.Spreadsheet.set('A10', 'var wscrew = '); App.ActiveDocument.Spreadsheet.set('B10', '1.52'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'wscrew')
# rmxtwo
App.ActiveDocument.Spreadsheet.set('A11', 'var rmxtwo = '); App.ActiveDocument.Spreadsheet.set('B11', '-10.16'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmxtwo')
# rmytwo
App.ActiveDocument.Spreadsheet.set('A12', 'var rmytwo = '); App.ActiveDocument.Spreadsheet.set('B12', '-2.54'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'rmytwo')
# rmxthree
App.ActiveDocument.Spreadsheet.set('A13', 'var rmxthree = '); App.ActiveDocument.Spreadsheet.set('B13', '-17.78'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmxthree')
# rmythree
App.ActiveDocument.Spreadsheet.set('A14', 'var rmythree = '); App.ActiveDocument.Spreadsheet.set('B14', '0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmythree')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '18.42'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '3.685'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.7'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '6.35'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# offsetx
App.ActiveDocument.Spreadsheet.set('A19', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B19', '-18.42'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A20', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B20', '-3.685'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3006Y_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3006Y_Horizontal.FCStd")
print("created Potentiometer_Bourns_3006Y_Horizontal")


 # Potentiometer_Bourns_3009P_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-16'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-3.685'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '19.05'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '4.83'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '-17.52'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-2.45'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '1.52'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '2.36'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A9', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B9', '2.36'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dscrew')
# wscrew
App.ActiveDocument.Spreadsheet.set('A10', 'var wscrew = '); App.ActiveDocument.Spreadsheet.set('B10', '1.52'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'wscrew')
# rmxtwo
App.ActiveDocument.Spreadsheet.set('A11', 'var rmxtwo = '); App.ActiveDocument.Spreadsheet.set('B11', '-7.62'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmxtwo')
# rmytwo
App.ActiveDocument.Spreadsheet.set('A12', 'var rmytwo = '); App.ActiveDocument.Spreadsheet.set('B12', '-2.54'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'rmytwo')
# rmxthree
App.ActiveDocument.Spreadsheet.set('A13', 'var rmxthree = '); App.ActiveDocument.Spreadsheet.set('B13', '-12.7'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmxthree')
# rmythree
App.ActiveDocument.Spreadsheet.set('A14', 'var rmythree = '); App.ActiveDocument.Spreadsheet.set('B14', '0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmythree')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '16'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '3.685'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.7'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '8.98'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# offsetx
App.ActiveDocument.Spreadsheet.set('A19', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B19', '-16'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A20', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B20', '-3.685'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3009P_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3009P_Horizontal.FCStd")
print("created Potentiometer_Bourns_3009P_Horizontal")


 # Potentiometer_Bourns_3009Y_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-18.42'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-3.685'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '19.05'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '4.83'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '-19.94'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-2.45'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '1.52'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '2.36'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A9', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B9', '2.36'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dscrew')
# wscrew
App.ActiveDocument.Spreadsheet.set('A10', 'var wscrew = '); App.ActiveDocument.Spreadsheet.set('B10', '1.52'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'wscrew')
# rmxtwo
App.ActiveDocument.Spreadsheet.set('A11', 'var rmxtwo = '); App.ActiveDocument.Spreadsheet.set('B11', '-10.16'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmxtwo')
# rmytwo
App.ActiveDocument.Spreadsheet.set('A12', 'var rmytwo = '); App.ActiveDocument.Spreadsheet.set('B12', '-2.54'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'rmytwo')
# rmxthree
App.ActiveDocument.Spreadsheet.set('A13', 'var rmxthree = '); App.ActiveDocument.Spreadsheet.set('B13', '-17.78'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmxthree')
# rmythree
App.ActiveDocument.Spreadsheet.set('A14', 'var rmythree = '); App.ActiveDocument.Spreadsheet.set('B14', '0'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmythree')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '18.42'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '3.685'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.7'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '8.98'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# offsetx
App.ActiveDocument.Spreadsheet.set('A19', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B19', '-18.42'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A20', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B20', '-3.685'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3009Y_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3009Y_Horizontal.FCStd")
print("created Potentiometer_Bourns_3009Y_Horizontal")


 # Potentiometer_Bourns_3296X_Horizontal
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
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '-8.825'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '0.054999999999999716'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '1.52'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '2.19'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A9', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B9', '2.19'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dscrew')
# wscrew
App.ActiveDocument.Spreadsheet.set('A10', 'var wscrew = '); App.ActiveDocument.Spreadsheet.set('B10', '1.52'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'wscrew')
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

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3296X_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3296X_Horizontal.FCStd")
print("created Potentiometer_Bourns_3296X_Horizontal")


 # Potentiometer_Bourns_3296Z_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-7.305'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-1.1500000000000004'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '9.53'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '4.83'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '-8.825'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '1.3149999999999995'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '1.52'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '2.19'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A9', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B9', '2.19'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dscrew')
# wscrew
App.ActiveDocument.Spreadsheet.set('A10', 'var wscrew = '); App.ActiveDocument.Spreadsheet.set('B10', '1.52'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'wscrew')
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
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '1.1500000000000004'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.5'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '10.03'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# offsetx
App.ActiveDocument.Spreadsheet.set('A19', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B19', '-7.305'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A20', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B20', '-1.1500000000000004'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3296Z_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3296Z_Horizontal.FCStd")
print("created Potentiometer_Bourns_3296Z_Horizontal")


 # Potentiometer_Bourns_3296P_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-5.015'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-2.2249999999999996'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '10.03'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '9.53'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '-6.535'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-2.05'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '1.52'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '2.19'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A9', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B9', '2.19'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dscrew')
# wscrew
App.ActiveDocument.Spreadsheet.set('A10', 'var wscrew = '); App.ActiveDocument.Spreadsheet.set('B10', '1.52'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'wscrew')
# rmxtwo
App.ActiveDocument.Spreadsheet.set('A11', 'var rmxtwo = '); App.ActiveDocument.Spreadsheet.set('B11', '-2.54'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmxtwo')
# rmytwo
App.ActiveDocument.Spreadsheet.set('A12', 'var rmytwo = '); App.ActiveDocument.Spreadsheet.set('B12', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'rmytwo')
# rmxthree
App.ActiveDocument.Spreadsheet.set('A13', 'var rmxthree = '); App.ActiveDocument.Spreadsheet.set('B13', '0'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmxthree')
# rmythree
App.ActiveDocument.Spreadsheet.set('A14', 'var rmythree = '); App.ActiveDocument.Spreadsheet.set('B14', '5.08'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmythree')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '5.015'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '2.2249999999999996'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.5'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '4.83'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# offsetx
App.ActiveDocument.Spreadsheet.set('A19', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B19', '-5.015'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A20', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B20', '-2.2249999999999996'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3296P_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3296P_Horizontal.FCStd")
print("created Potentiometer_Bourns_3296P_Horizontal")


 # Potentiometer_Bourns_3299X_Horizontal
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
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '-8.825'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '1.8250000000000004'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '1.52'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '2.19'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A9', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B9', '2.19'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dscrew')
# wscrew
App.ActiveDocument.Spreadsheet.set('A10', 'var wscrew = '); App.ActiveDocument.Spreadsheet.set('B10', '1.52'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'wscrew')
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

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3299X_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3299X_Horizontal.FCStd")
print("created Potentiometer_Bourns_3299X_Horizontal")


 # Potentiometer_Bourns_3299Z_Horizontal
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
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '-8.825'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '1.8250000000000004'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '1.52'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '2.19'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A9', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B9', '2.19'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dscrew')
# wscrew
App.ActiveDocument.Spreadsheet.set('A10', 'var wscrew = '); App.ActiveDocument.Spreadsheet.set('B10', '1.52'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'wscrew')
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

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3299Z_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3299Z_Horizontal.FCStd")
print("created Potentiometer_Bourns_3299Z_Horizontal")


 # Potentiometer_Bourns_3299P_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-5.015'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-2.2249999999999996'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '10.03'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '9.53'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '-6.535'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-2.05'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
# wscrew_fab
App.ActiveDocument.Spreadsheet.set('A7', 'var wscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B7', '1.52'); App.ActiveDocument.Spreadsheet.setAlias('B7', 'wscrew_fab')
# hscrew_fab
App.ActiveDocument.Spreadsheet.set('A8', 'var hscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B8', '2.19'); App.ActiveDocument.Spreadsheet.setAlias('B8', 'hscrew_fab')
# dscrew
App.ActiveDocument.Spreadsheet.set('A9', 'var dscrew = '); App.ActiveDocument.Spreadsheet.set('B9', '2.19'); App.ActiveDocument.Spreadsheet.setAlias('B9', 'dscrew')
# wscrew
App.ActiveDocument.Spreadsheet.set('A10', 'var wscrew = '); App.ActiveDocument.Spreadsheet.set('B10', '1.52'); App.ActiveDocument.Spreadsheet.setAlias('B10', 'wscrew')
# rmxtwo
App.ActiveDocument.Spreadsheet.set('A11', 'var rmxtwo = '); App.ActiveDocument.Spreadsheet.set('B11', '-2.54'); App.ActiveDocument.Spreadsheet.setAlias('B11', 'rmxtwo')
# rmytwo
App.ActiveDocument.Spreadsheet.set('A12', 'var rmytwo = '); App.ActiveDocument.Spreadsheet.set('B12', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'rmytwo')
# rmxthree
App.ActiveDocument.Spreadsheet.set('A13', 'var rmxthree = '); App.ActiveDocument.Spreadsheet.set('B13', '0'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmxthree')
# rmythree
App.ActiveDocument.Spreadsheet.set('A14', 'var rmythree = '); App.ActiveDocument.Spreadsheet.set('B14', '5.08'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmythree')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '5.015'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '2.2249999999999996'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.5'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '6.1'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# offsetx
App.ActiveDocument.Spreadsheet.set('A19', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B19', '-5.015'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A20', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B20', '-2.2249999999999996'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3299P_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3299P_Horizontal.FCStd")
print("created Potentiometer_Bourns_3299P_Horizontal")


 # Potentiometer_Bourns_3266Z_Horizontal
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
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '-7.414999999999999'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '0.17999999999999972'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
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

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3266Z_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3266Z_Horizontal.FCStd")
print("created Potentiometer_Bourns_3266Z_Horizontal")


 # Potentiometer_Bourns_3266X_Horizontal
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
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '-7.414999999999999'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '1.3199999999999998'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
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

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3266X_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3266X_Horizontal.FCStd")
print("created Potentiometer_Bourns_3266X_Horizontal")


 # Potentiometer_Bourns_3266P_Horizontal
import FreeCAD
import os
import os.path

App.ActiveDocument.clearAll()
# lbody_fab
App.ActiveDocument.Spreadsheet.set('A1', 'var lbody_fab = '); App.ActiveDocument.Spreadsheet.set('B1', '-3.355'); App.ActiveDocument.Spreadsheet.setAlias('B1', 'lbody_fab')
# tbody_fab
App.ActiveDocument.Spreadsheet.set('A2', 'var tbody_fab = '); App.ActiveDocument.Spreadsheet.set('B2', '-0.815'); App.ActiveDocument.Spreadsheet.setAlias('B2', 'tbody_fab')
# wbody_fab
App.ActiveDocument.Spreadsheet.set('A3', 'var wbody_fab = '); App.ActiveDocument.Spreadsheet.set('B3', '6.71'); App.ActiveDocument.Spreadsheet.setAlias('B3', 'wbody_fab')
# hbody_fab
App.ActiveDocument.Spreadsheet.set('A4', 'var hbody_fab = '); App.ActiveDocument.Spreadsheet.set('B4', '6.71'); App.ActiveDocument.Spreadsheet.setAlias('B4', 'hbody_fab')
# lscrew_fab
App.ActiveDocument.Spreadsheet.set('A5', 'var lscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B5', '-4.875'); App.ActiveDocument.Spreadsheet.setAlias('B5', 'lscrew_fab')
# tscrew_fab
App.ActiveDocument.Spreadsheet.set('A6', 'var tscrew_fab = '); App.ActiveDocument.Spreadsheet.set('B6', '-0.43499999999999994'); App.ActiveDocument.Spreadsheet.setAlias('B6', 'tscrew_fab')
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
App.ActiveDocument.Spreadsheet.set('A12', 'var rmytwo = '); App.ActiveDocument.Spreadsheet.set('B12', '2.54'); App.ActiveDocument.Spreadsheet.setAlias('B12', 'rmytwo')
# rmxthree
App.ActiveDocument.Spreadsheet.set('A13', 'var rmxthree = '); App.ActiveDocument.Spreadsheet.set('B13', '0'); App.ActiveDocument.Spreadsheet.setAlias('B13', 'rmxthree')
# rmythree
App.ActiveDocument.Spreadsheet.set('A14', 'var rmythree = '); App.ActiveDocument.Spreadsheet.set('B14', '5.08'); App.ActiveDocument.Spreadsheet.setAlias('B14', 'rmythree')
# padx
App.ActiveDocument.Spreadsheet.set('A15', 'var padx = '); App.ActiveDocument.Spreadsheet.set('B15', '3.355'); App.ActiveDocument.Spreadsheet.setAlias('B15', 'padx')
# pady
App.ActiveDocument.Spreadsheet.set('A16', 'var pady = '); App.ActiveDocument.Spreadsheet.set('B16', '0.815'); App.ActiveDocument.Spreadsheet.setAlias('B16', 'pady')
# d_wire
App.ActiveDocument.Spreadsheet.set('A17', 'var d_wire = '); App.ActiveDocument.Spreadsheet.set('B17', '0.5'); App.ActiveDocument.Spreadsheet.setAlias('B17', 'd_wire')
# height
App.ActiveDocument.Spreadsheet.set('A18', 'var height = '); App.ActiveDocument.Spreadsheet.set('B18', '4.5'); App.ActiveDocument.Spreadsheet.setAlias('B18', 'height')
# offsetx
App.ActiveDocument.Spreadsheet.set('A19', 'var offsetx = '); App.ActiveDocument.Spreadsheet.set('B19', '-3.355'); App.ActiveDocument.Spreadsheet.setAlias('B19', 'offsetx')
# offsety
App.ActiveDocument.Spreadsheet.set('A20', 'var offsety = '); App.ActiveDocument.Spreadsheet.set('B20', '-0.815'); App.ActiveDocument.Spreadsheet.setAlias('B20', 'offsety')
App.ActiveDocument.recompute()

doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3266P_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Potentiometer_Bourns_3266P_Horizontal.FCStd")
print("created Potentiometer_Bourns_3266P_Horizontal")
