# -*- coding: utf-8 -*-
import random
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QStringListModel
import numpy as np
import csv

class Qtrandom:
    def __init__(self):
        qfile = QFile("Qtrandom.ui")
        qfile.open(QFile.ReadOnly)
        self.ui = QUiLoader().load(qfile)
        qfile.close()
        self.ui.ClassButton_3.clicked.connect(self.All_class)
        self.ui.SampleButton_1.clicked.connect(self.random_key_in)
        self.ui.SaveButton_2.clicked.connect(self.save_CSV)
        self.ui.ExitButton_4.clicked.connect(self.close)
        self.class_info = []
        self.sample_number=[]
        self.search_no = ''
        self.output_class()
        self.word = self.ui.classlineEdit.text()

    def output_class(self):
        with open('VIP.csv', newline='',encoding='utf-8') as csvfile:
            rows = csv.reader(csvfile, delimiter=',')
            for row in rows:
                self.class_info.append(row)
            self.word=str(len(self.class_info))
            self.ui.classlineEdit.setPlaceholderText(self.word)
            self.ui.lineEdit.setPlaceholderText("0")
            self.show_list(self.sample_number)

    def All_class(self): #讀取全部的學生名單，存在列表裡
        self.class_info = []
        with open('VIP.csv', newline='',encoding='utf-8') as csvfile:
            rows = csv.reader(csvfile, delimiter=',')
            for row in rows:
                self.class_info.append(row)
        self.show_list(self.class_info)

#-------------------------------------------------------
    def random_key_in(self): #key隨機數字 samplelineEdit.
        if int(self.ui.lineEdit.text())<1 or int(self.ui.lineEdit.text()) > len(self.class_info):
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
        L = QStringListModel()
        L.setStringList(list)
        self.ui.listView.setModel(L)

    def close(self):#關閉程式
        self.ui.close()


app = QApplication()
stats = Qtrandom()
stats.ui.show()
app.exec_()