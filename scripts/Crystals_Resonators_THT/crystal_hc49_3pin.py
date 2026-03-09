#
# SCRIPT to generate 3D models
#



 # Crystal_HC49-U-3pin_Vertical
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

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC49-U-3pin_Vertical.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC49-U-3pin_Vertical.FCStd")
print("created Crystal_HC49-U-3pin_Vertical")


 # Crystal_HC52-U-3pin_Vertical
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

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC52-U-3pin_Vertical.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"Crystal_HC52-U-3pin_Vertical.FCStd")
print("created Crystal_HC52-U-3pin_Vertical")
