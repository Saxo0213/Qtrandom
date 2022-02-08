# -*- coding: utf-8 -*-
import random
from PySide2.QtWidgets import QApplication, QMessageBox,QFileDialog
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QStringListModel
import csv

class Qtrandom:
    def __init__(self):
        qfile = QFile("Qtrandom.ui")
        qfile.open(QFile.ReadOnly)
        self.ui = QUiLoader().load(qfile)
        qfile.close()
        self.ui.openButton_1.clicked.connect(self.fileopen)
        self.ui.ClassButton_3.clicked.connect(self.All_class)
        self.ui.SampleButton_1.clicked.connect(self.random_key_in)
        self.ui.SaveButton_2.clicked.connect(self.save_CSV)
        self.ui.ExitButton_4.clicked.connect(self.close)
        self.sample_number=[]
        self.ui.lineEdit.setText("0")
        self.search_no = ''
        self.word = "0"

    def fileopen(self):
        filename, filetype =QFileDialog.getOpenFileName(None)
        file=filename
        if file == "":
            return
        self.class_info=[]
        with open(file, newline='',encoding='utf-8') as csvfile:
            rows = csv.reader(csvfile, delimiter=',')
            print(rows)
            for row in rows:
                self.class_info.append(row)
            self.word=str(len(self.class_info))
            self.ui.label.setText("班級人數:{}".format(self.word))
            self.ui.lineEdit.setText("0")
            self.show_list(self.class_info)

    def All_class(self): #讀取全部的學生名單，存在列表裡
        self.show_list(self.class_info)

#-------------------------------------------------------
    def random_key_in(self): #key隨機數字 samplelineEdit.
        if int(self.ui.lineEdit.text())<1:
            msgBox = QMessageBox(QMessageBox.NoIcon, '提醒','沒有輸入抽樣人數')
            msgBox.exec()
            return
        if int(self.ui.lineEdit.text()) > len(self.class_info):
            msgBox = QMessageBox(QMessageBox.NoIcon, '提醒','抽樣人數太多')
            msgBox.exec()
            return
        self.search_no = int(self.ui.lineEdit.text())
        if self.search_no >= 1:
            self.sample_number=random.sample(
                self.class_info,
                k=self.search_no
                )
            self.show_list(self.sample_number)

# # -------------------------------------------------------
    def save_CSV(self):#把self.sample_number存成CSV檔案
        with open('output.csv', 'w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self.sample_number)
#
    def show_list(self,list):#顯示在螢幕
        pf=[]
        for l in list:
            pf.append(",".join(l))
        self.qList = QStringListModel()
        self.qList.setStringList(pf)
        self.ui.listView.setModel(self.qList)

    def close(self):#關閉程式
        self.ui.close()


app = QApplication()
stats = Qtrandom()
stats.ui.show()
app.exec_()