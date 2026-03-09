#
# SCRIPT to generate 3D models
#



 # Resonator
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '10')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '10')
# H
App.ActiveDocument.Spreadsheet.set('B2', '5')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '5')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '10')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '5')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.5')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Resonator-2pin_w10.0mm_h5.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Resonator-2pin_w10.0mm_h5.0mm.FCStd")
print("created Resonator-2pin_w10.0mm_h5.0mm")


 # Resonator
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '7')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '7')
# H
App.ActiveDocument.Spreadsheet.set('B2', '2.5')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '2.5')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '5.5')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '5')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.7')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Resonator-2pin_w7.0mm_h2.5mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Resonator-2pin_w7.0mm_h2.5mm.FCStd")
print("created Resonator-2pin_w7.0mm_h2.5mm")


 # Resonator
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '8')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '8')
# H
App.ActiveDocument.Spreadsheet.set('B2', '3.5')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '3.5')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '6.5')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '5')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.7')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Resonator-2pin_w8.0mm_h3.5mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Resonator-2pin_w8.0mm_h3.5mm.FCStd")
print("created Resonator-2pin_w8.0mm_h3.5mm")


 # Resonator
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '6')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '6')
# H
App.ActiveDocument.Spreadsheet.set('B2', '3.0')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '3.0')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '6.5')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '5')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.7')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Resonator-2pin_w6.0mm_h3.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Resonator-2pin_w6.0mm_h3.0mm.FCStd")
print("created Resonator-2pin_w6.0mm_h3.0mm")
