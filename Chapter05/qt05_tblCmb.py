# -*- coding: utf-8 -*- 

'''
    【简介】
	PyQT5中 单元格里面放控件 
    
'''

import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem, QAbstractItemView ,QComboBox )

class Table(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle("QTableWidget 例子")
		self.resize(430,300);
		conLayout = QHBoxLayout()
		tableWidget = QTableWidget()
		tableWidget.setRowCount(4)
		tableWidget.setColumnCount(3)
		conLayout.addWidget(tableWidget )
		
		tableWidget.setHorizontalHeaderLabels(['姓名','性别','体重(kg)'])  
		  
		newItem = QTableWidgetItem("张三")  
		tableWidget.setItem(0, 0, newItem)  
		  
		comBox = QComboBox()
		comBox.addItem("男")
		comBox.addItem("女")
		tableWidget.setCellWidget(0,1,comBox)
		
		newItem = QTableWidgetItem("160")  
		tableWidget.setItem(0, 2, newItem)   
				
		self.setLayout(conLayout)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	example = Table()  
	example.show()   
	sys.exit(app.exec_())
