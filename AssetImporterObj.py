import os, sys, hou, base64, re

#Checks Houdini Enviroment for the variable PYUI and loads the path from it.
sys.path.insert(0, (hou.getenv('PYUI')))

#Qt Import Block 
from Qt import QtCore, QtWidgets, QtCompat , QtGui 

#Root Assets Location
locPath = os.path.join("PATH_TO_ASSET_ROOT_HERE")

#Global Vars
dirLst = [] # Stores the Directories to search
imgs = [] #Stores items from Dirs to load into table for assets

#Class Creation
class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
                super(MyWindow, self).__init__(parent, QtCore.Qt.WindowStaysOnTopHint)
                #File Interface File goes here
                file_interface = os.path.join("PATH_TO_UI_FILE_HERE")
                self.mw = QtCompat.loadUi(file_interface)
                self.setCentralWidget(self.mw)
                #Set Window Title Here
                self.setWindowTitle("Asset Browser")
                stylesheet = hou.qt.styleSheet()
                self.setStyleSheet(stylesheet)
                #Set Windows Flags
                #self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
                #self.setWindowFlag(QtCore.Qt.MSWindowsFixedSizeDialogHint, True)
                #self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, False)
                
                #Vars
                
                
                #PIXMAPS
                h64 = "iVBORw0KGgoAAAANSUhEUgAAAoAAAABkCAYAAAAWh4GeAAAfAUlEQVR4nO2da2xd2VXH1/ErTpzYTjJ0EB05hgqVFqR4KKBSaMdTAS2iUsyHthSB4hGifGM8FPF1PN8AIerpBx5VIQ7QCvFQPRUqgkqMQ6GiUqEeEG3VaVW7KtNWmiR2Ej8SPw5aN//l2Tm5j/PY55597v3/pKPre33O3vvs1/mftfdeO5IKiOO4imgJyczY2NgHRORREdG2ckpETjqfJxDekXPE8vBn8iCEPEzkHOL8PYAj+fcg2tqeiGw7n4cicn17e/sK85iEQBRVIrU6QgFISBvGxsYE7eSEI/z0x9MiMiEiZ0Rk3Pk8hUPPGcVDagiHPbwED6kjfB463wnpdQYTh7WL2HmROnCOXRG5A4Gnn1sichvHLRy3cd4Ozru3vb3NikSCIFQBOBRAGggJnRgPlb0U6RyESDRxaGLRfjuP7ycca+IozhtuY0lsZU3k2xSpiqSlrpXFLkq8/Ow5gs0sd3ch7K5D5O3gcxvnborIPl+SCPEHBSAhfjnEg+tOh1CHIADNojgJwegerkXxFESjWRMHnQdr3MKiSHFIfDDQxGI36LyAWL3bx7EHAbcDAeda7MyCd8s5Z491lZDuQwFISDUcOA/FdgwmhptPO4JQReNZCMgTifmJZ5w5UnHCgkiLYv+StNYlLXZJq51+3oO17jYE2y5+UxF3A5+7zouPDcvu0WJHSLhQABISNoewmGx1SOUIhpJPwnI4AWFoonEcx2lHKA7jcC2KkWPRSVoUST2ImljrrHyTFrsDDL/uOMOut5z5dTYEu4X/7ULYsT4QUnMoAAnpDe45VpnvtrmjYYjCCYjBM00siqccMWnH6YSAiFvMU+TQc3kMOKKumaXO/j6AmLN5drsQebdbWOxM7N2hxY6Q/oECkJD+Yh8i4Eabu7ZVz65FcdIZWnZXPZtFcRTHuDNkWIijoyP1GNAQk1EURQMDAw0PAkdHR43fBgYG9OfGb+4qO/f74eFhy+uVwcHBqNlvbliaBo1LkCYNx/73QKYhTg0ruo+PihVD1J3G921nGHY3sRL2lmPFs3l3tnjpno/EEEJ6B7qBIaQNcANDWjPqDDHrCudpEXmriHwPBMpBnn5G+4iRkZFoaGioobYODw+P9vb2jlSIjY2NDaq42tnZOTw4OJChoSETao1rVaBBPMqpU6cGVNDptXfv3j0aGhqKTpw4MaDhqFDb3d3VMEV/MzGp51pYGraei2s1LLl3717D+qkST8PTcNz4Nd37+/smBItUnRhCXIf3vyIi/yki3xaRmxB32xD0pAl0A0NCgX4AHTY2NqqItnKmpqb68r7rDAVgLh4REXWg/ZMQKplFoIqpkydPDgwPDzcE4L179xoC8Ny5c8OqttSyNzo6Onjz5s390dHRARVoEGZy9uzZ4e3t7QP9//DwcKTXqsDb3Nw8GBkZGRgbGxvY2dk50vA1TL1GheLt27eP9FPD1nP185FHHhkeHx8fWl9f31Uh+LrXvW74zp07R5ubm/uPPvroyMHBQSNOFZxbW1sHGt/U1NTojRs3DjRtKhBz5mEMy6p+rojIpznvLhsUgCQU6AewO+j8mMdF5G0i8iMi8gYReQyWiUn8/xA+pV4VkXUR+ZqIfFlEPi8iX2QnS0hhtG19FNapn8KwZKZ2pR2mWue2t7ePr5uYmGj0V6+++uq+/n98fFwtdJFZ32zoV4WbCjH9n4owFYbj4+ODZ86cGdS/Vfzp77u7uwMq7lS8bW9vH21tbe3v7OyoyBtRK969e/eOLYJqddza2jq8devWof59eHg4rJbFmzdvHkxOTg6pKFWL36lTp4bu3LlzqOmwtOXo/E386b1/QkReZJUkhPimFwSgDj3Nich7ReQd+N6OQQhCPd4oIu9yztU5NP8qIn+Lt+5b1dwSIbVHFx38OVYiPw5LYOq5HyqcRkdHo5MnTzb6qDt37hyo4LK5evr3rVu3DvQ8tdLp8Ozw8LDO1dP/6fWRCkEVdyrE9vf345GRkYYYU3GnglDFmlrwNEy1Bh4dHQ2pNVEFnx6nT5/WvkLU2jc2NjakwlFFoMY9PT194uWXX97VcC29aiHUsNV6qNeqBXJnZ+cgyqYAYwz5atx/T/FHCCmLgRrn7FvwdvwdEbkqIu9JIf46MY5wriLcvxaRny7/VgjpSXThwcdF5BWsLM6Ezu/ToV09Dg4OGiIK8+wawk6Hh3VIV4Xe3t5efPfu3canfjfLm4o7m4tnizfkvoAc0KHh27dvH7i/q3VPrYQa/qlTpwZV4KklUkUfrIoab3Tjxo19FY3uYhMVjyo2NVx8j3LMd7adZP5NRP6RzYIQUhZ1FIA6r+hfROQLmGd0sqR4NNz3i8hnYRWkECQkO9+BJfCWM6etI7YgQ0WdHrboQ8WXijT9PHfuXMNiZ6t41Zqngk1FmP6tou3MmTND+l2tffo/PVcFnloPVfzpdRBtsQ4LX79+fX9iYmJQLXgWJ9LRGAY+f/68zkGUV1555a5+V0uifte49BoViyoe9VPnHZ48eXLQXWHcgQgW0/8Rkb+kSxZCSJnUSQBOweL37yLyZJfjfjtE4CeQDkJIenQF699B4IykEYGq1FRUqYg6ceJEw/qmIkwF2cjIyKD+rsO0+t0sdirY9NDf9/f3j2zYWEWiriK+ffu2nntk4hBuZCIVa7ZQRK/V+YAajp5v4k7jUQGph84D1GtVMGpa9XoN0+YX6hC0WgDt+gyMwVr6Vyn3nSaEkNzUZRXwZRH5iIchXh/oXKbfFJHlrGFxFXD94Cpgr7xPRH4h7U4S5oMPbvyOh3RteNfEmSv+xPHDZ9fj79h8/mG+3nE8er3cHxZ2/QQ2AnN9/iV9EpqrGTfJrv8/FYHmqzAFJ7FY5o9E5H/DK7r6wVXAJBS4Cjgf6l/sYxiKDQV1gHtFRH5eRH4txab/hJD7fEpEHsU0jq1OlkCIugd6TnPInPgt+T2S1zpdO//4t2RnnHTs3CyOZFpMhCbCeuCL61C6DebrT5A/FH+EkK4Q8hDw92H+XUjiz+V9SN/rw0kSIUGzh2kUX8NwJ7n/Eq4C8DMi8k/MD0JItwhVAP4Q/PLNBJCWdmj6/kNE3hxuEgkJiuuY47YJC38/bwtkW7z9N+ZIEkJIVzug0HgD3oYfq0k1eAyrkn8wgLQQUge+CvcwR7AE9qMI1OHhCZ0SLSJ/wb16CSHdJjQBqPOD/rlG4s94FCLwe8NIDiHB83nMpd3C1nGnenBnoiS2CvoMxN+XRORPROS7YSWTENIPhNThDmMHjh8IIC15UNH6NyLyM3ybJyQV12ANfDemUTwCYXSIbeRa+cEL1WLYatHHoOP+Rr0IfENEPoddPu52OY2EENIgJAH4+/C3V2c0/b8nIs/U/D4I6RbfhiVQ9+p+k4hMi8hZCMETTdIQQVCFRtzEtU0EEbuNOY/X4RPx63xJJIRUTSh+AGcxhBqms5xs6IPgnSKymryKfgAJIYSQ/iJUP4AhzAEcFZGP9oj4E9zHR3FfhBBCCCHBEYIA/K0eXEGr9/OhANJBCCGEEPIQVQvAiR4WSh/C/RFCCCGEBEXVAlD31D0XWJ744izujxBCCCEkKKoUgLqS74M9Xh1+I9AVi4QQQgjpY6oUgO+qocPnrLwePs4IIYQQQoKhSgH4K31SDX41gDQQQgghhBxTlQDUeH+uT4rh3djlhBBCCCEkCKoSgD8qIuf7pAroSuC3BJAOQgghhJAGVQnAt/VZ9v9EAGkghBBCCGlQ1V7Ab+qz7O+3+21Lt7fFieN4UUTWoyha7mrEhBBCeoo4jnvmdqqyAL65onir4of77H5D41kRme/3TCCEEEKMqgTgVJ+VwOsDSEMozKhFLo7j1TiO1+IHWcPv+v+ZXrjZOI7n4zhej+N4JYDkNNC8RR5TFJPUxHE8i3ozzVwjpP5UNQTcq7t/tGI8zGR1FRUbOhR7IRHpNefvJ5zPZ+M43tBraj50a/d8QQVXIPeiabok9x/qK1EUbVafJFIDZmFNX9UpFSwwQupNVRbAfhNE41NT/Wb0PEYteWsicgVC6AUReUq3yovuM+scOjnw+/H/F3D+FVgG62oRXG3xdyXEcTxp4g/QCkgIIX1IVRbAyqhIiI3os9dzmN1dSZGPeQg/gaBbwGKMloFFUaSWBbWSLWOoaQmCRYeGF+pmDYyiSIeAVfit4t6qxgTfVRG5jO9LAaSLdECHYEXkRRF5LoqiReYXqTPx/dUU19QAwIKshqosgLeqvnFSOq74U4veXNZhIxVMURTN4foJWANrZ7FS0RqI+BNHAC5i+P1ir8y3JIQQkp6qBOANllFPM+uIv8dh0csNrH5P4folCpZ8IN8u4q173SkXDgMTQkifUZUA/CYrWs8y6QiLpzD/rzCOCJwoKij7GBN6ln+6MnmLApAQQvqPqgTgl1jXepYFZ7GHV6EGEfgChi05Byo78xB8DZc0WP2rf0/EcTxXs3shhBBSgKoE4JdZaD3JJARgmVYlEzELWNFKUgCBp9bTpNsXDgMTQkgfUpUA/BwrW08yD5Ghq0pL8S0H8bKEeGi1Sk9y+LdBFEW6Qln9LV6ioCaEkP6hKjcw/yUi10XkPOtaT9FUZJTAMhzSLviIC+5mdOFKcocDFUdrdXeU7Pj+24DgS7LsbJdXiksYuDCZgZXYZR157GWuqBPfDOJLlukm4ivFJ2OLeDfhBsjrPfYKyLPZRN3IXU5tyn4N5VBKe0Y7s3txWS/bDVSLPJRu9WFN2neldb5NOyyt7YPZRPmv03F6go2NDT0+sbGxEXf76CEksGMaWbvWKV0+cLaR62i1wnkPNXpnm7ZOLOfd/grbZ8VVzllU/4nt0uCWned4p5F3mynyeB3bjOW2Quq1CCNNmSoreHAVvc9J5HGneDfT3mOBbqo0n2pIe6Y4cH6ztpe2rFLlWYYyiLHdZOZ8anX/aOMrKeJd8znXFu1rKWX7KlTXLd8Sv1kZtop/BeetpkhfMzL3mb7bYSLs47488Uyb7NDPBTtfvUpH0B8XkQ9UGD/xi3Uu3drzdgUuTWazxom3w2VcL1hYspbYtWMSYc/BYfLlOI6fqum2dG0ts2qZiOP4JfMJ6OOtHZ3es/i6gTJq9iZseXzRrLp5HH6jTFecrQablanAKjCDOC9h6FvPnc9jJcFDdTkR72pi9btZZy459zjXwRJxrclvk8injTYWheCt1Ymy2oJT8mTdcMvJ8my2Wd2EqFrGtBBp055n0BZ0q8kXi7ZnCAit50/jp5cQ52qiHNw6/ski9c2J221fWy3q3XSTun4NcReySLVob8n4LY5W/ckTSHur/6dOY4ntsBNu3WtVl2n9c4EFcHBjY+NbtADmJjQL4BJuZLZLFsDUljWct4q/Z5w3tVSWPceCpmQaIq3aAoj7jTtZ92ANzXx/LcJaRlibaR13w5qxkieftRN3r0tpYUtaL9ZyWATms8Tb5B4zLbwJoC4VtgAm8iytZc+tTzOJ/y854S2lbM/zTrmnLgP3/pEuG4VYS5MnuM69JrO1G/G6FrW0FmV3tOOhfExxfas+dKXA6EjczDqcI5yutMMmFsCH6nKZz7wyqGoRiHIoIn9aYfzEL9ahdOttxwRNlofRjGMVeFK3aUvzJhxF0RIcWusb3tM1243E0tpJUJkVtdC9qViGxVStITNpLSyJXV8E+dxxuAwPn2O/k1EULaSxrOg52E5tFmm9mMWSjDpwBXXiyTTxOvf4DH66UuaQbWjgXt08W0yRZ1pOmtfPOQvMGkAIP50ogzTtednpN1KJxgST6Ee0zlyNomgmjRUJ57j1LauV2+J9Albgx9Pkobx2zzOwUE1ga83MDvWRhhWEoe1trspdjhLt8BcztkPra67kGJqfQV1s1D1Ygms3V7xKAah8RERuVpwG4peudAY5h0/MVD+b1eyPoSfrJFJZmQLBBF1bcYP8vOrBJ6BZp3INM+FBZQIpjRVwEWX6XJ7hPKdctSN/IqUlZ8Z56OSpS0vOPa70w+prRzjkzbNFCKcnYImZxTBe3vDWHFG5kPF2FiHgnoc4zRLvpiMCL2V8mVxCvPZylWmqhiOmXRGYte4tYZj1maqnwzRph5mmAiV2mFrOmBeuJ4oyF5WUStUCUAvuDypOA/FD6NuzPYHO85m8c9zwkHk+aYkIFcf339WUgrmQFRAPZYsv9zxCCCSdq3QhhRidRT+SuzwgVE0EpBEDx/lUoC4tYZ5SHgFSR+yBuVCgblgZzzvWs6bzAjOEl8dnqW2nmKvc0Bbt2lTD+Whbly29ReYPQgRey7Gr0jTS8ALqb9Uc+zAt0A6XnXaYdmrFHJ4nz9VZ/EkAAlD5QxF5OYB0kGJM4M20m2ygIaZlw0PHtYhOeK4GlptU1j8Db9BFfALaS4CPTtE6904vFhd8uLlwrBltLYCw2FyAyC264OlYdPa4FdCEw7WCViPL78sog+cKvmhsoq5O5BgOLTRVAi+TV/GSkyYsy7dFT65VzOp9KcM0BFtgUfkLC/LsIsSor3Y4n7IdXiz60hkKIQjAPRH5oJZpAGkhxej2HIisQ4yFJ8+726eF7Ig64fsvSwdZxAro+gArSuY5nh645qwkbYXVIR91ad0Zjutlp+YmHIqKpk3nJdPXA9jqWRYBeNXTvDcTdW3LHlbwC55eYBs4DvUlo6Dzde9FsfZXWIzmbIelbXbQTUIQgIK3sOcDSAfpXbY8zlkxkRTyQzuT9c/BHWbLSp6HaVNg5XgyZQfvy3q2gDib4jyIfT4ErXx6fTHIC57yzB66y56cG5u1OstCEC+urtxdeDqcam3R9+rvJccKmLYNdcvNV0tgsSyrHabt0+voDuwhQhGAyu+IyGcDSAfpTbw5OXYsaiHPe0y7+vcB0KEe+wTMGKflsRdhrA/IFMNd15DWXK4oEvF12iXA7svbQ7AmdckHvh6YVh+qFCI+LT/mWqXdC8Alzy+wDZzRDMnQZkOY81Z1O2znh7NWhCQA90XkfSLyjQDSQkgnbJFCcHO3INwaqwVzviHnsgIiLhNk3ZonZA/FbqymbTwcPMw5SvKS45S8V/ElHGo/7JagrdXcEYZlCa8sFuiXAtkWs5HWEtrhNWe6QjtqvfDDJSQBqHxHRH5WRL4VQFoIaYcJqxAtN7msfw5F5gEuYFjpw2mdMhcBVpFrEFC5fJtl4GKLHTqK0muiJkkowiFETAC2aidWn8vaUzfLEHgoZVhWO0xLz+zsUeVWcK34OkTgZ0TksQDTR4gE3gnknf/XQB/WcRxfxfZ3c1netHUYFVaLVTjpnceuHsslTh6fw73qivAvIu3LPjd9d4TldAk7cRQevg4cir/WWN60enExYViK1QltfasuUxCcqR5shx4IUQAqXxGRt4rIP/TB3BiSnxDqRlBDwDl8/7ViBe425rMKSYjAaVggL8Nh77PYb7ixJ7BPcWbOdeEaYtHZu3kDD06Ls0h+WDlfcPZgJaQQaCtScT+yltGdVpWYSGM79ECoAlD5PxF5u4j8GeYGkrDZqqATmah4KEAgQitfGedQyPpnqNUPloHGCsGs4gnnz2Mu4LzjPPUixKCg7EycFR7iwnDwMkSwHZdxCAToKuLLmz9Xe2UFICE1hu3QAyELQOWOiLxfRD6NbePGA0gTaU6d3iJ7kgK+/1qxbMO4eecTOv7GbD7gLETzLOpLo85AnOl5Kx6cOq+YAMbQ7awT79PYZ3gL5yxmHJpe92m9JITkgu3QA6ELQEPV/osi8rsi8kvax4eRLNKE6W7Mj/Ph9sMTIc0FNPcIm57mx9iwVG4B6OK4nTgWp4617jL29VShOO9rhR8si2uWfgjCeRw2VPw8hCDnqhFC+oa6CEDlmyLyyyLyx9iDr6XDVlIJq7DmdEUAOnNBqn4LDEkAmuuVi57dijR8AnraguoBzFoHwWrz9z6pCzmybrSfMr415NMChqcXYRXUOYSzKURgL2/ZRrpMhm3YyqSOix/6bsFGGdRJABrqLPqdIvJjIvLbGPIaDSNpfY0JodkuiTLrOMtyj9CJoDogWEQvwqecTx98c84wcGm+/TAMq3MGVzD0rJY5HebxvdLPjXMJ8a2YG5k2C4u87XJCSJv61Yoy+5sLAcylToUO+2L+MAWgB+ooAI0vYDjY9u97r4i8Q0TOhJG8vsNE31wJWxY1w4Y7q7IAWgcUigXQxNmSZ/cna90QgAYWn8xhyocuFlkqc2hWhSesMGuwdM4323Ghbu4ySG2wfqRVHV/FatdS6p3j3qhO0x+qWHDYk4TmCDoPW5gj+B4ROSsiP44H1sfQeL4qIjfqd1u1Y93Z0aDUtzPX2lXhvK1GBxTIxuhSxvZI8tq8vRf0RQvCrHQgYK8iHu/DwC3u0eJpF98q8oEikPjC6lKrlzazDJY1VFz2TiNlYNvnhbwXey3oBQHocgjLoK4Y/nXME3yjiJzXfn5qaoqLR8rFLCdlW4qK7nRRCEcABDFsgo7wAjbcL0MQW7mWLsaaxNkVseVszN/OsmDiulvb3JHep+1UFrTnvHtzp8HadJ0EYNb9i0kLKhkCnpqaYnn0JssY/rVVo96tY3AlYtuNZbF2+Zy8X4q1rQCWnlL8YqXxCYhh1Fm4cfHh06/jXB8sHFn3uEn+eoe9QFdQr+fy+EYkxCXDSIbW7w+j3/P2EoY2exFuo6qaS50Ha4c6TzirGyfi0GsWQFIt5vNtokTr3LKFn/EBfNHjijsvzpZ9AEGsK2e3Stgc3aWTFXASc5W8vJWn3EP42S7NN23guLGZ6Ga8JDh89yOdXmCW8cJ72bP7q8XEZy1wfIsK22ExKACJbxYxZHHJ95AhtvoyR8d5Gn5hUYo02HBrCG+epVr/HDoJQMsLX8MyFk47y4TWsws+HooQnDN40LbDrM9PB+LCg3SfhaJ1LjGS0bbtJgSPl3aOfuwJ9KV13FFjyRHFbIc5oQAkZTCPxnnFlwhEI7+CcPOKjItFHCSj0w7tzdPmo5XaiWOIyOYiPfTww/83PFpa7b7azU0yi6cPa/MCLHttrah4GFvaVorOy9L6qK5oUlo8DS5CqZaO9SQFSxlHMpZsjmocx4XaOuqstZkq57PmXlWfWLjlox0u5GiHJGdmV3n0ClXnY6dj3snnBffcHPXFDSuzoMR1OqdszdKTORH3w1nF9akFh4ohXONdMKoQQ9hdmb+Dcmx5/7oYBf/fLNIh6wMuzX1pZ424ctULJxy3fqVKt5PG3Pfq5Oda2gePxZknvqJArMZZBL61vSrT0CG81O3Tidv6keU8gsGpb+tZrtd65tT3XCIwEUaWfsxrOcqD/amPvqJIO5x3yrVlebh1JevzkDyYkRSAxQldAJogsM5mFYIlS8OcxltZjHByPeSd+Cedznsl7TBO4rpMYqtkAbiEsLvyFo98UFoOfSc65EzlhfJeda7v2KEnH4pZH8jOQz1zGTn3mula5KNbr7OIALuu65YbCsDX4nZfUjLmx6JT7pkFS6K+r2YZik7U9UwC0nc5yoMvQIWsqR7bYdu8pAD0BAWgF+ogAK3DWnNueBVvXE0bG0TAvNMwY1xf5C0xts4LjX7VCXsZQvWhhzDSvpjocLMKjDIF4DrC7tqwhVMuLYfhEw+adXT0TcsP5TGX6MTXs5Q3ysnyYrNdmcqD5bruxJnXKryQSPdim3udhWi3+pTa8pcIo1Ca80IB+GDczgtY234NdXw+UUeL9GfJPrVTH7ZQtK77Lkd52IKfy5rqhFW0HXYU0hSAnqAA9EJdBKAd84lOyFhLDM+6rBcZ2jMQ3mrit2bp2URaVpv8nkvAlSUAneHWrq5EduJta0HAg2clfhg3jzeb5PNSzmG1yYRYd7H4mtW/VQ/zh6YTAtYNu9V9FpmLupgIby1RZ0t5IaAAfDhuXJ/sL9wySZZ96pGHlOlpVrda9afLeeP2XY5OuHOJe1hP5Fvq+d5lt8NeFICVOEauOEN6RY7X1an1DBZxWCfqOt69Blcya778yclrC0g2m4WHDmYW6Zp2/MC9hJWt2ukt5/X5hrh1W7PnfO5ri458Gn7wuroa2R6AabacQzrnnPydweR3waT2dSefV3z41kuU6SR8nRlWxyw+b3nn3Oss7tXitfvU+rfqw10PymAe92jxbCGOhTL8ujl1bi1tObVre91KQ4fwbPV3x3YEsaCuh55M1v0UZW/9SBm+Ud367ravlxJtK3fcvssxEfY0FqPMNHkeLGddpVxWO3TrSlYft1EU5uOaArC+1HZXk1AbQxmUJQAJIV1vyy0FIOkf8uiXUJ95dANDCCGEENJnUAASQgghhPQZFICEEEIIIX0GBSAh5WIrTLlhOSGEkGCgACSkXCgACSGEBAcFICElAbcB6o5gi6sGCSGEhAQFICHlseRp43hCCCHEKxSAhJQANlq/DOe89P9HCCEkKIZYHITkw/HAb97lBd/nsaOIir/Zbu/UQQghhHSCApCQ/OgCj6dbXK3bGM1T/BFCCAmRftwKjlRML20FF8fxjLPPrdjemxR+hBDSe/TSVnCEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEkMKIyP8DaRI6O4x0rUgAAAAASUVORK5CYII="
                pixmap = QtGui.QPixmap()
                header = base64.b64decode(h64)
                pixmap.loadFromData(header)
                self.mw.lbl_header.setPixmap(pixmap)
                
                ##Loading Bundle Info
                
                #Table View
                ##Table Item Viewer
                header = self.mw.tableWidget.horizontalHeader()
                header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
                
                header2 = self.mw.tableWidget_2.horizontalHeader()
                header2.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
                
                ##Table Clicked
                self.mw.tableWidget.doubleClicked.connect(self.importItem)
                self.mw.tableWidget_2.doubleClicked.connect(self.loadItem)
                
                
                #Buttons
                self.mw.btn_load.clicked.connect(self.loadMain)
                self.mw.btn_return.clicked.connect(self.back)
                
                
    def importItem(self,mi):
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
            
                
    def back(self):
        self.mw.stackedWidget.setCurrentIndex(0)
                
    def loadMain(self):
        #Load Dir File
        with open((locPath + "\Dirs.txt"),'r') as dirsF:
            #Read Lines into List.
            cLines = dirsF.readlines()
            cLines = [x.strip() for x in cLines] #Strips whitespace chars like \n etc.
            global dirLst
            dirLst = cLines
            
        #Add Items to Table Widget with Number of Dirs and Fill the Names
        for i in range(len(dirLst)):
            rowPosition = self.mw.tableWidget_2.rowCount()
            self.mw.tableWidget_2.insertRow(rowPosition)
            dirAdd = dirLst[i]
            #print(dirAdd)
            self.mw.tableWidget_2.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(dirAdd))
            
        #Add Bundle Image to Label
        try:
            bundleImg = locPath + "\Bundle.jpg"
        except:
            bundleImg = locPath + "\Bundle.png"
            
        #Assign to Label
        bundlePixmap = QtGui.QPixmap(bundleImg)
        self.mw.lbl_bundleImg.setPixmap(bundlePixmap)
        
        
        
    def loadItem(self,ind):
        global dirLst, imgs
        indexR = ind.row()

        #Fill Item on other Table with Index
        self.mw.tableWidget.setRowCount(0)
        imgs = []
        path = locPath + dirLst[indexR]
        self.mw.lbl_item.setText(dirLst[indexR])
        valid_images = [".jpg",".png"]
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
        #Switch Stacked Widget to Second Page.
        self.mw.stackedWidget.setCurrentIndex(1)

            
        



                
isPanel = False
#Create the UI Block
if isPanel == True:
    #Create Interface Python Panel
    def onCreateInterface():
        my_window = MyWindow()
        my_window.show()
        return my_window
elif isPanel == False:
    #Create Interface Shelf.
    try:
        my_window.close()
    except:
        pass
    my_window = MyWindow()
    #my_window.resize(360,720)
    my_window.show() 

