#
# SCRIPT to generate 3D models
#



 # Crystal_HC49-U_Horizontal
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '13.0')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '12')
# H
App.ActiveDocument.Spreadsheet.set('B2', '10.9')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '10')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '4.65')
# iheight3d
App.ActiveDocument.Spreadsheet.set('C3', '4')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '4.9')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.5')
# pack_offset
App.ActiveDocument.Spreadsheet.set('B6', '2')
# pack_rm
App.ActiveDocument.Spreadsheet.set('B7', '4.9')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC49-U_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC49-U_Horizontal.FCStd")
print("created Crystal_HC49-U_Horizontal")


 # Crystal_HC49-U_Horizontal
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '13.0')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '12')
# H
App.ActiveDocument.Spreadsheet.set('B2', '10.9')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '10')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '4.65')
# iheight3d
App.ActiveDocument.Spreadsheet.set('C3', '4')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '4.9')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.5')
# pack_offset
App.ActiveDocument.Spreadsheet.set('B6', '2')
# pack_rm
App.ActiveDocument.Spreadsheet.set('B7', '4.9')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC49-U_Horizontal_1EP_style1.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC49-U_Horizontal_1EP_style1.FCStd")
print("created Crystal_HC49-U_Horizontal_1EP_style1")


 # Crystal_HC49-U_Horizontal
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '13.0')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '12')
# H
App.ActiveDocument.Spreadsheet.set('B2', '10.9')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '10')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '4.65')
# iheight3d
App.ActiveDocument.Spreadsheet.set('C3', '4')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '4.9')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.5')
# pack_offset
App.ActiveDocument.Spreadsheet.set('B6', '2')
# pack_rm
App.ActiveDocument.Spreadsheet.set('B7', '4.9')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC49-U_Horizontal_1EP_style2.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC49-U_Horizontal_1EP_style2.FCStd")
print("created Crystal_HC49-U_Horizontal_1EP_style2")


 # Crystal_HC18-U_Horizontal
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '13.0')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '12')
# H
App.ActiveDocument.Spreadsheet.set('B2', '10.9')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '10')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '4.65')
# iheight3d
App.ActiveDocument.Spreadsheet.set('C3', '4')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '4.9')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.5')
# pack_offset
App.ActiveDocument.Spreadsheet.set('B6', '2')
# pack_rm
App.ActiveDocument.Spreadsheet.set('B7', '4.9')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC18-U_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC18-U_Horizontal.FCStd")
print("created Crystal_HC18-U_Horizontal")


 # Crystal_HC18-U_Horizontal
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '13.0')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '12')
# H
App.ActiveDocument.Spreadsheet.set('B2', '10.9')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '10')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '4.65')
# iheight3d
App.ActiveDocument.Spreadsheet.set('C3', '4')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '4.9')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.5')
# pack_offset
App.ActiveDocument.Spreadsheet.set('B6', '2')
# pack_rm
App.ActiveDocument.Spreadsheet.set('B7', '4.9')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC18-U_Horizontal_1EP_style1.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC18-U_Horizontal_1EP_style1.FCStd")
print("created Crystal_HC18-U_Horizontal_1EP_style1")


 # Crystal_HC18-U_Horizontal
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '13.0')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '12')
# H
App.ActiveDocument.Spreadsheet.set('B2', '10.9')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '10')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '4.65')
# iheight3d
App.ActiveDocument.Spreadsheet.set('C3', '4')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '4.9')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.5')
# pack_offset
App.ActiveDocument.Spreadsheet.set('B6', '2')
# pack_rm
App.ActiveDocument.Spreadsheet.set('B7', '4.9')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC18-U_Horizontal_1EP_style2.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC18-U_Horizontal_1EP_style2.FCStd")
print("created Crystal_HC18-U_Horizontal_1EP_style2")


 # Crystal_HC33-U_Horizontal
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '19.7')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '18')
# H
App.ActiveDocument.Spreadsheet.set('B2', '19.23')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '18')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '8.94')
# iheight3d
App.ActiveDocument.Spreadsheet.set('C3', '8.05')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '12.34')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '1.4')
# pack_offset
App.ActiveDocument.Spreadsheet.set('B6', '2.5')
# pack_rm
App.ActiveDocument.Spreadsheet.set('B7', '12.34')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC33-U_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC33-U_Horizontal.FCStd")
print("created Crystal_HC33-U_Horizontal")


 # Crystal_HC33-U_Horizontal
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '19.7')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '18')
# H
App.ActiveDocument.Spreadsheet.set('B2', '19.23')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '18')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '8.94')
# iheight3d
App.ActiveDocument.Spreadsheet.set('C3', '8.05')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '12.34')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '1.4')
# pack_offset
App.ActiveDocument.Spreadsheet.set('B6', '2.5')
# pack_rm
App.ActiveDocument.Spreadsheet.set('B7', '12.34')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC33-U_Horizontal_1EP_style1.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC33-U_Horizontal_1EP_style1.FCStd")
print("created Crystal_HC33-U_Horizontal_1EP_style1")


 # Crystal_HC33-U_Horizontal
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '19.7')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '18')
# H
App.ActiveDocument.Spreadsheet.set('B2', '19.23')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '18')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '8.94')
# iheight3d
App.ActiveDocument.Spreadsheet.set('C3', '8.05')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '12.34')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '1.4')
# pack_offset
App.ActiveDocument.Spreadsheet.set('B6', '2.5')
# pack_rm
App.ActiveDocument.Spreadsheet.set('B7', '12.34')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC33-U_Horizontal_1EP_style2.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC33-U_Horizontal_1EP_style2.FCStd")
print("created Crystal_HC33-U_Horizontal_1EP_style2")


 # Crystal_HC50_Horizontal
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '13.36')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '12')
# H
App.ActiveDocument.Spreadsheet.set('B2', '11.05')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '10')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '4.65')
# iheight3d
App.ActiveDocument.Spreadsheet.set('C3', '3.8')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '4.9')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '1.2')
# pack_offset
App.ActiveDocument.Spreadsheet.set('B6', '2.5')
# pack_rm
App.ActiveDocument.Spreadsheet.set('B7', '4.9')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC50_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC50_Horizontal.FCStd")
print("created Crystal_HC50_Horizontal")


 # Crystal_HC50_Horizontal
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '13.36')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '12')
# H
App.ActiveDocument.Spreadsheet.set('B2', '11.05')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '10')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '4.65')
# iheight3d
App.ActiveDocument.Spreadsheet.set('C3', '3.8')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '4.9')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '1.2')
# pack_offset
App.ActiveDocument.Spreadsheet.set('B6', '2.5')
# pack_rm
App.ActiveDocument.Spreadsheet.set('B7', '4.9')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC50_Horizontal_1EP_style1.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC50_Horizontal_1EP_style1.FCStd")
print("created Crystal_HC50_Horizontal_1EP_style1")


 # Crystal_HC50_Horizontal
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '13.36')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '12')
# H
App.ActiveDocument.Spreadsheet.set('B2', '11.05')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '10')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '4.65')
# iheight3d
App.ActiveDocument.Spreadsheet.set('C3', '3.8')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '4.9')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '1.2')
# pack_offset
App.ActiveDocument.Spreadsheet.set('B6', '2.5')
# pack_rm
App.ActiveDocument.Spreadsheet.set('B7', '4.9')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC50_Horizontal_1EP_style2.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC50_Horizontal_1EP_style2.FCStd")
print("created Crystal_HC50_Horizontal_1EP_style2")


 # Crystal_HC51_Horizontal
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '19.7')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '18')
# H
App.ActiveDocument.Spreadsheet.set('B2', '19.3')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '18')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '8.9')
# iheight3d
App.ActiveDocument.Spreadsheet.set('C3', '7.6')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '12.35')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.8999999999999999')
# pack_offset
App.ActiveDocument.Spreadsheet.set('B6', '2.5')
# pack_rm
App.ActiveDocument.Spreadsheet.set('B7', '12.35')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC51_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC51_Horizontal.FCStd")
print("created Crystal_HC51_Horizontal")


 # Crystal_HC51_Horizontal
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '19.7')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '18')
# H
App.ActiveDocument.Spreadsheet.set('B2', '19.3')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '18')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '8.9')
# iheight3d
App.ActiveDocument.Spreadsheet.set('C3', '7.6')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '12.35')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.8999999999999999')
# pack_offset
App.ActiveDocument.Spreadsheet.set('B6', '2.5')
# pack_rm
App.ActiveDocument.Spreadsheet.set('B7', '12.35')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC51_Horizontal_1EP_style1.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC51_Horizontal_1EP_style1.FCStd")
print("created Crystal_HC51_Horizontal_1EP_style1")


 # Crystal_HC51_Horizontal
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '19.7')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '18')
# H
App.ActiveDocument.Spreadsheet.set('B2', '19.3')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '18')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '8.9')
# iheight3d
App.ActiveDocument.Spreadsheet.set('C3', '7.6')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '12.35')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.8999999999999999')
# pack_offset
App.ActiveDocument.Spreadsheet.set('B6', '2.5')
# pack_rm
App.ActiveDocument.Spreadsheet.set('B7', '12.35')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC51_Horizontal_1EP_style2.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC51_Horizontal_1EP_style2.FCStd")
print("created Crystal_HC51_Horizontal_1EP_style2")


 # Crystal_HC52-U_Horizontal
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '8.8')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '8')
# H
App.ActiveDocument.Spreadsheet.set('B2', '8')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '7')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '3.3')
# iheight3d
App.ActiveDocument.Spreadsheet.set('C3', '2.3')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '3.8')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.5')
# pack_offset
App.ActiveDocument.Spreadsheet.set('B6', '1.5')
# pack_rm
App.ActiveDocument.Spreadsheet.set('B7', '3.8')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC52-U_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC52-U_Horizontal.FCStd")
print("created Crystal_HC52-U_Horizontal")


 # Crystal_HC52-U_Horizontal
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '8.8')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '8')
# H
App.ActiveDocument.Spreadsheet.set('B2', '8')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '7')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '3.3')
# iheight3d
App.ActiveDocument.Spreadsheet.set('C3', '2.3')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '3.8')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.5')
# pack_offset
App.ActiveDocument.Spreadsheet.set('B6', '1.5')
# pack_rm
App.ActiveDocument.Spreadsheet.set('B7', '3.8')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC52-U_Horizontal_1EP_style1.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC52-U_Horizontal_1EP_style1.FCStd")
print("created Crystal_HC52-U_Horizontal_1EP_style1")


 # Crystal_HC52-U_Horizontal
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '8.8')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '8')
# H
App.ActiveDocument.Spreadsheet.set('B2', '8')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '7')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '3.3')
# iheight3d
App.ActiveDocument.Spreadsheet.set('C3', '2.3')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '3.8')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.5')
# pack_offset
App.ActiveDocument.Spreadsheet.set('B6', '1.5')
# pack_rm
App.ActiveDocument.Spreadsheet.set('B7', '3.8')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC52-U_Horizontal_1EP_style2.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC52-U_Horizontal_1EP_style2.FCStd")
print("created Crystal_HC52-U_Horizontal_1EP_style2")


 # Crystal_HC52-8mm_Horizontal
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
App.ActiveDocument.Spreadsheet.set('B2', '8')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '7')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '3.3')
# iheight3d
App.ActiveDocument.Spreadsheet.set('C3', '2.3')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '3.8')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.5')
# pack_offset
App.ActiveDocument.Spreadsheet.set('B6', '1.5')
# pack_rm
App.ActiveDocument.Spreadsheet.set('B7', '3.8')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC52-8mm_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC52-8mm_Horizontal.FCStd")
print("created Crystal_HC52-8mm_Horizontal")


 # Crystal_HC52-8mm_Horizontal
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
App.ActiveDocument.Spreadsheet.set('B2', '8')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '7')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '3.3')
# iheight3d
App.ActiveDocument.Spreadsheet.set('C3', '2.3')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '3.8')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.5')
# pack_offset
App.ActiveDocument.Spreadsheet.set('B6', '1.5')
# pack_rm
App.ActiveDocument.Spreadsheet.set('B7', '3.8')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC52-8mm_Horizontal_1EP_style1.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC52-8mm_Horizontal_1EP_style1.FCStd")
print("created Crystal_HC52-8mm_Horizontal_1EP_style1")


 # Crystal_HC52-8mm_Horizontal
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
App.ActiveDocument.Spreadsheet.set('B2', '8')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '7')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '3.3')
# iheight3d
App.ActiveDocument.Spreadsheet.set('C3', '2.3')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '3.8')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.5')
# pack_offset
App.ActiveDocument.Spreadsheet.set('B6', '1.5')
# pack_rm
App.ActiveDocument.Spreadsheet.set('B7', '3.8')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC52-8mm_Horizontal_1EP_style2.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC52-8mm_Horizontal_1EP_style2.FCStd")
print("created Crystal_HC52-8mm_Horizontal_1EP_style2")


 # Crystal_HC52-6mm_Horizontal
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '6')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '5')
# H
App.ActiveDocument.Spreadsheet.set('B2', '8')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '7')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '3.3')
# iheight3d
App.ActiveDocument.Spreadsheet.set('C3', '2.3')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '3.8')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.5')
# pack_offset
App.ActiveDocument.Spreadsheet.set('B6', '1.5')
# pack_rm
App.ActiveDocument.Spreadsheet.set('B7', '3.8')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC52-6mm_Horizontal.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC52-6mm_Horizontal.FCStd")
print("created Crystal_HC52-6mm_Horizontal")


 # Crystal_HC52-6mm_Horizontal
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '6')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '5')
# H
App.ActiveDocument.Spreadsheet.set('B2', '8')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '7')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '3.3')
# iheight3d
App.ActiveDocument.Spreadsheet.set('C3', '2.3')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '3.8')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.5')
# pack_offset
App.ActiveDocument.Spreadsheet.set('B6', '1.5')
# pack_rm
App.ActiveDocument.Spreadsheet.set('B7', '3.8')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC52-6mm_Horizontal_1EP_style1.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC52-6mm_Horizontal_1EP_style1.FCStd")
print("created Crystal_HC52-6mm_Horizontal_1EP_style1")


 # Crystal_HC52-6mm_Horizontal
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.02')
App.ActiveDocument.recompute()
# W
App.ActiveDocument.Spreadsheet.set('B1', '6')
# Wi
App.ActiveDocument.Spreadsheet.set('C1', '5')
# H
App.ActiveDocument.Spreadsheet.set('B2', '8')
# Hi
App.ActiveDocument.Spreadsheet.set('C2', '7')
# height3d
App.ActiveDocument.Spreadsheet.set('B3', '3.3')
# iheight3d
App.ActiveDocument.Spreadsheet.set('C3', '2.3')
# RM
App.ActiveDocument.Spreadsheet.set('B4', '3.8')
# d_wire
App.ActiveDocument.Spreadsheet.set('B5', '0.5')
# pack_offset
App.ActiveDocument.Spreadsheet.set('B6', '1.5')
# pack_rm
App.ActiveDocument.Spreadsheet.set('B7', '3.8')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC52-6mm_Horizontal_1EP_style2.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC52-6mm_Horizontal_1EP_style2.FCStd")
print("created Crystal_HC52-6mm_Horizontal_1EP_style2")
