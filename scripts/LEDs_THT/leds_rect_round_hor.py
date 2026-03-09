#
# SCRIPT to generate 3D models
#



 # LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O1.27mm_Z1.6mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '1.8')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '3.3')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '1.27')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '2.4')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '3')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '1.65')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '1.6')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O1.27mm_Z1.6mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O1.27mm_Z1.6mm.FCStd")
print("created LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O1.27mm_Z1.6mm")


 # LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O3.81mm_Z1.6mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '1.8')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '3.3')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '3.81')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '2.4')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '3')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '1.65')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '1.6')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O3.81mm_Z1.6mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O3.81mm_Z1.6mm.FCStd")
print("created LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O3.81mm_Z1.6mm")


 # LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O6.35mm_Z1.6mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '1.8')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '3.3')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '6.35')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '2.4')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '3')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '1.65')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '1.6')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O6.35mm_Z1.6mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O6.35mm_Z1.6mm.FCStd")
print("created LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O6.35mm_Z1.6mm")


 # LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O1.27mm_Z4.9mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '1.8')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '3.3')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '1.27')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '2.4')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '3')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '4.949999999999999')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '1.6')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O1.27mm_Z4.9mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O1.27mm_Z4.9mm.FCStd")
print("created LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O1.27mm_Z4.9mm")


 # LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O3.81mm_Z4.9mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '1.8')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '3.3')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '3.81')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '2.4')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '3')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '4.949999999999999')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '1.6')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O3.81mm_Z4.9mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O3.81mm_Z4.9mm.FCStd")
print("created LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O3.81mm_Z4.9mm")


 # LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O6.35mm_Z4.9mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '1.8')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '3.3')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '6.35')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '2.4')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '3')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '4.949999999999999')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '1.6')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O6.35mm_Z4.9mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O6.35mm_Z4.9mm.FCStd")
print("created LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O6.35mm_Z4.9mm")


 # LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O1.27mm_Z8.2mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '1.8')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '3.3')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '1.27')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '2.4')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '3')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '8.25')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '1.6')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O1.27mm_Z8.2mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O1.27mm_Z8.2mm.FCStd")
print("created LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O1.27mm_Z8.2mm")


 # LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O3.81mm_Z8.2mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '1.8')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '3.3')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '3.81')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '2.4')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '3')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '8.25')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '1.6')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O3.81mm_Z8.2mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O3.81mm_Z8.2mm.FCStd")
print("created LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O3.81mm_Z8.2mm")


 # LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O6.35mm_Z8.2mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '1.8')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '3.3')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '6.35')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '2.4')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '3')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '8.25')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '1.6')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O6.35mm_Z8.2mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O6.35mm_Z8.2mm.FCStd")
print("created LED_D1.8mm_W1.8mm_H2.4mm_Horizontal_O6.35mm_Z8.2mm")
