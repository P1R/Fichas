# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Solver.ui'
#
# Created: Sat Feb 15 23:54:23 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Pila import *
from Gira import Resolv

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
        Form.resize(529, 281)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 40, 81, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayoutWidget = QtGui.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(110, 10, 261, 211))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
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
        self.lineEdit_3 = QtGui.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bitstream Vera Sans"))
        font.setPointSize(48)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setMaxLength(1)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 1, 0, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bitstream Vera Sans"))
        font.setPointSize(48)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setMaxLength(1)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout.addWidget(self.lineEdit_4, 1, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 130, 81, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.treeView = QtGui.QTreeView(Form)
        self.treeView.setGeometry(QtCore.QRect(390, 20, 111, 192))
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 230, 311, 41))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.procesar)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_3.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_2.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_4.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.treeView.reset)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Resolver", None))
        self.pushButton_2.setText(_translate("Form", "Limpiar", None))
    
    #def VerCad(self,X):
		#text = "Error en los datos ingresados, deben ser 1, 2, 3 o B y no repetirlos"
		#for i in X:
			#if int(X[i])== 1 or int(X[i])== 2 or int(X[i])==3:
				#if len(X)!=len(set(X)):
					#QMessageBox.information(self.iface.mainWindow(),"test", "%s" % (text), QMessageBox.Ok)
					#self.lineEdit.clear
					#self.lineEdit_2.clear
					#self.lineEdit_3.clear
					#self.lineEdit_4.clear
					#self.label.clear
					#self.treeView.reset
				#else:	
					#X[i] = int(X[i])
			#elif 'b' == find(X[i],'b') or X[i] =='%c' % find(X[i],'B'):
				#if len(X)!=len(set(X)):
					#QMessageBox.information(self.iface.mainWindow(),"test", "%s" % (text), QMessageBox.Ok)
					#self.lineEdit.clear
					#self.lineEdit_2.clear
					#self.lineEdit_3.clear
					#self.lineEdit_4.clear
					#self.label.clear
					#self.treeView.reset
				#else:
					#X[i] = 'B'
			#else:
				#QMessageBox.information(self.iface.mainWindow(),"test", "%s" % (text), QMessageBox.Ok)
				#self.lineEdit.clear
				#self.lineEdit_2.clear
				#self.lineEdit_3.clear
				#self.lineEdit_4.clear
				#self.label.clear
				#self.treeView.reset	
		#return X	
			
    #def VerCad(self,X):
		#text = "Error en los datos ingresados, deben ser 1, 2, 3 o B y no repetirlos"
		#for i in X:
			#if int(X[i])== 1 or int(X[i])== 2 or int(X[i])==3:
				#if len(X)!=len(set(X)):
					#QMessageBox.information(self.iface.mainWindow(),"test", "%s" % (text), QMessageBox.Ok)
					#self.lineEdit.clear
					#self.lineEdit_2.clear
					#self.lineEdit_3.clear
					#self.lineEdit_4.clear
					#self.label.clear
					#self.treeView.reset
				#else:	
					#X[i] = int(X[i])
			#elif 'b' == find(X[i],'b') or X[i] =='%c' % find(X[i],'B'):
				#if len(X)!=len(set(X)):
					#QMessageBox.information(self.iface.mainWindow(),"test", "%s" % (text), QMessageBox.Ok)
					#self.lineEdit.clear
					#self.lineEdit_2.clear
					#self.lineEdit_3.clear
					#self.lineEdit_4.clear
					#self.label.clear
					#self.treeView.reset
				#else:
					#X[i] = 'B'
			#else:
				#QMessageBox.information(self.iface.mainWindow(),"test", "%s" % (text), QMessageBox.Ok)
				#self.lineEdit.clear
				#self.lineEdit_2.clear
				#self.lineEdit_3.clear
				#self.lineEdit_4.clear
				#self.label.clear
				#self.treeView.reset	
		#return X					
    def procesar(self):
		text = "Error en los datos ingresados, deben ser 1, 2, 3 o B y no repetirlos"
		Fin=[1,2,3,'B'];
		C=Pila();
		X=[3,2,1,'B'];
		Found=Pila();
		X[0]=str(_fromUtf8(self.lineEdit.text()))
		X[1]=str(_fromUtf8(self.lineEdit_2.text()))
		X[2]=str(_fromUtf8(self.lineEdit_3.text()))
		X[3]=str(_fromUtf8(self.lineEdit_4.text()))
		
		for i in range(len(X)):
			try:
				X[i]=int(X[i])
			except(ValueError,TypeError):
				if X[i] == 'b' or X[i] == 'B':
					X[i] = 'B'
					pass
				else:
					QMessageBox.information(self.iface.mainWindow(),"test", "%s" % (text), QMessageBox.Ok)
					#self.lineEdit.clear
					#self.lineEdit_2.clear
					#self.lineEdit_3.clear
					#self.lineEdit_4.clear
					#self.label.clear
					#self.treeView.reset
					#break
		print X
		C.apilar(X);
		Found.apilar(False)
		An, Con = Resolv(Fin, X, 'R')
		C.apilar(An);
		Found.apilar(Con)
		Bn, Con = Resolv(Fin, X, 'I')
		C.apilar(Bn);
		Found.apilar(Con)
		Cn, Con = Resolv(Fin, An, 'R')
		C.apilar(Cn);
		Found.apilar(Con)
		Dn, Con = Resolv(Fin, An, 'I')
		C.apilar(Dn);
		Found.apilar(Con)
		En, Con = Resolv(Fin, Bn, 'R')
		C.apilar(En);
		Found.apilar(Con)
		Fn, Con = Resolv(Fin, Bn, 'I')
		C.apilar(Fn);
		Found.apilar(Con)
		print C.items
		print Found.items
		print Found.items.index(True);
		

if __name__ == "__main__":
    import sys;
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

