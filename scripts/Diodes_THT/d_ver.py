#
# SCRIPT to generate 3D models
#



 # D_DO-27_P5.08mm_Vertical_AnodeUp
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '9.52')
# d
App.ActiveDocument.Spreadsheet.set('B2', '5.33')
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

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"D_DO-27_P5.08mm_Vertical_AnodeUp.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"D_DO-27_P5.08mm_Vertical_AnodeUp.FCStd")
print("created D_DO-27_P5.08mm_Vertical_AnodeUp")


 # D_DO-41_SOD81_P2.54mm_Vertical_AnodeUp
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '5.2')
# d
App.ActiveDocument.Spreadsheet.set('B2', '2.7')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"D_DO-41_SOD81_P2.54mm_Vertical_AnodeUp.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"D_DO-41_SOD81_P2.54mm_Vertical_AnodeUp.FCStd")
print("created D_DO-41_SOD81_P2.54mm_Vertical_AnodeUp")


 # D_DO-41_SOD81_P3.81mm_Vertical_AnodeUp
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '5.2')
# d
App.ActiveDocument.Spreadsheet.set('B2', '2.7')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '3.81')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"D_DO-41_SOD81_P3.81mm_Vertical_AnodeUp.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"D_DO-41_SOD81_P3.81mm_Vertical_AnodeUp.FCStd")
print("created D_DO-41_SOD81_P3.81mm_Vertical_AnodeUp")


 # D_DO-41_SOD81_P5.08mm_Vertical_AnodeUp
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '5.2')
# d
App.ActiveDocument.Spreadsheet.set('B2', '2.7')
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

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"D_DO-41_SOD81_P5.08mm_Vertical_AnodeUp.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"D_DO-41_SOD81_P5.08mm_Vertical_AnodeUp.FCStd")
print("created D_DO-41_SOD81_P5.08mm_Vertical_AnodeUp")


 # D_DO-34_SOD68_P2.54mm_Vertical_AnodeUp
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '3.04')
# d
App.ActiveDocument.Spreadsheet.set('B2', '1.6')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.45')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"D_DO-34_SOD68_P2.54mm_Vertical_AnodeUp.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"D_DO-34_SOD68_P2.54mm_Vertical_AnodeUp.FCStd")
print("created D_DO-34_SOD68_P2.54mm_Vertical_AnodeUp")


 # D_DO-34_SOD68_P5.08mm_Vertical_AnodeUp
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '3.04')
# d
App.ActiveDocument.Spreadsheet.set('B2', '1.6')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '5.08')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.45')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"D_DO-34_SOD68_P5.08mm_Vertical_AnodeUp.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"D_DO-34_SOD68_P5.08mm_Vertical_AnodeUp.FCStd")
print("created D_DO-34_SOD68_P5.08mm_Vertical_AnodeUp")


 # D_A-405_P2.54mm_Vertical_AnodeUp
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '5.2')
# d
App.ActiveDocument.Spreadsheet.set('B2', '2.7')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.6000000000000001')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"D_A-405_P2.54mm_Vertical_AnodeUp.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"D_A-405_P2.54mm_Vertical_AnodeUp.FCStd")
print("created D_A-405_P2.54mm_Vertical_AnodeUp")


 # D_A-405_P5.08mm_Vertical_AnodeUp
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '5.2')
# d
App.ActiveDocument.Spreadsheet.set('B2', '2.7')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '5.08')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.6000000000000001')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"D_A-405_P5.08mm_Vertical_AnodeUp.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"D_A-405_P5.08mm_Vertical_AnodeUp.FCStd")
print("created D_A-405_P5.08mm_Vertical_AnodeUp")


 # D_DO-15_P2.54mm_Vertical_AnodeUp
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '7.6')
# d
App.ActiveDocument.Spreadsheet.set('B2', '3.6')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '2.54')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8999999999999999')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"D_DO-15_P2.54mm_Vertical_AnodeUp.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"D_DO-15_P2.54mm_Vertical_AnodeUp.FCStd")
print("created D_DO-15_P2.54mm_Vertical_AnodeUp")


 # D_DO-15_P3.81mm_Vertical_AnodeUp
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '7.6')
# d
App.ActiveDocument.Spreadsheet.set('B2', '3.6')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '3.81')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.8999999999999999')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"D_DO-15_P3.81mm_Vertical_AnodeUp.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"D_DO-15_P3.81mm_Vertical_AnodeUp.FCStd")
print("created D_DO-15_P3.81mm_Vertical_AnodeUp")


 # D_DO-15_P5.08mm_Vertical_AnodeUp
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '7.6')
# d
App.ActiveDocument.Spreadsheet.set('B2', '3.6')
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

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"D_DO-15_P5.08mm_Vertical_AnodeUp.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"D_DO-15_P5.08mm_Vertical_AnodeUp.FCStd")
print("created D_DO-15_P5.08mm_Vertical_AnodeUp")


 # D_DO-201_P3.81mm_Vertical_AnodeUp
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '9.53')
# d
App.ActiveDocument.Spreadsheet.set('B2', '5.21')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '3.81')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '1.0')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"D_DO-201_P3.81mm_Vertical_AnodeUp.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"D_DO-201_P3.81mm_Vertical_AnodeUp.FCStd")
print("created D_DO-201_P3.81mm_Vertical_AnodeUp")


 # D_DO-201_P5.08mm_Vertical_AnodeUp
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '9.53')
# d
App.ActiveDocument.Spreadsheet.set('B2', '5.21')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '5.08')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '1.0')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"D_DO-201_P5.08mm_Vertical_AnodeUp.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"D_DO-201_P5.08mm_Vertical_AnodeUp.FCStd")
print("created D_DO-201_P5.08mm_Vertical_AnodeUp")


 # D_DO-201AD_P3.81mm_Vertical_AnodeUp
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '9.5')
# d
App.ActiveDocument.Spreadsheet.set('B2', '5.2')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '3.81')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '1.3')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"D_DO-201AD_P3.81mm_Vertical_AnodeUp.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"D_DO-201AD_P3.81mm_Vertical_AnodeUp.FCStd")
print("created D_DO-201AD_P3.81mm_Vertical_AnodeUp")


 # D_DO-201AD_P5.08mm_Vertical_AnodeUp
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '9.5')
# d
App.ActiveDocument.Spreadsheet.set('B2', '5.2')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '5.08')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '1.3')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"D_DO-201AD_P5.08mm_Vertical_AnodeUp.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"D_DO-201AD_P5.08mm_Vertical_AnodeUp.FCStd")
print("created D_DO-201AD_P5.08mm_Vertical_AnodeUp")


 # D_DO-201AE_P3.81mm_Vertical_AnodeUp
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '9')
# d
App.ActiveDocument.Spreadsheet.set('B2', '5.3')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '3.81')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '1.0')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"D_DO-201AE_P3.81mm_Vertical_AnodeUp.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"D_DO-201AE_P3.81mm_Vertical_AnodeUp.FCStd")
print("created D_DO-201AE_P3.81mm_Vertical_AnodeUp")


 # D_DO-201AE_P5.08mm_Vertical_AnodeUp
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '9')
# d
App.ActiveDocument.Spreadsheet.set('B2', '5.3')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '5.08')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '1.0')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"D_DO-201AE_P5.08mm_Vertical_AnodeUp.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"D_DO-201AE_P5.08mm_Vertical_AnodeUp.FCStd")
print("created D_DO-201AE_P5.08mm_Vertical_AnodeUp")


 # D_P600_R-6_P7.62mm_Vertical_AnodeUp
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '9.1')
# d
App.ActiveDocument.Spreadsheet.set('B2', '9.1')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '7.62')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '1.3')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"D_P600_R-6_P7.62mm_Vertical_AnodeUp.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"D_P600_R-6_P7.62mm_Vertical_AnodeUp.FCStd")
print("created D_P600_R-6_P7.62mm_Vertical_AnodeUp")


 # D_5W_P5.08mm_Vertical_AnodeUp
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '8.9')
# d
App.ActiveDocument.Spreadsheet.set('B2', '3.7')
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

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"D_5W_P5.08mm_Vertical_AnodeUp.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"D_5W_P5.08mm_Vertical_AnodeUp.FCStd")
print("created D_5W_P5.08mm_Vertical_AnodeUp")


 # D_5KP_P7.62mm_Vertical_AnodeUp
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '7.62')
# d
App.ActiveDocument.Spreadsheet.set('B2', '9.53')
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

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"D_5KP_P7.62mm_Vertical_AnodeUp.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"D_5KP_P7.62mm_Vertical_AnodeUp.FCStd")
print("created D_5KP_P7.62mm_Vertical_AnodeUp")


 # D_5KPW_P7.62mm_Vertical_AnodeUp
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '9')
# d
App.ActiveDocument.Spreadsheet.set('B2', '8')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '7.62')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '1.3')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"D_5KPW_P7.62mm_Vertical_AnodeUp.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"D_5KPW_P7.62mm_Vertical_AnodeUp.FCStd")
print("created D_5KPW_P7.62mm_Vertical_AnodeUp")
