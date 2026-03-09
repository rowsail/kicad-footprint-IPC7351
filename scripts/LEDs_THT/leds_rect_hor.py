#
# SCRIPT to generate 3D models
#



 # LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O1.27mm_Z1.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '5')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '5')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '1.27')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '2')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '9.7')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '1')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '0')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O1.27mm_Z1.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O1.27mm_Z1.0mm.FCStd")
print("created LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O1.27mm_Z1.0mm")


 # LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O3.81mm_Z1.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '5')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '5')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '3.81')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '2')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '9.7')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '1')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '0')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O3.81mm_Z1.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O3.81mm_Z1.0mm.FCStd")
print("created LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O3.81mm_Z1.0mm")


 # LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O6.35mm_Z1.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '5')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '5')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '6.35')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '2')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '9.7')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '1')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '0')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O6.35mm_Z1.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O6.35mm_Z1.0mm.FCStd")
print("created LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O6.35mm_Z1.0mm")


 # LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O1.27mm_Z3.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '5')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '5')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '1.27')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '2')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '9.7')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '3')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '0')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O1.27mm_Z3.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O1.27mm_Z3.0mm.FCStd")
print("created LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O1.27mm_Z3.0mm")


 # LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O3.81mm_Z3.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '5')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '5')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '3.81')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '2')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '9.7')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '3')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '0')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O3.81mm_Z3.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O3.81mm_Z3.0mm.FCStd")
print("created LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O3.81mm_Z3.0mm")


 # LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O6.35mm_Z3.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '5')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '5')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '6.35')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '2')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '9.7')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '3')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '0')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O6.35mm_Z3.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O6.35mm_Z3.0mm.FCStd")
print("created LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O6.35mm_Z3.0mm")


 # LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O1.27mm_Z5.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '5')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '5')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '1.27')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '2')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '9.7')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '5')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '0')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O1.27mm_Z5.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O1.27mm_Z5.0mm.FCStd")
print("created LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O1.27mm_Z5.0mm")


 # LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O3.81mm_Z5.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '5')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '5')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '3.81')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '2')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '9.7')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '5')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '0')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O3.81mm_Z5.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O3.81mm_Z5.0mm.FCStd")
print("created LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O3.81mm_Z5.0mm")


 # LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O6.35mm_Z5.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '5')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '5')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '6.35')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '2')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '9.7')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '5')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '0')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O6.35mm_Z5.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O6.35mm_Z5.0mm.FCStd")
print("created LED_Rectangular_W5.0mm_H2.0mm_Horizontal_O6.35mm_Z5.0mm")
