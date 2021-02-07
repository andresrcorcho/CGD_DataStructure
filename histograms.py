# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'histograms.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Geochronology(object):
    def setupUi(self, Geochronology):
        Geochronology.setObjectName("Geochronology")
        Geochronology.resize(1440, 808)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Geochronology.sizePolicy().hasHeightForWidth())
        Geochronology.setSizePolicy(sizePolicy)
        self.Principal = QtWidgets.QWidget(Geochronology)
        self.Principal.setObjectName("Principal")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Principal)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.MainLayout = QtWidgets.QGridLayout()
        self.MainLayout.setContentsMargins(0, -1, 0, -1)
        self.MainLayout.setHorizontalSpacing(6)
        self.MainLayout.setObjectName("MainLayout")
        self.LayOutWidget = QtWidgets.QWidget(self.Principal)
        self.LayOutWidget.setObjectName("LayOutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.LayOutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.KDEs = QtWidgets.QGridLayout()
        self.KDEs.setSpacing(0)
        self.KDEs.setObjectName("KDEs")
        self.Methods = QtWidgets.QTabWidget(self.LayOutWidget)
        self.Methods.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Methods.sizePolicy().hasHeightForWidth())
        self.Methods.setSizePolicy(sizePolicy)
        self.Methods.setAccessibleName("")
        self.Methods.setMovable(False)
        self.Methods.setObjectName("Methods")
        self.KDEf = MplWidget()
        self.KDEf.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.KDEf.sizePolicy().hasHeightForWidth())
        self.KDEf.setSizePolicy(sizePolicy)
        self.KDEf.setObjectName("KDEf")
        self.Methods.addTab(self.KDEf, "")
        self.PDPf = MplWidget()
        self.PDPf.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PDPf.sizePolicy().hasHeightForWidth())
        self.PDPf.setSizePolicy(sizePolicy)
        self.PDPf.setObjectName("PDPf")
        self.Methods.addTab(self.PDPf, "")
        self.KDEa = MplWidget()
        self.KDEa.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.KDEa.sizePolicy().hasHeightForWidth())
        self.KDEa.setSizePolicy(sizePolicy)
        self.KDEa.setObjectName("KDEa")
        self.Methods.addTab(self.KDEa, "")
        self.KDEs.addWidget(self.Methods, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.KDEs, 0, 0, 2, 1)
        self.LoadFiles = QtWidgets.QGroupBox(self.LayOutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.LoadFiles.setFont(font)
        self.LoadFiles.setObjectName("LoadFiles")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.LoadFiles)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.f11 = QtWidgets.QCheckBox(self.LoadFiles)
        self.f11.setEnabled(False)
        self.f11.setText("")
        self.f11.setObjectName("f11")
        self.gridLayout_3.addWidget(self.f11, 4, 1, 1, 1)
        self.f14 = QtWidgets.QCheckBox(self.LoadFiles)
        self.f14.setEnabled(False)
        self.f14.setText("")
        self.f14.setObjectName("f14")
        self.gridLayout_3.addWidget(self.f14, 1, 2, 1, 1)
        self.f1 = QtWidgets.QCheckBox(self.LoadFiles)
        self.f1.setEnabled(False)
        self.f1.setText("")
        self.f1.setObjectName("f1")
        self.gridLayout_3.addWidget(self.f1, 0, 0, 1, 1)
        self.f6 = QtWidgets.QCheckBox(self.LoadFiles)
        self.f6.setEnabled(False)
        self.f6.setText("")
        self.f6.setObjectName("f6")
        self.gridLayout_3.addWidget(self.f6, 6, 0, 1, 1)
        self.f7 = QtWidgets.QCheckBox(self.LoadFiles)
        self.f7.setEnabled(False)
        self.f7.setText("")
        self.f7.setObjectName("f7")
        self.gridLayout_3.addWidget(self.f7, 0, 1, 1, 1)
        self.f10 = QtWidgets.QCheckBox(self.LoadFiles)
        self.f10.setEnabled(False)
        self.f10.setText("")
        self.f10.setObjectName("f10")
        self.gridLayout_3.addWidget(self.f10, 3, 1, 1, 1)
        self.f13 = QtWidgets.QCheckBox(self.LoadFiles)
        self.f13.setEnabled(False)
        self.f13.setText("")
        self.f13.setObjectName("f13")
        self.gridLayout_3.addWidget(self.f13, 0, 2, 1, 1)
        self.f2 = QtWidgets.QCheckBox(self.LoadFiles)
        self.f2.setEnabled(False)
        self.f2.setText("")
        self.f2.setObjectName("f2")
        self.gridLayout_3.addWidget(self.f2, 1, 0, 1, 1)
        self.f5 = QtWidgets.QCheckBox(self.LoadFiles)
        self.f5.setEnabled(False)
        self.f5.setText("")
        self.f5.setObjectName("f5")
        self.gridLayout_3.addWidget(self.f5, 4, 0, 1, 1)
        self.loadSession = QtWidgets.QPushButton(self.LoadFiles)
        self.loadSession.setObjectName("loadSession")
        self.gridLayout_3.addWidget(self.loadSession, 8, 1, 1, 1)
        self.f12 = QtWidgets.QCheckBox(self.LoadFiles)
        self.f12.setEnabled(False)
        self.f12.setText("")
        self.f12.setObjectName("f12")
        self.gridLayout_3.addWidget(self.f12, 6, 1, 1, 1)
        self.f3 = QtWidgets.QCheckBox(self.LoadFiles)
        self.f3.setEnabled(False)
        self.f3.setText("")
        self.f3.setObjectName("f3")
        self.gridLayout_3.addWidget(self.f3, 2, 0, 1, 1)
        self.f4 = QtWidgets.QCheckBox(self.LoadFiles)
        self.f4.setEnabled(False)
        self.f4.setText("")
        self.f4.setObjectName("f4")
        self.gridLayout_3.addWidget(self.f4, 3, 0, 1, 1)
        self.f8 = QtWidgets.QCheckBox(self.LoadFiles)
        self.f8.setEnabled(False)
        self.f8.setText("")
        self.f8.setObjectName("f8")
        self.gridLayout_3.addWidget(self.f8, 1, 1, 1, 1)
        self.resetFields = QtWidgets.QPushButton(self.LoadFiles)
        self.resetFields.setObjectName("resetFields")
        self.gridLayout_3.addWidget(self.resetFields, 8, 0, 1, 1)
        self.f18 = QtWidgets.QCheckBox(self.LoadFiles)
        self.f18.setEnabled(False)
        self.f18.setText("")
        self.f18.setObjectName("f18")
        self.gridLayout_3.addWidget(self.f18, 6, 2, 1, 1)
        self.f15 = QtWidgets.QCheckBox(self.LoadFiles)
        self.f15.setEnabled(False)
        self.f15.setText("")
        self.f15.setObjectName("f15")
        self.gridLayout_3.addWidget(self.f15, 2, 2, 1, 1)
        self.f16 = QtWidgets.QCheckBox(self.LoadFiles)
        self.f16.setEnabled(False)
        self.f16.setText("")
        self.f16.setObjectName("f16")
        self.gridLayout_3.addWidget(self.f16, 3, 2, 1, 1)
        self.f9 = QtWidgets.QCheckBox(self.LoadFiles)
        self.f9.setEnabled(False)
        self.f9.setText("")
        self.f9.setObjectName("f9")
        self.gridLayout_3.addWidget(self.f9, 2, 1, 1, 1)
        self.saveSession = QtWidgets.QPushButton(self.LoadFiles)
        self.saveSession.setObjectName("saveSession")
        self.gridLayout_3.addWidget(self.saveSession, 8, 2, 1, 1)
        self.plotData = QtWidgets.QPushButton(self.LoadFiles)
        self.plotData.setObjectName("plotData")
        self.gridLayout_3.addWidget(self.plotData, 9, 1, 1, 1)
        self.f17 = QtWidgets.QCheckBox(self.LoadFiles)
        self.f17.setEnabled(False)
        self.f17.setText("")
        self.f17.setObjectName("f17")
        self.gridLayout_3.addWidget(self.f17, 4, 2, 1, 1)
        self.gridLayout.addWidget(self.LoadFiles, 1, 1, 2, 1)
        self.actions = QtWidgets.QGroupBox(self.LayOutWidget)
        self.actions.setTitle("")
        self.actions.setObjectName("actions")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.actions)
        self.horizontalLayout.setContentsMargins(8, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.exoandStatus = QtWidgets.QCheckBox(self.actions)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.exoandStatus.setFont(font)
        self.exoandStatus.setObjectName("exoandStatus")
        self.horizontalLayout.addWidget(self.exoandStatus)
        self.sizeFactorV = QtWidgets.QSlider(self.actions)
        self.sizeFactorV.setEnabled(False)
        self.sizeFactorV.setMinimum(1)
        self.sizeFactorV.setMaximum(20)
        self.sizeFactorV.setOrientation(QtCore.Qt.Horizontal)
        self.sizeFactorV.setObjectName("sizeFactorV")
        self.horizontalLayout.addWidget(self.sizeFactorV)
        self.sizeFactorH = QtWidgets.QSlider(self.actions)
        self.sizeFactorH.setEnabled(False)
        self.sizeFactorH.setMinimum(1)
        self.sizeFactorH.setMaximum(20)
        self.sizeFactorH.setOrientation(QtCore.Qt.Horizontal)
        self.sizeFactorH.setObjectName("sizeFactorH")
        self.horizontalLayout.addWidget(self.sizeFactorH)
        self.label = QtWidgets.QLabel(self.actions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.dataName = QtWidgets.QLineEdit(self.actions)
        self.dataName.setObjectName("dataName")
        self.horizontalLayout.addWidget(self.dataName)
        self.LoadData = QtWidgets.QPushButton(self.actions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoadData.sizePolicy().hasHeightForWidth())
        self.LoadData.setSizePolicy(sizePolicy)
        self.LoadData.setObjectName("LoadData")
        self.horizontalLayout.addWidget(self.LoadData)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 6)
        self.gridLayout.addWidget(self.actions, 2, 0, 1, 1)
        self.Parameters = QtWidgets.QGroupBox(self.LayOutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Parameters.sizePolicy().hasHeightForWidth())
        self.Parameters.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Parameters.setFont(font)
        self.Parameters.setObjectName("Parameters")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.Parameters)
        self.gridLayout_4.setHorizontalSpacing(3)
        self.gridLayout_4.setVerticalSpacing(14)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Hist = QtWidgets.QCheckBox(self.Parameters)
        self.Hist.setObjectName("Hist")
        self.gridLayout_4.addWidget(self.Hist, 4, 0, 1, 1)
        self.TSize = QtWidgets.QSlider(self.Parameters)
        self.TSize.setMinimum(5)
        self.TSize.setMaximum(20)
        self.TSize.setProperty("value", 9)
        self.TSize.setOrientation(QtCore.Qt.Horizontal)
        self.TSize.setObjectName("TSize")
        self.gridLayout_4.addWidget(self.TSize, 9, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.Parameters)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 3, 0, 1, 1)
        self.BW = QtWidgets.QLabel(self.Parameters)
        self.BW.setText("")
        self.BW.setObjectName("BW")
        self.gridLayout_4.addWidget(self.BW, 1, 4, 1, 1)
        self.savepdf = QtWidgets.QCheckBox(self.Parameters)
        self.savepdf.setObjectName("savepdf")
        self.gridLayout_4.addWidget(self.savepdf, 2, 4, 1, 1)
        self.Minin = QtWidgets.QLineEdit(self.Parameters)
        self.Minin.setObjectName("Minin")
        self.gridLayout_4.addWidget(self.Minin, 2, 2, 1, 1)
        self.peakvalue = QtWidgets.QLabel(self.Parameters)
        self.peakvalue.setMidLineWidth(1)
        self.peakvalue.setText("")
        self.peakvalue.setObjectName("peakvalue")
        self.gridLayout_4.addWidget(self.peakvalue, 5, 4, 1, 1)
        self.peakdetect = QtWidgets.QCheckBox(self.Parameters)
        self.peakdetect.setObjectName("peakdetect")
        self.gridLayout_4.addWidget(self.peakdetect, 5, 0, 1, 1)
        self.delta = QtWidgets.QSlider(self.Parameters)
        self.delta.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delta.sizePolicy().hasHeightForWidth())
        self.delta.setSizePolicy(sizePolicy)
        self.delta.setMinimum(1)
        self.delta.setMaximum(50)
        self.delta.setSingleStep(1)
        self.delta.setPageStep(30)
        self.delta.setProperty("value", 2)
        self.delta.setSliderPosition(2)
        self.delta.setTracking(True)
        self.delta.setOrientation(QtCore.Qt.Horizontal)
        self.delta.setObjectName("delta")
        self.gridLayout_4.addWidget(self.delta, 5, 2, 1, 2)
        self.Maxi = QtWidgets.QLineEdit(self.Parameters)
        self.Maxi.setObjectName("Maxi")
        self.gridLayout_4.addWidget(self.Maxi, 3, 2, 1, 1)
        self.ticksadjust = QtWidgets.QLabel(self.Parameters)
        self.ticksadjust.setObjectName("ticksadjust")
        self.gridLayout_4.addWidget(self.ticksadjust, 0, 0, 1, 1)
        self.bins = QtWidgets.QLineEdit(self.Parameters)
        self.bins.setEnabled(False)
        self.bins.setReadOnly(False)
        self.bins.setObjectName("bins")
        self.gridLayout_4.addWidget(self.bins, 4, 2, 1, 1)
        self.tsize = QtWidgets.QLabel(self.Parameters)
        self.tsize.setText("")
        self.tsize.setObjectName("tsize")
        self.gridLayout_4.addWidget(self.tsize, 9, 4, 1, 1)
        self.tratio = QtWidgets.QSlider(self.Parameters)
        self.tratio.setMinimum(1)
        self.tratio.setMaximum(50)
        self.tratio.setSingleStep(1)
        self.tratio.setPageStep(1)
        self.tratio.setProperty("value", 8)
        self.tratio.setOrientation(QtCore.Qt.Horizontal)
        self.tratio.setObjectName("tratio")
        self.gridLayout_4.addWidget(self.tratio, 0, 1, 1, 3)
        self.TR = QtWidgets.QLabel(self.Parameters)
        self.TR.setText("")
        self.TR.setObjectName("TR")
        self.gridLayout_4.addWidget(self.TR, 0, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.Parameters)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 2, 0, 1, 1)
        self.sharedXY = QtWidgets.QCheckBox(self.Parameters)
        self.sharedXY.setObjectName("sharedXY")
        self.gridLayout_4.addWidget(self.sharedXY, 7, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.Parameters)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 4, 4, 1, 1)
        self.sizeT = QtWidgets.QLabel(self.Parameters)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.sizeT.setFont(font)
        self.sizeT.setObjectName("sizeT")
        self.gridLayout_4.addWidget(self.sizeT, 9, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.Parameters)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.peakLabel = QtWidgets.QCheckBox(self.groupBox)
        self.peakLabel.setObjectName("peakLabel")
        self.horizontalLayout_2.addWidget(self.peakLabel)
        self.adjustLabel = QtWidgets.QCheckBox(self.groupBox)
        self.adjustLabel.setEnabled(False)
        self.adjustLabel.setObjectName("adjustLabel")
        self.horizontalLayout_2.addWidget(self.adjustLabel)
        self.gridLayout_4.addWidget(self.groupBox, 7, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.Parameters)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.KDEstatus = QtWidgets.QCheckBox(self.groupBox_2)
        self.KDEstatus.setObjectName("KDEstatus")
        self.horizontalLayout_3.addWidget(self.KDEstatus)
        self.PDPstatus = QtWidgets.QCheckBox(self.groupBox_2)
        self.PDPstatus.setChecked(False)
        self.PDPstatus.setObjectName("PDPstatus")
        self.horizontalLayout_3.addWidget(self.PDPstatus)
        self.gridLayout_4.addWidget(self.groupBox_2, 7, 2, 1, 1)
        self.Bw = QtWidgets.QSlider(self.Parameters)
        self.Bw.setMinimum(1)
        self.Bw.setMaximum(50)
        self.Bw.setPageStep(10)
        self.Bw.setProperty("value", 25)
        self.Bw.setSliderPosition(25)
        self.Bw.setTracking(True)
        self.Bw.setOrientation(QtCore.Qt.Horizontal)
        self.Bw.setObjectName("Bw")
        self.gridLayout_4.addWidget(self.Bw, 1, 2, 1, 1)
        self.savepng = QtWidgets.QCheckBox(self.Parameters)
        self.savepng.setObjectName("savepng")
        self.gridLayout_4.addWidget(self.savepng, 3, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.Parameters)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 1, 0, 1, 1)
        self.filled = QtWidgets.QCheckBox(self.Parameters)
        self.filled.setChecked(True)
        self.filled.setObjectName("filled")
        self.gridLayout_4.addWidget(self.filled, 8, 0, 1, 1)
        self.geoScale = QtWidgets.QCheckBox(self.Parameters)
        self.geoScale.setChecked(True)
        self.geoScale.setObjectName("geoScale")
        self.gridLayout_4.addWidget(self.geoScale, 8, 2, 1, 1)
        self.gridLayout.addWidget(self.Parameters, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setRowStretch(0, 4)
        self.gridLayout.setRowStretch(1, 4)
        self.MainLayout.addWidget(self.LayOutWidget, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.MainLayout, 1, 0, 1, 1)
        Geochronology.setCentralWidget(self.Principal)
        self.menubar = QtWidgets.QMenuBar(Geochronology)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 22))
        self.menubar.setObjectName("menubar")
        self.menugfg = QtWidgets.QMenu(self.menubar)
        self.menugfg.setObjectName("menugfg")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        Geochronology.setMenuBar(self.menubar)
        self.actionDataSets = QtWidgets.QAction(Geochronology)
        self.actionDataSets.setObjectName("actionDataSets")
        self.actionV_1_0 = QtWidgets.QAction(Geochronology)
        self.actionV_1_0.setObjectName("actionV_1_0")
        self.menugfg.addAction(self.actionDataSets)
        self.menuAbout.addAction(self.actionV_1_0)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menugfg.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(Geochronology)
        self.Methods.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Geochronology)

    def retranslateUi(self, Geochronology):
        _translate = QtCore.QCoreApplication.translate
        Geochronology.setWindowTitle(_translate("Geochronology", "Geochronological Plotter"))
        self.KDEf.setAccessibleName(_translate("Geochronology", "KDE"))
        self.Methods.setTabText(self.Methods.indexOf(self.KDEf), _translate("Geochronology", "KDE-Fixed Bw"))
        self.Methods.setTabText(self.Methods.indexOf(self.PDPf), _translate("Geochronology", "PDP"))
        self.Methods.setTabText(self.Methods.indexOf(self.KDEa), _translate("Geochronology", "KDE-PDP"))
        self.LoadFiles.setTitle(_translate("Geochronology", "Loaded Files"))
        self.loadSession.setText(_translate("Geochronology", "Load"))
        self.resetFields.setText(_translate("Geochronology", "Reset"))
        self.saveSession.setText(_translate("Geochronology", "Save"))
        self.plotData.setText(_translate("Geochronology", "Plot"))
        self.exoandStatus.setText(_translate("Geochronology", "Expand Size"))
        self.label.setText(_translate("Geochronology", "DataSet"))
        self.dataName.setText(_translate("Geochronology", "Unnamed"))
        self.LoadData.setText(_translate("Geochronology", "Load Data"))
        self.Parameters.setTitle(_translate("Geochronology", "Parameters"))
        self.Hist.setText(_translate("Geochronology", "Plot Bars"))
        self.label_5.setText(_translate("Geochronology", "Max."))
        self.savepdf.setText(_translate("Geochronology", "Save PDFs"))
        self.Minin.setText(_translate("Geochronology", "0"))
        self.peakdetect.setText(_translate("Geochronology", "Peak Detector"))
        self.Maxi.setText(_translate("Geochronology", "2000"))
        self.ticksadjust.setText(_translate("Geochronology", "Number of Ticks"))
        self.bins.setText(_translate("Geochronology", "100"))
        self.label_4.setText(_translate("Geochronology", "Min."))
        self.sharedXY.setText(_translate("Geochronology", "Shared Axes"))
        self.label_7.setText(_translate("Geochronology", "Bins"))
        self.sizeT.setText(_translate("Geochronology", "Text Size"))
        self.peakLabel.setText(_translate("Geochronology", "Label"))
        self.adjustLabel.setText(_translate("Geochronology", "Adjust"))
        self.KDEstatus.setText(_translate("Geochronology", "KDE-PDP"))
        self.PDPstatus.setText(_translate("Geochronology", "PDP"))
        self.savepng.setText(_translate("Geochronology", "Save PNGs"))
        self.label_6.setText(_translate("Geochronology", "Set BandWidth"))
        self.filled.setText(_translate("Geochronology", "Filled Plot"))
        self.geoScale.setText(_translate("Geochronology", "GeoColors"))
        self.menugfg.setTitle(_translate("Geochronology", "Layers"))
        self.menuAbout.setTitle(_translate("Geochronology", "About"))
        self.menuFile.setTitle(_translate("Geochronology", "File"))
        self.actionDataSets.setText(_translate("Geochronology", "DataSets"))
        self.actionV_1_0.setText(_translate("Geochronology", "V_1.0"))

from mplwidget import MplWidget