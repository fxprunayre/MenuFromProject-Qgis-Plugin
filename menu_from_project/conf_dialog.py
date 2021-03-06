# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W:\projets\QGis plugins\menu_from_project\conf_dialog.ui'
#
# Created: Tue Feb 19 16:47:11 2013
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from qgis.PyQt.QtCore import *
from qgis.PyQt.QtGui import *
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui

_fromUtf8 = lambda s: str(s)
_toUtf8 = lambda s: str(s)

class Ui_ConfDialog(object):
    def setupUi(self, ConfDialog):
        ConfDialog.setObjectName(_fromUtf8("ConfDialog"))
        ConfDialog.setWindowModality(QtCore.Qt.WindowModal)
        ConfDialog.resize(640, 224)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConfDialog.sizePolicy().hasHeightForWidth())
        ConfDialog.setSizePolicy(sizePolicy)
        ConfDialog.setMinimumSize(QtCore.QSize(540, 150))
        ConfDialog.setSizeGripEnabled(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ConfDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tableWidget = QtWidgets.QTableWidget(ConfDialog)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideNone)
        self.tableWidget.setRowCount(2)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(17)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnAdd = QtWidgets.QToolButton(ConfDialog)
        self.btnAdd.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.horizontalLayout.addWidget(self.btnAdd)
        self.btnDelete = QtWidgets.QToolButton(ConfDialog)
        self.btnDelete.setObjectName(_fromUtf8("btnDelete"))
        self.horizontalLayout.addWidget(self.btnDelete)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.cbxShowTooltip = QtWidgets.QCheckBox(ConfDialog)
        self.cbxShowTooltip.setChecked(True)
        self.cbxShowTooltip.setTristate(False)
        self.cbxShowTooltip.setObjectName(_fromUtf8("cbxShowTooltip"))
        self.horizontalLayout_2.addWidget(self.cbxShowTooltip)
        self.cbxLoadAll = QtWidgets.QCheckBox(ConfDialog)
        self.cbxLoadAll.setTristate(False)
        self.cbxLoadAll.setObjectName(_fromUtf8("cbxLoadAll"))
        self.horizontalLayout_2.addWidget(self.cbxLoadAll)
        self.cbxCreateGroup = QtWidgets.QCheckBox(ConfDialog)
        self.cbxCreateGroup.setChecked(False)
        self.cbxCreateGroup.setTristate(False)
        self.cbxCreateGroup.setObjectName(_fromUtf8("cbxCreateGroup"))
        self.horizontalLayout_2.addWidget(self.cbxCreateGroup)
        
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(ConfDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(ConfDialog)
        self.buttonBox.accepted.connect(ConfDialog.accept)
        self.buttonBox.rejected.connect(ConfDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConfDialog)

    def retranslateUi(self, ConfDialog):
        ConfDialog.setWindowTitle(QtWidgets.QApplication.translate("ConfDialog", "Projects", None))
        self.tableWidget.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("ConfDialog", "...", None))
        self.tableWidget.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("ConfDialog", "QGis Project", None))
        self.tableWidget.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("ConfDialog", "Name", None))
        self.btnAdd.setText(QtWidgets.QApplication.translate("ConfDialog", "+", None))
        self.btnDelete.setText(QtWidgets.QApplication.translate("ConfDialog", "-", None))
        self.cbxShowTooltip.setText(QtWidgets.QApplication.translate("ConfDialog", "Show title && abstract in tooltip", None))
        self.cbxLoadAll.setText(QtWidgets.QApplication.translate("ConfDialog", "Load all layers item", None))
        self.cbxCreateGroup.setText(QtWidgets.QApplication.translate("ConfDialog", "Create group", None))

