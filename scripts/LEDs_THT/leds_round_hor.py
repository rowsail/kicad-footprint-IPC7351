#
# SCRIPT to generate 3D models
#



 # LED_D3.0mm_Horizontal_O1.27mm_Z2.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '3')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '3.8')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '1.27')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '3')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '5.3')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '2')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '1')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D3.0mm_Horizontal_O1.27mm_Z2.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D3.0mm_Horizontal_O1.27mm_Z2.0mm.FCStd")
print("created LED_D3.0mm_Horizontal_O1.27mm_Z2.0mm")


 # LED_D3.0mm_Horizontal_O3.81mm_Z2.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '3')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '3.8')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '3.81')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '3')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '5.3')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '2')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '1')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D3.0mm_Horizontal_O3.81mm_Z2.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D3.0mm_Horizontal_O3.81mm_Z2.0mm.FCStd")
print("created LED_D3.0mm_Horizontal_O3.81mm_Z2.0mm")


 # LED_D3.0mm_Horizontal_O6.35mm_Z2.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '3')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '3.8')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '6.35')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '3')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '5.3')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '2')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '1')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D3.0mm_Horizontal_O6.35mm_Z2.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D3.0mm_Horizontal_O6.35mm_Z2.0mm.FCStd")
print("created LED_D3.0mm_Horizontal_O6.35mm_Z2.0mm")


 # LED_D3.0mm_Horizontal_O1.27mm_Z6.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '3')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '3.8')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '1.27')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '3')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '5.3')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '6')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '1')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D3.0mm_Horizontal_O1.27mm_Z6.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D3.0mm_Horizontal_O1.27mm_Z6.0mm.FCStd")
print("created LED_D3.0mm_Horizontal_O1.27mm_Z6.0mm")


 # LED_D3.0mm_Horizontal_O3.81mm_Z6.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '3')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '3.8')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '3.81')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '3')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '5.3')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '6')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '1')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D3.0mm_Horizontal_O3.81mm_Z6.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D3.0mm_Horizontal_O3.81mm_Z6.0mm.FCStd")
print("created LED_D3.0mm_Horizontal_O3.81mm_Z6.0mm")


 # LED_D3.0mm_Horizontal_O6.35mm_Z6.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '3')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '3.8')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '6.35')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '3')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '5.3')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '6')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '1')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D3.0mm_Horizontal_O6.35mm_Z6.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D3.0mm_Horizontal_O6.35mm_Z6.0mm.FCStd")
print("created LED_D3.0mm_Horizontal_O6.35mm_Z6.0mm")


 # LED_D3.0mm_Horizontal_O1.27mm_Z10.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '3')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '3.8')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '1.27')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '3')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '5.3')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '10')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '1')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D3.0mm_Horizontal_O1.27mm_Z10.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D3.0mm_Horizontal_O1.27mm_Z10.0mm.FCStd")
print("created LED_D3.0mm_Horizontal_O1.27mm_Z10.0mm")


 # LED_D3.0mm_Horizontal_O3.81mm_Z10.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '3')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '3.8')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '3.81')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '3')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '5.3')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '10')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '1')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D3.0mm_Horizontal_O3.81mm_Z10.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D3.0mm_Horizontal_O3.81mm_Z10.0mm.FCStd")
print("created LED_D3.0mm_Horizontal_O3.81mm_Z10.0mm")


 # LED_D3.0mm_Horizontal_O6.35mm_Z10.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '3')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '3.8')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '6.35')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '3')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '5.3')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '10')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '1')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D3.0mm_Horizontal_O6.35mm_Z10.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D3.0mm_Horizontal_O6.35mm_Z10.0mm.FCStd")
print("created LED_D3.0mm_Horizontal_O6.35mm_Z10.0mm")


 # LED_D5.0mm_Horizontal_O1.27mm_Z3.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '5')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '5.8')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '1.27')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '5')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '8.6')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '3')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '1')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D5.0mm_Horizontal_O1.27mm_Z3.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D5.0mm_Horizontal_O1.27mm_Z3.0mm.FCStd")
print("created LED_D5.0mm_Horizontal_O1.27mm_Z3.0mm")


 # LED_D5.0mm_Horizontal_O3.81mm_Z3.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '5')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '5.8')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '3.81')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '5')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '8.6')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '3')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '1')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D5.0mm_Horizontal_O3.81mm_Z3.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D5.0mm_Horizontal_O3.81mm_Z3.0mm.FCStd")
print("created LED_D5.0mm_Horizontal_O3.81mm_Z3.0mm")


 # LED_D5.0mm_Horizontal_O6.35mm_Z3.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '5')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '5.8')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '6.35')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '5')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '8.6')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '3')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '1')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D5.0mm_Horizontal_O6.35mm_Z3.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D5.0mm_Horizontal_O6.35mm_Z3.0mm.FCStd")
print("created LED_D5.0mm_Horizontal_O6.35mm_Z3.0mm")


 # LED_D5.0mm_Horizontal_O1.27mm_Z9.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '5')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '5.8')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '1.27')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '5')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '8.6')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '9')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '1')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D5.0mm_Horizontal_O1.27mm_Z9.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D5.0mm_Horizontal_O1.27mm_Z9.0mm.FCStd")
print("created LED_D5.0mm_Horizontal_O1.27mm_Z9.0mm")


 # LED_D5.0mm_Horizontal_O3.81mm_Z9.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '5')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '5.8')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '3.81')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '5')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '8.6')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '9')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '1')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D5.0mm_Horizontal_O3.81mm_Z9.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D5.0mm_Horizontal_O3.81mm_Z9.0mm.FCStd")
print("created LED_D5.0mm_Horizontal_O3.81mm_Z9.0mm")


 # LED_D5.0mm_Horizontal_O6.35mm_Z9.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '5')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '5.8')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '6.35')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '5')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '8.6')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '9')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '1')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D5.0mm_Horizontal_O6.35mm_Z9.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D5.0mm_Horizontal_O6.35mm_Z9.0mm.FCStd")
print("created LED_D5.0mm_Horizontal_O6.35mm_Z9.0mm")


 # LED_D5.0mm_Horizontal_O1.27mm_Z15.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '5')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '5.8')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '1.27')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '5')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '8.6')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '15')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '1')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D5.0mm_Horizontal_O1.27mm_Z15.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D5.0mm_Horizontal_O1.27mm_Z15.0mm.FCStd")
print("created LED_D5.0mm_Horizontal_O1.27mm_Z15.0mm")


 # LED_D5.0mm_Horizontal_O3.81mm_Z15.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '5')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '5.8')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '3.81')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '5')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '8.6')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '15')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '1')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D5.0mm_Horizontal_O3.81mm_Z15.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D5.0mm_Horizontal_O3.81mm_Z15.0mm.FCStd")
print("created LED_D5.0mm_Horizontal_O3.81mm_Z15.0mm")


 # LED_D5.0mm_Horizontal_O6.35mm_Z15.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# dled
App.ActiveDocument.Spreadsheet.set('B1', '5')
# dledout
App.ActiveDocument.Spreadsheet.set('B2', '5.8')
# offsetled
App.ActiveDocument.Spreadsheet.set('B3', '6.35')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B6', '5')
# wled
App.ActiveDocument.Spreadsheet.set('B7', '8.6')
# ledypos
App.ActiveDocument.Spreadsheet.set('B8', '15')
# wledback
App.ActiveDocument.Spreadsheet.set('B9', '1')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D5.0mm_Horizontal_O6.35mm_Z15.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D5.0mm_Horizontal_O6.35mm_Z15.0mm.FCStd")
print("created LED_D5.0mm_Horizontal_O6.35mm_Z15.0mm")
