# -*- coding: utf-8 -*-

"""
/***************************************************************************
Name            : ImagineSustainability
Description     : geographical MCDA for sustainability assessment
Date            : 25/06/2023
copyright       : Università degli Studi di Perugia (C) 2023
email           : (developper) Gianluca Massei (geonomica@gmail.com)

 ***************************************************************************/


/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""


from __future__ import absolute_import
from builtins import object

from PyQt5.QtCore import QSettings, QTranslator, qVersion, QCoreApplication,Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QMessageBox, QMenu, QAction
from qgis.core import QgsMapLayer
# Initialize Qt resources from file resources.py
from . import resources
import os
import webbrowser

import numpy as np





class ImagineSustainability:
    def __init__(self, iface):
        self.iface = iface  

    def initGui(self):
        self.actionIMAGINE = QAction(QIcon(":/plugins/ImagineSustainability/icon.png"), "Imagine Sustainability", self.iface.mainWindow())
        self.actionIMAGINE.triggered.connect(self.runImagineSustainability)
        self.iface.addToolBarIcon(self.actionIMAGINE)
        self.iface.addPluginToMenu( "&ImagineSustainability",self.actionIMAGINE )

    def unload(self):
        self.iface.removePluginMenu( "&ImagineSustainability",self.actionIMAGINE)
        self.iface.removeToolBarIcon(self.actionIMAGINE)
        
    def runImagineSustainability(self):
        from .guiImagineSustainability import guiImagineSustainabilityDialog
        self.active_layer = self.iface.activeLayer()
        self.base_layer = self.iface.activeLayer()
        if ((self.active_layer == None) or (self.active_layer.type() != QgsMapLayer.VectorLayer)):
            result=QMessageBox.warning(self.iface.mainWindow(), "ImagineSustainability",
            ("No active layer found\n" "Please make active one \n" \
            "Do you need documents or data ?"), QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if result  == QMessageBox.Yes:
                webbrowser.open("http://maplab.alwaysdata.net/")
        elif (self.iface.activeLayer().storageType() != 'GPKG'):
            result=QMessageBox.warning(self.iface.mainWindow(), "ImagineSustainability",
            ("Active layer is not a geopackage format\n"), QMessageBox.Ok)
        else:
            dlg = guiImagineSustainabilityDialog(self.iface)
            flags = Qt.Window | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint
            dlg.setWindowFlags(flags)
            dlg.setWindowModality(Qt.NonModal)
            #dlg.setModal(False)
            dlg.show()
            dlg.exec_()

