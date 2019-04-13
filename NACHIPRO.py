from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog,QLabel
from PyQt5.uic import loadUi




class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(910, 480)
        Dialog.setStyleSheet("background-image: url(:/newPrefix/morse1 - Copy.png);")
        Dialog.setProperty("pixmap", QtGui.QPixmap(":/newPrefix/morse1.jpg"))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 20, 751, 161))
        font = QtGui.QFont()
        font.setFamily("Niagara Engraved")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton1 = QtWidgets.QPushButton(Dialog)
        self.pushButton1.setGeometry(QtCore.QRect(310, 270, 301, 91))
        font = QtGui.QFont()
        font.setFamily("Niagara Solid")
        font.setPointSize(20)
        self.pushButton1.setFont(font)
        self.pushButton1.setAutoFillBackground(False)
        self.pushButton1.setStyleSheet("background-image: url(:/newPrefix/push.png);")
        self.pushButton1.setObjectName("pushButton1")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">WELCOME TO MORSECODE TRANSLATOR</span></p></body></html>"))
        self.pushButton1.setText(_translate("Dialog", "LET\'S GET STARTED"))
        self.pushButton1.clicked.connect(self.on_open)
    
    def on_open(self):
        self.newobject=openwindow()
        self.newobject.show()


class openwindow(QDialog):
    def __init__(self):
        super(openwindow,self).__init__()
        
        loadUi('traii.ui',self).show()
        self.setWindowTitle('project gui1')
        self.pushButton.clicked.connect(self.databaseconnect)
        
    def databaseconnect(self):
        
        conn=psycopg2.connect(database="mydb",user="postgres",password="1234",host="localhost",port="5432")
        cur=conn.cursor()
        
        conn.commit()

        cur.execute("SELECT * from project")
        rows=cur.fetchall()
        
        l=[]
        
        str1=self.lineEdit.text()
        l=str1.split()
        

        l1=[]
        for i in range(len(l)):
            for row in rows:
                if(row[1]==l[i]):
                    print(row[0])
                    l1.append(row[0])
                    
    


        str2 = ''.join(l1)
        
        self.label_3.setText(str2)

        








	
    

import source
import xy

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
