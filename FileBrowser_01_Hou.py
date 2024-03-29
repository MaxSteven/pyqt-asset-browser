'''
 
        This was Generated by PyQt-Ui Generator (V0.5) Advanced Framework Variant
        Created for easy access to UI code for DCC apps (Houdini, Maya)
        Initial UI should boot if all paramemters are met.
        PyQt-UI Generator is coded by Bilal Malik (Sideswipe)

'''
import os, sys, hou, base64, re

#Checks Houdini Enviroment for the variable PYUI and loads the path from it.
sys.path.insert(0, (hou.getenv('PYUI')))

locPath = os.path.join("PATH_HERE")
dirS = ["DIRS",
        "01-Indoors",
        "02-Runways",
        "03-Multi",
        "04-Poses",
        "05-Objects",
        "06-Cloths",
        "07-Rocks",
        "08-Complex",
        "09-ObserverDoel",]

imgs = []
#Qt Import Block 
from Qt import QtCore, QtWidgets, QtCompat ,QtGui

#Class Creation
class DBrowse(QtWidgets.QMainWindow):
        def __init__(self, parent=None):
                super(DBrowse, self).__init__(parent)
                #File Interface File goes here
                file_interface = os.path.join("PATH_HERE")
                self.mw = QtCompat.loadUi(file_interface)
                self.setCentralWidget(self.mw)
                #Set Window Title Here
                self.setWindowTitle("Asset Browser")

                stylesheet = hou.qt.styleSheet()
                self.setStyleSheet(stylesheet)
                
                #vars
                global imgs
                imgs = []
                
                #label
                h64 = "iVBORw0KGgoAAAANSUhEUgAAAWkAAACXCAYAAADXlKqTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAIk2lUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMxNDIgNzkuMTYwOTI0LCAyMDE3LzA3LzEzLTAxOjA2OjM5ICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0RXZ0PSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VFdmVudCMiIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bWxuczpwaG90b3Nob3A9Imh0dHA6Ly9ucy5hZG9iZS5jb20vcGhvdG9zaG9wLzEuMC8iIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTggKFdpbmRvd3MpIiB4bXA6Q3JlYXRlRGF0ZT0iMjAyMC0wNS0wOFQwMToxOTo1MSswMTowMCIgeG1wOk1ldGFkYXRhRGF0ZT0iMjAyMC0wNS0wOFQwMToyMTo0NiswMTowMCIgeG1wOk1vZGlmeURhdGU9IjIwMjAtMDUtMDhUMDE6MjE6NDYrMDE6MDAiIGRjOmZvcm1hdD0iaW1hZ2UvcG5nIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOmNhMjhhZWUyLWFiMjItNjY0Ny1hMGJlLTQ0Mjk1MzRkYTgxMSIgeG1wTU06RG9jdW1lbnRJRD0iYWRvYmU6ZG9jaWQ6cGhvdG9zaG9wOmM4ZDEwNGM5LThjYTUtMzE0Zi1hNmEzLTgyZmIxNzU1OTZkYyIgeG1wTU06T3JpZ2luYWxEb2N1bWVudElEPSJ4bXAuZGlkOmNkYjNmZGZjLThlYmEtOWM0NC04MWZiLTc4ZjYzMzYzODU2NSIgcGhvdG9zaG9wOkNvbG9yTW9kZT0iMyI+IDx4bXBNTTpIaXN0b3J5PiA8cmRmOlNlcT4gPHJkZjpsaSBzdEV2dDphY3Rpb249ImNyZWF0ZWQiIHN0RXZ0Omluc3RhbmNlSUQ9InhtcC5paWQ6Y2RiM2ZkZmMtOGViYS05YzQ0LTgxZmItNzhmNjMzNjM4NTY1IiBzdEV2dDp3aGVuPSIyMDIwLTA1LTA4VDAxOjE5OjUxKzAxOjAwIiBzdEV2dDpzb2Z0d2FyZUFnZW50PSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxOCAoV2luZG93cykiLz4gPHJkZjpsaSBzdEV2dDphY3Rpb249InNhdmVkIiBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOmFlNTRkNTMwLTg2MjItMjY0Zi05NThmLTE0YzIwNGQzMzU3MiIgc3RFdnQ6d2hlbj0iMjAyMC0wNS0wOFQwMToyMTo0NiswMTowMCIgc3RFdnQ6c29mdHdhcmVBZ2VudD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTggKFdpbmRvd3MpIiBzdEV2dDpjaGFuZ2VkPSIvIi8+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJjb252ZXJ0ZWQiIHN0RXZ0OnBhcmFtZXRlcnM9ImZyb20gYXBwbGljYXRpb24vdm5kLmFkb2JlLnBob3Rvc2hvcCB0byBpbWFnZS9wbmciLz4gPHJkZjpsaSBzdEV2dDphY3Rpb249ImRlcml2ZWQiIHN0RXZ0OnBhcmFtZXRlcnM9ImNvbnZlcnRlZCBmcm9tIGFwcGxpY2F0aW9uL3ZuZC5hZG9iZS5waG90b3Nob3AgdG8gaW1hZ2UvcG5nIi8+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJzYXZlZCIgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDpjYTI4YWVl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"
                pixmap = QtGui.QPixmap()
                header = base64.b64decode(h64)
                pixmap.loadFromData(header)
                self.mw.label.setPixmap(pixmap)
                
                #Table View
                header = self.mw.tableWidget.horizontalHeader()
                header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
                #header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
                
                #clicked
                self.mw.tableWidget.doubleClicked.connect(self.clickedF)
                
                
                #Button
                self.mw.pushButton.clicked.connect(lambda: self.tableFill(1))
                self.mw.pushButton_2.clicked.connect(lambda: self.tableFill(2))
                self.mw.pushButton_3.clicked.connect(lambda: self.tableFill(3))
                self.mw.pushButton_4.clicked.connect(lambda: self.tableFill(4))
                self.mw.pushButton_5.clicked.connect(lambda: self.tableFill(5))
                self.mw.pushButton_6.clicked.connect(lambda: self.tableFill(6))
                self.mw.pushButton_7.clicked.connect(lambda: self.tableFill(7))
                self.mw.pushButton_8.clicked.connect(lambda: self.tableFill(8))
                self.mw.pushButton_9.clicked.connect(lambda: self.tableFill(9))
                
              
        
        def clickedF(self,mi):
            #print("clicked")
            #column = mi.column()
            row = mi.row()
            item = imgs[row][0]
            
            pre, ext = os.path.splitext(item)
            item = (pre + '.obj')
            nameitem = re.sub("[\W_]","_", imgs[row][1])
            
            OBJ = hou.node('/obj/')
            geometry = OBJ.createNode('geo', run_init_scripts = False)
            geometry.setName(('GI_'+ nameitem),unique_name=True)
            geometry.setUserData('nodeshape', "bulge_down")
            geometry.setColor(hou.Color((1,0,0)))
            geometry.moveToGoodPosition()
            
            fileSop = geometry.createNode('file', run_init_scripts = True)
            fileSop.setName(nameitem,unique_name=True)
            fileSop.parm('file').set(item)
            fileSop.moveToGoodPosition()
            
                        
            print(item)
            
            
            
        def tableFill(self,index):
            self.mw.tableWidget.setRowCount(0)
            global imgs
            imgs = []
            path = locPath + dirS[index]
            valid_images = [".jpg",".gif",".png",".tga"]
            for f in os.listdir(path):
                ext = os.path.splitext(f)[1]
                name = os.path.splitext(f)[0]
                if ext.lower() not in valid_images:
                    continue
                tup = ((os.path.join(path,f)),name)
                imgs.append(tup)
                
            
            for i in range(len(imgs)):
                rowPosition = self.mw.tableWidget.rowCount()
                self.mw.tableWidget.insertRow(rowPosition)
                pixa, textl = imgs[i]
                pixl =  QtGui.QPixmap(pixa)
                item = QtWidgets.QTableWidgetItem(pixl,"")
                self.mw.tableWidget.setItem(rowPosition , 0, item)
                self.mw.tableWidget.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(textl))  
                

                

isPanel = False
#Create the UI Block
if isPanel == True:
    #Create Interface Python Panel
    def onCreateInterface():
        my_window = DBrowse()
        my_window.show()
        return my_window
elif isPanel == False:
    #Create Interface Shelf.
    try:
        my_window.close()
    except:
        pass
    my_window = DBrowse()
    my_window.resize(640,480)
    my_window.show() 

