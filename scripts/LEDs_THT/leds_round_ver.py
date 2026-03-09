#
# SCRIPT to generate 3D models
#



 # LED_D3.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# rin
App.ActiveDocument.Spreadsheet.set('B1', '3')
# w
App.ActiveDocument.Spreadsheet.set('B2', '3.8')
# h
App.ActiveDocument.Spreadsheet.set('C2', '3.8')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B5', '4.3')
# H_bottom
App.ActiveDocument.Spreadsheet.set('B6', '1')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D3.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D3.0mm.FCStd")
print("created LED_D3.0mm")


 # LED_D3.0mm-3
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# rin
App.ActiveDocument.Spreadsheet.set('B1', '3')
# w
App.ActiveDocument.Spreadsheet.set('B2', '3.8')
# h
App.ActiveDocument.Spreadsheet.set('C2', '3.8')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B5', '4.3')
# H_bottom
App.ActiveDocument.Spreadsheet.set('B6', '1')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D3.0mm-3.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D3.0mm-3.FCStd")
print("created LED_D3.0mm-3")


 # LED_D5.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# rin
App.ActiveDocument.Spreadsheet.set('B1', '5')
# w
App.ActiveDocument.Spreadsheet.set('B2', '5.8')
# h
App.ActiveDocument.Spreadsheet.set('C2', '5.8')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B5', '7.6')
# H_bottom
App.ActiveDocument.Spreadsheet.set('B6', '1')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D5.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D5.0mm.FCStd")
print("created LED_D5.0mm")


 # LED_D5.0mm-3
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# rin
App.ActiveDocument.Spreadsheet.set('B1', '5')
# w
App.ActiveDocument.Spreadsheet.set('B2', '5.8')
# h
App.ActiveDocument.Spreadsheet.set('C2', '5.8')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B5', '7.6')
# H_bottom
App.ActiveDocument.Spreadsheet.set('B6', '1')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D5.0mm-3.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D5.0mm-3.FCStd")
print("created LED_D5.0mm-3")


 # LED_D5.0mm-4
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# rin
App.ActiveDocument.Spreadsheet.set('B1', '5')
# w
App.ActiveDocument.Spreadsheet.set('B2', '5.8')
# h
App.ActiveDocument.Spreadsheet.set('C2', '5.8')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '1.27')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B5', '7.6')
# H_bottom
App.ActiveDocument.Spreadsheet.set('B6', '1')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D5.0mm-4.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D5.0mm-4.FCStd")
print("created LED_D5.0mm-4")


 # LED_D4.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# rin
App.ActiveDocument.Spreadsheet.set('B1', '4')
# w
App.ActiveDocument.Spreadsheet.set('B2', '4.8')
# h
App.ActiveDocument.Spreadsheet.set('C2', '4.8')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B5', '6')
# H_bottom
App.ActiveDocument.Spreadsheet.set('B6', '1')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D4.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D4.0mm.FCStd")
print("created LED_D4.0mm")


 # LED_D8.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# rin
App.ActiveDocument.Spreadsheet.set('B1', '8')
# w
App.ActiveDocument.Spreadsheet.set('B2', '9')
# h
App.ActiveDocument.Spreadsheet.set('C2', '9')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B5', '9')
# H_bottom
App.ActiveDocument.Spreadsheet.set('B6', '2')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D8.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D8.0mm.FCStd")
print("created LED_D8.0mm")


 # LED_D8.0mm-3
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# rin
App.ActiveDocument.Spreadsheet.set('B1', '8')
# w
App.ActiveDocument.Spreadsheet.set('B2', '9')
# h
App.ActiveDocument.Spreadsheet.set('C2', '9')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B5', '9')
# H_bottom
App.ActiveDocument.Spreadsheet.set('B6', '2')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D8.0mm-3.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D8.0mm-3.FCStd")
print("created LED_D8.0mm-3")


 # LED_D10.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# rin
App.ActiveDocument.Spreadsheet.set('B1', '10')
# w
App.ActiveDocument.Spreadsheet.set('B2', '11')
# h
App.ActiveDocument.Spreadsheet.set('C2', '11')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B5', '11.5')
# H_bottom
App.ActiveDocument.Spreadsheet.set('B6', '2')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D10.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D10.0mm.FCStd")
print("created LED_D10.0mm")


 # LED_D10.0mm-3
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# rin
App.ActiveDocument.Spreadsheet.set('B1', '10')
# w
App.ActiveDocument.Spreadsheet.set('B2', '11')
# h
App.ActiveDocument.Spreadsheet.set('C2', '11')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B5', '11.5')
# H_bottom
App.ActiveDocument.Spreadsheet.set('B6', '2')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D10.0mm-3.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D10.0mm-3.FCStd")
print("created LED_D10.0mm-3")


 # LED_D20.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# rin
App.ActiveDocument.Spreadsheet.set('B1', '20')
# w
App.ActiveDocument.Spreadsheet.set('B2', '23')
# h
App.ActiveDocument.Spreadsheet.set('C2', '23')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B5', '10')
# H_bottom
App.ActiveDocument.Spreadsheet.set('B6', '3.5')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D20.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D20.0mm.FCStd")
print("created LED_D20.0mm")


 # LED_Oval_W5.2mm_H3.8mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# rin
App.ActiveDocument.Spreadsheet.set('B1', '0')
# w
App.ActiveDocument.Spreadsheet.set('B2', '5.2')
# h
App.ActiveDocument.Spreadsheet.set('C2', '3.8')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B5', '7')
# H_bottom
App.ActiveDocument.Spreadsheet.set('B6', '0')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_Oval_W5.2mm_H3.8mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_Oval_W5.2mm_H3.8mm.FCStd")
print("created LED_Oval_W5.2mm_H3.8mm")


 # LED_D2.0mm_W4.8mm_H2.5mm_FlatTop
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# rin
App.ActiveDocument.Spreadsheet.set('B1', '2')
# w
App.ActiveDocument.Spreadsheet.set('B2', '4.8')
# h
App.ActiveDocument.Spreadsheet.set('C2', '2.5')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B5', '4.5')
# H_bottom
App.ActiveDocument.Spreadsheet.set('B6', '3.5')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D2.0mm_W4.8mm_H2.5mm_FlatTop.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D2.0mm_W4.8mm_H2.5mm_FlatTop.FCStd")
print("created LED_D2.0mm_W4.8mm_H2.5mm_FlatTop")


 # LED_D1.8mm_W3.3mm_H2.4mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# rin
App.ActiveDocument.Spreadsheet.set('B1', '1.8')
# w
App.ActiveDocument.Spreadsheet.set('B2', '3.3')
# h
App.ActiveDocument.Spreadsheet.set('C2', '2.4')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B5', '1.4')
# H_bottom
App.ActiveDocument.Spreadsheet.set('B6', '1.6')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D1.8mm_W3.3mm_H2.4mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D1.8mm_W3.3mm_H2.4mm.FCStd")
print("created LED_D1.8mm_W3.3mm_H2.4mm")


 # LED_D3.0mm_FlatTop
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# rin
App.ActiveDocument.Spreadsheet.set('B1', '3')
# w
App.ActiveDocument.Spreadsheet.set('B2', '3.8')
# h
App.ActiveDocument.Spreadsheet.set('C2', '3.8')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B5', '4.8')
# H_bottom
App.ActiveDocument.Spreadsheet.set('B6', '1.2000000000000002')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D3.0mm_FlatTop.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D3.0mm_FlatTop.FCStd")
print("created LED_D3.0mm_FlatTop")


 # LED_D5.0mm_FlatTop
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# rin
App.ActiveDocument.Spreadsheet.set('B1', '5')
# w
App.ActiveDocument.Spreadsheet.set('B2', '5.9')
# h
App.ActiveDocument.Spreadsheet.set('C2', '5.9')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B5', '8.6')
# H_bottom
App.ActiveDocument.Spreadsheet.set('B6', '1')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D5.0mm_FlatTop.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D5.0mm_FlatTop.FCStd")
print("created LED_D5.0mm_FlatTop")


 # LED_D2.0mm_W4.0mm_H2.8mm_FlatTop
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# rin
App.ActiveDocument.Spreadsheet.set('B1', '2')
# w
App.ActiveDocument.Spreadsheet.set('B2', '4')
# h
App.ActiveDocument.Spreadsheet.set('C2', '2.8')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B5', '1.95')
# H_bottom
App.ActiveDocument.Spreadsheet.set('B6', '3.05')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_D2.0mm_W4.0mm_H2.8mm_FlatTop.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_D2.0mm_W4.0mm_H2.8mm_FlatTop.FCStd")
print("created LED_D2.0mm_W4.0mm_H2.8mm_FlatTop")


 # LED_Rectangular_W3.9mm_H1.8mm_FlatTop
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# rin
App.ActiveDocument.Spreadsheet.set('B1', '0')
# w
App.ActiveDocument.Spreadsheet.set('B2', '3.9')
# h
App.ActiveDocument.Spreadsheet.set('C2', '1.75')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B5', '7')
# H_bottom
App.ActiveDocument.Spreadsheet.set('B6', '0')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_Rectangular_W3.9mm_H1.8mm_FlatTop.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_Rectangular_W3.9mm_H1.8mm_FlatTop.FCStd")
print("created LED_Rectangular_W3.9mm_H1.8mm_FlatTop")


 # LED_Rectangular_W3.9mm_H1.9mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# rin
App.ActiveDocument.Spreadsheet.set('B1', '0')
# w
App.ActiveDocument.Spreadsheet.set('B2', '3.9')
# h
App.ActiveDocument.Spreadsheet.set('C2', '1.9')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B5', '7')
# H_bottom
App.ActiveDocument.Spreadsheet.set('B6', '0')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_Rectangular_W3.9mm_H1.9mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_Rectangular_W3.9mm_H1.9mm.FCStd")
print("created LED_Rectangular_W3.9mm_H1.9mm")


 # LED_Rectangular_W3.0mm_H2.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# rin
App.ActiveDocument.Spreadsheet.set('B1', '0')
# w
App.ActiveDocument.Spreadsheet.set('B2', '3')
# h
App.ActiveDocument.Spreadsheet.set('C2', '2')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B5', '7')
# H_bottom
App.ActiveDocument.Spreadsheet.set('B6', '0')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_Rectangular_W3.0mm_H2.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_Rectangular_W3.0mm_H2.0mm.FCStd")
print("created LED_Rectangular_W3.0mm_H2.0mm")


 # LED_Rectangular_W5.0mm_H2.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# rin
App.ActiveDocument.Spreadsheet.set('B1', '0')
# w
App.ActiveDocument.Spreadsheet.set('B2', '5')
# h
App.ActiveDocument.Spreadsheet.set('C2', '2')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B5', '9.7')
# H_bottom
App.ActiveDocument.Spreadsheet.set('B6', '0')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_Rectangular_W5.0mm_H2.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_Rectangular_W5.0mm_H2.0mm.FCStd")
print("created LED_Rectangular_W5.0mm_H2.0mm")


 # LED_Rectangular_W5.0mm_H2.0mm-3pins
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# rin
App.ActiveDocument.Spreadsheet.set('B1', '0')
# w
App.ActiveDocument.Spreadsheet.set('B2', '5')
# h
App.ActiveDocument.Spreadsheet.set('C2', '2')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B5', '9.7')
# H_bottom
App.ActiveDocument.Spreadsheet.set('B6', '0')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_Rectangular_W5.0mm_H2.0mm-3pins.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_Rectangular_W5.0mm_H2.0mm-3pins.FCStd")
print("created LED_Rectangular_W5.0mm_H2.0mm-3pins")


 # LED_Rectangular_W5.0mm_H5.0mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# rin
App.ActiveDocument.Spreadsheet.set('B1', '0')
# w
App.ActiveDocument.Spreadsheet.set('B2', '5')
# h
App.ActiveDocument.Spreadsheet.set('C2', '5')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B5', '9.7')
# H_bottom
App.ActiveDocument.Spreadsheet.set('B6', '0')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_Rectangular_W5.0mm_H5.0mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_Rectangular_W5.0mm_H5.0mm.FCStd")
print("created LED_Rectangular_W5.0mm_H5.0mm")


 # LED_SideEmitter_Rectangular_W4.5mm_H1.6mm
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# rin
App.ActiveDocument.Spreadsheet.set('B1', '0')
# w
App.ActiveDocument.Spreadsheet.set('B2', '4.5')
# h
App.ActiveDocument.Spreadsheet.set('C2', '1.6')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.6000000000000001')
# H
App.ActiveDocument.Spreadsheet.set('B5', '5.7')
# H_bottom
App.ActiveDocument.Spreadsheet.set('B6', '0')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"LED_SideEmitter_Rectangular_W4.5mm_H1.6mm.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"LED_SideEmitter_Rectangular_W4.5mm_H1.6mm.FCStd")
print("created LED_SideEmitter_Rectangular_W4.5mm_H1.6mm")
