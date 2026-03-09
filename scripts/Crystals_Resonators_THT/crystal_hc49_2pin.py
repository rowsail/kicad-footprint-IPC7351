#
# SCRIPT to generate 3D models
#



 # Crystal_HC49-U_Vertical
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '10.9')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '10')
# H
App.ActiveDocument.Spreadsheet.set('B2', '4.65')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '4')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '13')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '4.88')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.5')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC49-U_Vertical.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC49-U_Vertical.FCStd")
print("created Crystal_HC49-U_Vertical")


 # Crystal_HC49-4H_Vertical
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '11.05')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '10')
# H
App.ActiveDocument.Spreadsheet.set('B2', '4.65')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '4')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '4')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '4.88')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.5')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC49-4H_Vertical.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC49-4H_Vertical.FCStd")
print("created Crystal_HC49-4H_Vertical")


 # Crystal_HC18-U_Vertical
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '10.9')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '10')
# H
App.ActiveDocument.Spreadsheet.set('B2', '4.65')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '4')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '13')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '4.9')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.5')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC18-U_Vertical.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC18-U_Vertical.FCStd")
print("created Crystal_HC18-U_Vertical")


 # Crystal_HC33-U_Vertical
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '19.23')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '18.42')
# H
App.ActiveDocument.Spreadsheet.set('B2', '8.94')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '8.05')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '19.7')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '12.34')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '1.4')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC33-U_Vertical.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC33-U_Vertical.FCStd")
print("created Crystal_HC33-U_Vertical")


 # Crystal_HC50_Vertical
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '11.05')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '10.2')
# H
App.ActiveDocument.Spreadsheet.set('B2', '4.65')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '3.8')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '13.36')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '4.9')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '1.2')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC50_Vertical.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC50_Vertical.FCStd")
print("created Crystal_HC50_Vertical")


 # Crystal_HC51-U_Vertical
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '19.3')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '18')
# H
App.ActiveDocument.Spreadsheet.set('B2', '8.9')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '7.6')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '19.7')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '12.35')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.8999999999999999')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC51-U_Vertical.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC51-U_Vertical.FCStd")
print("created Crystal_HC51-U_Vertical")


 # Crystal_HC52-U_Vertical
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '8')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '7')
# H
App.ActiveDocument.Spreadsheet.set('B2', '3.3')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '2.3')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '8.8')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '3.8')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.5')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC52-U_Vertical.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC52-U_Vertical.FCStd")
print("created Crystal_HC52-U_Vertical")


 # Crystal_HC52-8mm_Vertical
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '8')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '7')
# H
App.ActiveDocument.Spreadsheet.set('B2', '3.3')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '2.3')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '8')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '3.8')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.5')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC52-8mm_Vertical.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC52-8mm_Vertical.FCStd")
print("created Crystal_HC52-8mm_Vertical")


 # Crystal_HC52-6mm_Vertical
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '8')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '7')
# H
App.ActiveDocument.Spreadsheet.set('B2', '3.3')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '2.3')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '6')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '3.8')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.5')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC52-6mm_Vertical.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC52-6mm_Vertical.FCStd")
print("created Crystal_HC52-6mm_Vertical")
