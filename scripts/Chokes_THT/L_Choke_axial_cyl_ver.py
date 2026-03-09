#
# SCRIPT to generate 3D models
#



 # L_Axial_L9.5mm_D4.0mm_P2.54mm_Vertical_Fastron_SMCC
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '9.5')
# d
App.ActiveDocument.Spreadsheet.set('B2', '4')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.7')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L9.5mm_D4.0mm_P2.54mm_Vertical_Fastron_SMCC.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L9.5mm_D4.0mm_P2.54mm_Vertical_Fastron_SMCC.FCStd")
print("created L_Axial_L9.5mm_D4.0mm_P2.54mm_Vertical_Fastron_SMCC")


 # L_Axial_L9.5mm_D4.0mm_P5.08mm_Vertical_Fastron_SMCC
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '9.5')
# d
App.ActiveDocument.Spreadsheet.set('B2', '4')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '5.08')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.7')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L9.5mm_D4.0mm_P5.08mm_Vertical_Fastron_SMCC.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L9.5mm_D4.0mm_P5.08mm_Vertical_Fastron_SMCC.FCStd")
print("created L_Axial_L9.5mm_D4.0mm_P5.08mm_Vertical_Fastron_SMCC")


 # L_Axial_L7.0mm_D3.3mm_P2.54mm_Vertical_Fastron_MICC
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '7')
# d
App.ActiveDocument.Spreadsheet.set('B2', '3.3')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.5')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L7.0mm_D3.3mm_P2.54mm_Vertical_Fastron_MICC.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L7.0mm_D3.3mm_P2.54mm_Vertical_Fastron_MICC.FCStd")
print("created L_Axial_L7.0mm_D3.3mm_P2.54mm_Vertical_Fastron_MICC")


 # L_Axial_L7.0mm_D3.3mm_P5.08mm_Vertical_Fastron_MICC
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '7')
# d
App.ActiveDocument.Spreadsheet.set('B2', '3.3')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '5.08')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.5')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L7.0mm_D3.3mm_P5.08mm_Vertical_Fastron_MICC.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L7.0mm_D3.3mm_P5.08mm_Vertical_Fastron_MICC.FCStd")
print("created L_Axial_L7.0mm_D3.3mm_P5.08mm_Vertical_Fastron_MICC")


 # L_Axial_L24.0mm_D7.5mm_P5.08mm_Vertical_Fastron_MESC
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '24')
# d
App.ActiveDocument.Spreadsheet.set('B2', '7.5')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '5.08')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8999999999999999')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L24.0mm_D7.5mm_P5.08mm_Vertical_Fastron_MESC.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L24.0mm_D7.5mm_P5.08mm_Vertical_Fastron_MESC.FCStd")
print("created L_Axial_L24.0mm_D7.5mm_P5.08mm_Vertical_Fastron_MESC")


 # L_Axial_L24.0mm_D7.5mm_P7.62mm_Vertical_Fastron_MESC
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '24')
# d
App.ActiveDocument.Spreadsheet.set('B2', '7.5')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '7.62')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8999999999999999')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L24.0mm_D7.5mm_P7.62mm_Vertical_Fastron_MESC.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L24.0mm_D7.5mm_P7.62mm_Vertical_Fastron_MESC.FCStd")
print("created L_Axial_L24.0mm_D7.5mm_P7.62mm_Vertical_Fastron_MESC")


 # L_Axial_L16.0mm_D7.5mm_P5.08mm_Vertical_Fastron_XHBCC
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '16')
# d
App.ActiveDocument.Spreadsheet.set('B2', '7.5')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '5.08')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L16.0mm_D7.5mm_P5.08mm_Vertical_Fastron_XHBCC.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L16.0mm_D7.5mm_P5.08mm_Vertical_Fastron_XHBCC.FCStd")
print("created L_Axial_L16.0mm_D7.5mm_P5.08mm_Vertical_Fastron_XHBCC")


 # L_Axial_L16.0mm_D7.5mm_P7.62mm_Vertical_Fastron_XHBCC
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '16')
# d
App.ActiveDocument.Spreadsheet.set('B2', '7.5')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '7.62')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L16.0mm_D7.5mm_P7.62mm_Vertical_Fastron_XHBCC.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L16.0mm_D7.5mm_P7.62mm_Vertical_Fastron_XHBCC.FCStd")
print("created L_Axial_L16.0mm_D7.5mm_P7.62mm_Vertical_Fastron_XHBCC")


 # L_Axial_L16.0mm_D6.3mm_P5.08mm_Vertical_Fastron_VHBCC
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '16')
# d
App.ActiveDocument.Spreadsheet.set('B2', '6.3')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '5.08')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L16.0mm_D6.3mm_P5.08mm_Vertical_Fastron_VHBCC.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L16.0mm_D6.3mm_P5.08mm_Vertical_Fastron_VHBCC.FCStd")
print("created L_Axial_L16.0mm_D6.3mm_P5.08mm_Vertical_Fastron_VHBCC")


 # L_Axial_L16.0mm_D6.3mm_P7.62mm_Vertical_Fastron_VHBCC
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '16')
# d
App.ActiveDocument.Spreadsheet.set('B2', '6.3')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '7.62')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L16.0mm_D6.3mm_P7.62mm_Vertical_Fastron_VHBCC.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L16.0mm_D6.3mm_P7.62mm_Vertical_Fastron_VHBCC.FCStd")
print("created L_Axial_L16.0mm_D6.3mm_P7.62mm_Vertical_Fastron_VHBCC")


 # L_Axial_L14.5mm_D5.8mm_P5.08mm_Vertical_Fastron_HBCC
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '14.5')
# d
App.ActiveDocument.Spreadsheet.set('B2', '5.8')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '5.08')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L14.5mm_D5.8mm_P5.08mm_Vertical_Fastron_HBCC.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L14.5mm_D5.8mm_P5.08mm_Vertical_Fastron_HBCC.FCStd")
print("created L_Axial_L14.5mm_D5.8mm_P5.08mm_Vertical_Fastron_HBCC")


 # L_Axial_L14.5mm_D5.8mm_P7.62mm_Vertical_Fastron_HBCC
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '14.5')
# d
App.ActiveDocument.Spreadsheet.set('B2', '5.8')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '7.62')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L14.5mm_D5.8mm_P7.62mm_Vertical_Fastron_HBCC.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L14.5mm_D5.8mm_P7.62mm_Vertical_Fastron_HBCC.FCStd")
print("created L_Axial_L14.5mm_D5.8mm_P7.62mm_Vertical_Fastron_HBCC")


 # L_Axial_L12.8mm_D5.8mm_P5.08mm_Vertical_Fastron_HBCC
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '12.8')
# d
App.ActiveDocument.Spreadsheet.set('B2', '5.8')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '5.08')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L12.8mm_D5.8mm_P5.08mm_Vertical_Fastron_HBCC.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L12.8mm_D5.8mm_P5.08mm_Vertical_Fastron_HBCC.FCStd")
print("created L_Axial_L12.8mm_D5.8mm_P5.08mm_Vertical_Fastron_HBCC")


 # L_Axial_L12.8mm_D5.8mm_P7.62mm_Vertical_Fastron_HBCC
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '12.8')
# d
App.ActiveDocument.Spreadsheet.set('B2', '5.8')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '7.62')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L12.8mm_D5.8mm_P7.62mm_Vertical_Fastron_HBCC.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L12.8mm_D5.8mm_P7.62mm_Vertical_Fastron_HBCC.FCStd")
print("created L_Axial_L12.8mm_D5.8mm_P7.62mm_Vertical_Fastron_HBCC")


 # L_Axial_L12.0mm_D5.0mm_P5.08mm_Vertical_Fastron_MISC
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '12')
# d
App.ActiveDocument.Spreadsheet.set('B2', '5')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '5.08')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8999999999999999')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L12.0mm_D5.0mm_P5.08mm_Vertical_Fastron_MISC.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L12.0mm_D5.0mm_P5.08mm_Vertical_Fastron_MISC.FCStd")
print("created L_Axial_L12.0mm_D5.0mm_P5.08mm_Vertical_Fastron_MISC")


 # L_Axial_L12.0mm_D5.0mm_P7.62mm_Vertical_Fastron_MISC
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '12')
# d
App.ActiveDocument.Spreadsheet.set('B2', '5')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '7.62')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8999999999999999')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L12.0mm_D5.0mm_P7.62mm_Vertical_Fastron_MISC.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L12.0mm_D5.0mm_P7.62mm_Vertical_Fastron_MISC.FCStd")
print("created L_Axial_L12.0mm_D5.0mm_P7.62mm_Vertical_Fastron_MISC")


 # L_Axial_L11.0mm_D4.5mm_P5.08mm_Vertical_Fastron_MECC
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '11')
# d
App.ActiveDocument.Spreadsheet.set('B2', '4.5')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '5.08')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.7')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L11.0mm_D4.5mm_P5.08mm_Vertical_Fastron_MECC.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L11.0mm_D4.5mm_P5.08mm_Vertical_Fastron_MECC.FCStd")
print("created L_Axial_L11.0mm_D4.5mm_P5.08mm_Vertical_Fastron_MECC")


 # L_Axial_L11.0mm_D4.5mm_P7.62mm_Vertical_Fastron_MECC
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '11')
# d
App.ActiveDocument.Spreadsheet.set('B2', '4.5')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '7.62')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.7')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L11.0mm_D4.5mm_P7.62mm_Vertical_Fastron_MECC.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L11.0mm_D4.5mm_P7.62mm_Vertical_Fastron_MECC.FCStd")
print("created L_Axial_L11.0mm_D4.5mm_P7.62mm_Vertical_Fastron_MECC")


 # L_Axial_L13.0mm_D4.5mm_P5.08mm_Vertical_Fastron_HCCC
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '13')
# d
App.ActiveDocument.Spreadsheet.set('B2', '4.5')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '5.08')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8999999999999999')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L13.0mm_D4.5mm_P5.08mm_Vertical_Fastron_HCCC.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L13.0mm_D4.5mm_P5.08mm_Vertical_Fastron_HCCC.FCStd")
print("created L_Axial_L13.0mm_D4.5mm_P5.08mm_Vertical_Fastron_HCCC")


 # L_Axial_L13.0mm_D4.5mm_P7.62mm_Vertical_Fastron_HCCC
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '13')
# d
App.ActiveDocument.Spreadsheet.set('B2', '4.5')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '7.62')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8999999999999999')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L13.0mm_D4.5mm_P7.62mm_Vertical_Fastron_HCCC.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L13.0mm_D4.5mm_P7.62mm_Vertical_Fastron_HCCC.FCStd")
print("created L_Axial_L13.0mm_D4.5mm_P7.62mm_Vertical_Fastron_HCCC")


 # L_Axial_L14.0mm_D4.5mm_P5.08mm_Vertical_Fastron_LACC
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '14')
# d
App.ActiveDocument.Spreadsheet.set('B2', '4.5')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '5.08')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.7')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L14.0mm_D4.5mm_P5.08mm_Vertical_Fastron_LACC.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L14.0mm_D4.5mm_P5.08mm_Vertical_Fastron_LACC.FCStd")
print("created L_Axial_L14.0mm_D4.5mm_P5.08mm_Vertical_Fastron_LACC")


 # L_Axial_L14.0mm_D4.5mm_P7.62mm_Vertical_Fastron_LACC
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '14')
# d
App.ActiveDocument.Spreadsheet.set('B2', '4.5')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '7.62')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.7')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L14.0mm_D4.5mm_P7.62mm_Vertical_Fastron_LACC.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L14.0mm_D4.5mm_P7.62mm_Vertical_Fastron_LACC.FCStd")
print("created L_Axial_L14.0mm_D4.5mm_P7.62mm_Vertical_Fastron_LACC")


 # L_Axial_L20.0mm_D8.0mm_P5.08mm_Vertical
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '20')
# d
App.ActiveDocument.Spreadsheet.set('B2', '8')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '5.08')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8999999999999999')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L20.0mm_D8.0mm_P5.08mm_Vertical.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L20.0mm_D8.0mm_P5.08mm_Vertical.FCStd")
print("created L_Axial_L20.0mm_D8.0mm_P5.08mm_Vertical")


 # L_Axial_L20.0mm_D8.0mm_P7.62mm_Vertical
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '20')
# d
App.ActiveDocument.Spreadsheet.set('B2', '8')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '7.62')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8999999999999999')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L20.0mm_D8.0mm_P7.62mm_Vertical.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L20.0mm_D8.0mm_P7.62mm_Vertical.FCStd")
print("created L_Axial_L20.0mm_D8.0mm_P7.62mm_Vertical")


 # L_Axial_L30.0mm_D8.0mm_P5.08mm_Vertical_Fastron_77A
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '30')
# d
App.ActiveDocument.Spreadsheet.set('B2', '8')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '5.08')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '1.0999999999999999')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L30.0mm_D8.0mm_P5.08mm_Vertical_Fastron_77A.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L30.0mm_D8.0mm_P5.08mm_Vertical_Fastron_77A.FCStd")
print("created L_Axial_L30.0mm_D8.0mm_P5.08mm_Vertical_Fastron_77A")


 # L_Axial_L30.0mm_D8.0mm_P7.62mm_Vertical_Fastron_77A
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '30')
# d
App.ActiveDocument.Spreadsheet.set('B2', '8')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '7.62')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '1.0999999999999999')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L30.0mm_D8.0mm_P7.62mm_Vertical_Fastron_77A.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L30.0mm_D8.0mm_P7.62mm_Vertical_Fastron_77A.FCStd")
print("created L_Axial_L30.0mm_D8.0mm_P7.62mm_Vertical_Fastron_77A")


 # L_Axial_L26.0mm_D9.0mm_P5.08mm_Vertical_Fastron_77A
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '26')
# d
App.ActiveDocument.Spreadsheet.set('B2', '9')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '5.08')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8999999999999999')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L26.0mm_D9.0mm_P5.08mm_Vertical_Fastron_77A.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L26.0mm_D9.0mm_P5.08mm_Vertical_Fastron_77A.FCStd")
print("created L_Axial_L26.0mm_D9.0mm_P5.08mm_Vertical_Fastron_77A")


 # L_Axial_L26.0mm_D9.0mm_P7.62mm_Vertical_Fastron_77A
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '26')
# d
App.ActiveDocument.Spreadsheet.set('B2', '9')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '7.62')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8999999999999999')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L26.0mm_D9.0mm_P7.62mm_Vertical_Fastron_77A.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L26.0mm_D9.0mm_P7.62mm_Vertical_Fastron_77A.FCStd")
print("created L_Axial_L26.0mm_D9.0mm_P7.62mm_Vertical_Fastron_77A")


 # L_Axial_L26.0mm_D10.0mm_P5.08mm_Vertical_Fastron_77A
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '26')
# d
App.ActiveDocument.Spreadsheet.set('B2', '10')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '5.08')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8999999999999999')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L26.0mm_D10.0mm_P5.08mm_Vertical_Fastron_77A.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L26.0mm_D10.0mm_P5.08mm_Vertical_Fastron_77A.FCStd")
print("created L_Axial_L26.0mm_D10.0mm_P5.08mm_Vertical_Fastron_77A")


 # L_Axial_L26.0mm_D10.0mm_P7.62mm_Vertical_Fastron_77A
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '26')
# d
App.ActiveDocument.Spreadsheet.set('B2', '10')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '7.62')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8999999999999999')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L26.0mm_D10.0mm_P7.62mm_Vertical_Fastron_77A.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L26.0mm_D10.0mm_P7.62mm_Vertical_Fastron_77A.FCStd")
print("created L_Axial_L26.0mm_D10.0mm_P7.62mm_Vertical_Fastron_77A")


 # L_Axial_L26.0mm_D11.0mm_P5.08mm_Vertical_Fastron_77A
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '26')
# d
App.ActiveDocument.Spreadsheet.set('B2', '11')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '5.08')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8999999999999999')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L26.0mm_D11.0mm_P5.08mm_Vertical_Fastron_77A.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L26.0mm_D11.0mm_P5.08mm_Vertical_Fastron_77A.FCStd")
print("created L_Axial_L26.0mm_D11.0mm_P5.08mm_Vertical_Fastron_77A")


 # L_Axial_L26.0mm_D11.0mm_P7.62mm_Vertical_Fastron_77A
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '26')
# d
App.ActiveDocument.Spreadsheet.set('B2', '11')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '7.62')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8999999999999999')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L26.0mm_D11.0mm_P7.62mm_Vertical_Fastron_77A.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L26.0mm_D11.0mm_P7.62mm_Vertical_Fastron_77A.FCStd")
print("created L_Axial_L26.0mm_D11.0mm_P7.62mm_Vertical_Fastron_77A")


 # L_Axial_L5.3mm_D2.2mm_P2.54mm_Vertical_Vishay_IM-1
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '5.3')
# d
App.ActiveDocument.Spreadsheet.set('B2', '2.2')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.5')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L5.3mm_D2.2mm_P2.54mm_Vertical_Vishay_IM-1.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L5.3mm_D2.2mm_P2.54mm_Vertical_Vishay_IM-1.FCStd")
print("created L_Axial_L5.3mm_D2.2mm_P2.54mm_Vertical_Vishay_IM-1")


 # L_Axial_L6.6mm_D2.7mm_P2.54mm_Vertical_Vishay_IM-2
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '6.6')
# d
App.ActiveDocument.Spreadsheet.set('B2', '2.7')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.5')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L6.6mm_D2.7mm_P2.54mm_Vertical_Vishay_IM-2.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L6.6mm_D2.7mm_P2.54mm_Vertical_Vishay_IM-2.FCStd")
print("created L_Axial_L6.6mm_D2.7mm_P2.54mm_Vertical_Vishay_IM-2")


 # L_Axial_L24.0mm_D7.1mm_P5.08mm_Vertical_Vishay_IM-10-28
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '24')
# d
App.ActiveDocument.Spreadsheet.set('B2', '7.1')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '5.08')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.7')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L24.0mm_D7.1mm_P5.08mm_Vertical_Vishay_IM-10-28.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L24.0mm_D7.1mm_P5.08mm_Vertical_Vishay_IM-10-28.FCStd")
print("created L_Axial_L24.0mm_D7.1mm_P5.08mm_Vertical_Vishay_IM-10-28")


 # L_Axial_L24.0mm_D7.1mm_P5.08mm_Vertical_Vishay_IM-10-28
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '24')
# d
App.ActiveDocument.Spreadsheet.set('B2', '7.1')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '5.08')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.7')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L24.0mm_D7.1mm_P5.08mm_Vertical_Vishay_IM-10-28.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L24.0mm_D7.1mm_P5.08mm_Vertical_Vishay_IM-10-28.FCStd")
print("created L_Axial_L24.0mm_D7.1mm_P5.08mm_Vertical_Vishay_IM-10-28")


 # L_Axial_L16.0mm_D9.5mm_P5.08mm_Vertical_Vishay_IM-10-37
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '16')
# d
App.ActiveDocument.Spreadsheet.set('B2', '9.5')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '5.08')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.7')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L16.0mm_D9.5mm_P5.08mm_Vertical_Vishay_IM-10-37.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L16.0mm_D9.5mm_P5.08mm_Vertical_Vishay_IM-10-37.FCStd")
print("created L_Axial_L16.0mm_D9.5mm_P5.08mm_Vertical_Vishay_IM-10-37")


 # L_Axial_L17.5mm_D12.0mm_P7.62mm_Vertical_Vishay_IM-10-46
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '17.5')
# d
App.ActiveDocument.Spreadsheet.set('B2', '12')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '7.62')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.7')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L17.5mm_D12.0mm_P7.62mm_Vertical_Vishay_IM-10-46.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L17.5mm_D12.0mm_P7.62mm_Vertical_Vishay_IM-10-46.FCStd")
print("created L_Axial_L17.5mm_D12.0mm_P7.62mm_Vertical_Vishay_IM-10-46")


 # L_Axial_L20.3mm_D12.1mm_P7.62mm_Vertical_Vishay_IHA-101
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '20.32')
# d
App.ActiveDocument.Spreadsheet.set('B2', '12.07')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '7.62')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8999999999999999')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L20.3mm_D12.1mm_P7.62mm_Vertical_Vishay_IHA-101.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L20.3mm_D12.1mm_P7.62mm_Vertical_Vishay_IHA-101.FCStd")
print("created L_Axial_L20.3mm_D12.1mm_P7.62mm_Vertical_Vishay_IHA-101")


 # L_Axial_L26.7mm_D12.1mm_P7.62mm_Vertical_Vishay_IHA-103
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '26.67')
# d
App.ActiveDocument.Spreadsheet.set('B2', '12.07')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '7.62')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8999999999999999')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L26.7mm_D12.1mm_P7.62mm_Vertical_Vishay_IHA-103.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L26.7mm_D12.1mm_P7.62mm_Vertical_Vishay_IHA-103.FCStd")
print("created L_Axial_L26.7mm_D12.1mm_P7.62mm_Vertical_Vishay_IHA-103")


 # L_Axial_L26.7mm_D14.0mm_P7.62mm_Vertical_Vishay_IHA-104
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '26.67')
# d
App.ActiveDocument.Spreadsheet.set('B2', '13.97')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '7.62')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8999999999999999')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L26.7mm_D14.0mm_P7.62mm_Vertical_Vishay_IHA-104.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L26.7mm_D14.0mm_P7.62mm_Vertical_Vishay_IHA-104.FCStd")
print("created L_Axial_L26.7mm_D14.0mm_P7.62mm_Vertical_Vishay_IHA-104")


 # L_Axial_L29.9mm_D14.0mm_P7.62mm_Vertical_Vishay_IHA-105
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '29.85')
# d
App.ActiveDocument.Spreadsheet.set('B2', '13.97')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '7.62')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8999999999999999')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L29.9mm_D14.0mm_P7.62mm_Vertical_Vishay_IHA-105.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L29.9mm_D14.0mm_P7.62mm_Vertical_Vishay_IHA-105.FCStd")
print("created L_Axial_L29.9mm_D14.0mm_P7.62mm_Vertical_Vishay_IHA-105")


 # L_Axial_L23.4mm_D12.7mm_P7.62mm_Vertical_Vishay_IHA-203
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '23.37')
# d
App.ActiveDocument.Spreadsheet.set('B2', '12.7')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '7.62')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8999999999999999')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L23.4mm_D12.7mm_P7.62mm_Vertical_Vishay_IHA-203.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L23.4mm_D12.7mm_P7.62mm_Vertical_Vishay_IHA-203.FCStd")
print("created L_Axial_L23.4mm_D12.7mm_P7.62mm_Vertical_Vishay_IHA-203")


 # L_Axial_L20.3mm_D12.7mm_P7.62mm_Vertical_Vishay_IHA-201
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '20.32')
# d
App.ActiveDocument.Spreadsheet.set('B2', '12.7')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '7.62')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8999999999999999')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L20.3mm_D12.7mm_P7.62mm_Vertical_Vishay_IHA-201.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"L_Axial_L20.3mm_D12.7mm_P7.62mm_Vertical_Vishay_IHA-201.FCStd")
print("created L_Axial_L20.3mm_D12.7mm_P7.62mm_Vertical_Vishay_IHA-201")
