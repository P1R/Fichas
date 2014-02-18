#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Solver.ui'
#
# Created: Mon Feb 17 16:59:19 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Pila import *
from Gira import Resolv
from Soniguales import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(636, 559)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(636, 559))
        Form.setMaximumSize(QtCore.QSize(636, 559))
        self.gridLayoutWidget = QtGui.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 100, 261, 211))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit_4 = QtGui.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bitstream Vera Sans"))
        font.setPointSize(48)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setMaxLength(1)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout.addWidget(self.lineEdit_4, 1, 1, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bitstream Vera Sans"))
        font.setPointSize(48)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setMaxLength(1)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 1, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bitstream Vera Sans"))
        font.setPointSize(48)
        self.lineEdit.setFont(font)
        self.lineEdit.setMaxLength(1)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bitstream Vera Sans"))
        font.setPointSize(48)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setMaxLength(1)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.gridLayoutWidget_2 = QtGui.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(340, 100, 261, 211))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lineEdit_5 = QtGui.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bitstream Vera Sans"))
        font.setPointSize(48)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setMaxLength(1)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.gridLayout_2.addWidget(self.lineEdit_5, 0, 0, 1, 1)
        self.lineEdit_8 = QtGui.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bitstream Vera Sans"))
        font.setPointSize(48)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setMaxLength(1)
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.gridLayout_2.addWidget(self.lineEdit_8, 1, 1, 1, 1)
        self.lineEdit_6 = QtGui.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bitstream Vera Sans"))
        font.setPointSize(48)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setMaxLength(1)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.gridLayout_2.addWidget(self.lineEdit_6, 0, 1, 1, 1)
        self.lineEdit_7 = QtGui.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bitstream Vera Sans"))
        font.setPointSize(48)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setMaxLength(1)
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.gridLayout_2.addWidget(self.lineEdit_7, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(280, 190, 58, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bitstream Vera Sans"))
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 330, 581, 193))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textBrowser = QtGui.QTextBrowser(self.widget)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.widget1 = QtGui.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(20, 20, 581, 58))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bitstream Vera Sans"))
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bitstream Vera Sans"))
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_3.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_2.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_4.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_7.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_8.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_5.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_6.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textBrowser.clear)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.procesar)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Juego de Cuatro Fichas", None))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#d00000;\">=</span><span style=\" font-weight:600; color:#d00000;\">&gt;</span></p></body></html>", None))
        self.pushButton_2.setText(_translate("Form", "Limpiar", None))
        self.pushButton.setText(_translate("Form", "Resolver", None))
        self.label.setText(_translate("Form", "Inicial", None))
        self.label_2.setText(_translate("Form", "Final", None))
        
    def procesar(self):
		text = "Error en los datos ingresados, deben ser 1, 2, 3 o B y no repetirlos"
		k = 0;
		C=Pila();
		cont = 0;
		final=[0]*4;
		pilaf=[0]*4;
		Found=Pila();
		pilaf[0]=str(_fromUtf8(self.lineEdit.text()))
		pilaf[1]=str(_fromUtf8(self.lineEdit_2.text()))
		pilaf[2]=str(_fromUtf8(self.lineEdit_3.text()))
		pilaf[3]=str(_fromUtf8(self.lineEdit_4.text()))
		for i in range(len(pilaf)):
			try:
				pilaf[i]=int(pilaf[i])
			except(ValueError,TypeError):
				if pilaf[i] == 'b' or pilaf[i] == 'B':
					pilaf[i] = 'B'
					pass
				else:
					QMessageBox.information(self.iface.mainWindow(),"test", "%s" % (text), QMessageBox.Ok)
		final[0]=str(_fromUtf8(self.lineEdit_5.text()))
		final[1]=str(_fromUtf8(self.lineEdit_6.text()))
		final[2]=str(_fromUtf8(self.lineEdit_7.text()))
		final[3]=str(_fromUtf8(self.lineEdit_8.text()))
		for i in range(len(final)):
			try:
				final[i]=int(final[i])
			except(ValueError,TypeError):
				if final[i] == 'b' or final[i] == 'B':
					final[i] = 'B'
					pass
				else:
					QMessageBox.information(self.iface.mainWindow(),"test", "%s" % (text), QMessageBox.Ok)
		C.apilar(pilaf)	
		while(pilaf != final or k < 20):
			C.desapilar()       
			derecha, sux = Resolv(final, pilaf, 'R')
			
			if C.vacia():
				C.apilar(derecha)
			else:
				for i in range(len(C.items)):
					if sonListasIguales(C.items[i], derecha) == False:
						cont += 1
				if cont == len(C.items):
					C.apilar(derecha)
				cont = 0
						
			izq, sux1 = Resolv(final, pilaf, 'I')
			
			if C.vacia():
				C.apilar(izq)
			else:
				for i in range(len(C.items)):
					if sonListasIguales(C.items[i], izq) == False:
						cont += 1
				if cont == len(C.items):
					C.apilar(izq)
				cont = 0
						
			for i in range(len(pilaf)):
				pilaf[i] = derecha[i]
			self.textBrowser.append("%s" % C.items)
			k += 1
     
		
if __name__ == "__main__":
    import sys;
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

