import random
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QStringListModel
import numpy as np
import csv




class Qtrandom:
    def __init__(self):
        super(Qtrandom, self).__init__()
        # 设置UI文件只读
        qfile = QFile("stats/Qtrandom.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        # 设置UI文件只读
        # 加载UI文件
        self.ui = QUiLoader().load(qfile)
        self.ui.ClassButton_3.clicked.connect(self.All_class)
        self.ui.SampleButton_1.clicked.connect(self.random_key_in)
        self.ui.SaveButton_2.clicked.connect(self.save_CSV)
        self.ui.ExitButton_4.clicked.connect(self.close)
        # 初始化參數
        self.output_class()
        self.word = self.ui.classlineEdit.text()
        self.class_info = []
        self.search_no = ''
    def output_class(self):
        #open CSV file and read
        #enumerate 計算列舉出來import csv
        #計算最大值 max，不要最大值
        self.word = self.ui.classlineEdit.text()
        with open('VIP.csv', newline='') as csvfile:
            # 以冒號分隔欄位，讀取檔案內容
            rows = csv.reader(csvfile, delimiter=':')

            # for row in rows:
            #     print(row)
            prices = []  # int 無法迴圈，使用list裝入資料，然後在操作
            for idx, row in enumerate(rows):
                prices.append(int(idx))
            self.word=str(max(prices))
        self.set_placeholdertext() #呼叫底下的set_placeholdertext的方法!

    def set_placeholdertext(self): #取出文字
        self.ui.classlineEdit.setPlaceholderText(self.word)

    def All_class(self): #讀取全部的學生名單，存在列表裡
        self.class_info = []
        with open('VIP.csv', newline='') as csvfile:
            # 以冒號分隔欄位，讀取檔案內容

            rows = csv.reader(csvfile, delimiter=':')
            for row in rows:
                self.class_info.extend(row)
        self.show_list()

    def show_list(self):#顯示在螢幕
        qlist = QStringListModel()
        qlist.setStringList(self.class_info)
        self.ui.listView1.setModel(qlist)
#-------------------------------------------------------
    def random_key_in(self): #key隨機數字 samplelineEdit.
        self.search_no = int(self.ui.samplelineEdit.text())
        self.random_search()
    def random_search(self):  #隨機數字
        self.sample_number=random.sample(self.class_info,self.search_no)
        self.show_random_list()

    def show_random_list(self):#顯示在螢幕
        qlist = QStringListModel()
        qlist.setStringList(self.sample_number)
        self.ui.listView1.setModel(qlist)
# # -------------------------------------------------------
    def save_CSV(self):#把self.sample_number存成CSV檔案

        with open('output.csv', 'w', newline=self.sample_number) as csvfile:
                writer = csv.writer(csvfile)

                # 寫入二維表格
                writer.writerows(self.sample_number)
#
    def close(self):#關閉程式
        self.ui.close()


app = QApplication([])
stats = Qtrandom()
stats.ui.show()
app.exec_()