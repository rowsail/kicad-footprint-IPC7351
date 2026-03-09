#
# SCRIPT to generate 3D models
#



 # D_DO-35_SOD27_P2.54mm_Vertical_AnodeUp
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '4')
# d
App.ActiveDocument.Spreadsheet.set('B2', '2')
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

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"D_DO-35_SOD27_P2.54mm_Vertical_AnodeUp.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"D_DO-35_SOD27_P2.54mm_Vertical_AnodeUp.FCStd")
print("created D_DO-35_SOD27_P2.54mm_Vertical_AnodeUp")


 # D_DO-35_SOD27_P3.81mm_Vertical_AnodeUp
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '4')
# d
App.ActiveDocument.Spreadsheet.set('B2', '2')
# d2
App.ActiveDocument.Spreadsheet.set('C2', '0')
# RM
App.ActiveDocument.Spreadsheet.set('B3', '3.81')
# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.5')
App.ActiveDocument.recompute()
doc = FreeCAD.activeDocument()
__objs__=[]
for obj in doc.Objects:	
    if obj.ViewObject.Visibility:
        __objs__.append(obj)

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"D_DO-35_SOD27_P3.81mm_Vertical_AnodeUp.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"D_DO-35_SOD27_P3.81mm_Vertical_AnodeUp.FCStd")
print("created D_DO-35_SOD27_P3.81mm_Vertical_AnodeUp")


 # D_DO-35_SOD27_P5.08mm_Vertical_AnodeUp
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '4')
# d
App.ActiveDocument.Spreadsheet.set('B2', '2')
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

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"D_DO-35_SOD27_P5.08mm_Vertical_AnodeUp.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"D_DO-35_SOD27_P5.08mm_Vertical_AnodeUp.FCStd")
print("created D_DO-35_SOD27_P5.08mm_Vertical_AnodeUp")


 # D_T-1_P2.54mm_Vertical_AnodeUp
import FreeCAD
import os
import os.path

# d_wire
App.ActiveDocument.Spreadsheet.set('B4', '0.02')
App.ActiveDocument.recompute()
# L
App.ActiveDocument.Spreadsheet.set('B1', '3.2')
# d
App.ActiveDocument.Spreadsheet.set('B2', '2.6')
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

FreeCADGui.export(__objs__,os.path.split(doc.FileName)[0]+os.sep+"D_T-1_P2.54mm_Vertical_AnodeUp.wrl")
doc.saveCopy(os.path.split(doc.FileName)[0]+os.sep+"D_T-1_P2.54mm_Vertical_AnodeUp.FCStd")
print("created D_T-1_P2.54mm_Vertical_AnodeUp")
