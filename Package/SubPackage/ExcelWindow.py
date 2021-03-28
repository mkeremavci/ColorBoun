'''
ExcelWindow.py
Last Edit: 2020.04.15
'''

# GUI
from tkinter import *
from tkinter import messagebox
# Excel
import xlwt
from tempfile import TemporaryFile
# Others
import datetime

# ExcelWindow
class ExcelWindow():

	def __init__(self):
		# Creating Window
		self.window = Tk()
		self.window.title('Export to Excel')
		self.window.geometry('235x90+510+300')

		# Creating Button
		self.btn1 = Button(self.window, text="Export", height = 1, width = 10)
		self.btn1.place(x=65,y=60)

		# Creating Label
		self.lbl1 = Label(self.window, text="Solution/Material Name:")
		self.lbl1.place(x=20,y=10)

		# Creating Entry
		self.ent1 = Entry(self.window, width=20) #Given Saturation
		self.ent1.place(x=20,y=30)

		#XLSX
		self.date_text = None
		self.file_name = None
		self.sheet_text = None

	def get_file_name(self,file_name):
		# Date
		currentDT = datetime.datetime.now()
		if str(self.ent1.get()) == '':
			return
		if file_name == 'Main':
			self.file_text = 'Results/' + str(currentDT.year) + str(currentDT.month) + str(currentDT.day) + '_' +str(self.ent1.get()) + '.xls'
		elif file_name == 'Sub':
			self.file_text = 'Curves/' + str(currentDT.year) + str(currentDT.month) + str(currentDT.day) + '_' +str(self.ent1.get()) + '.xls'
		self.sheet_text = str(currentDT.hour) + str(currentDT.minute) + str(currentDT.second)

	def export_parameters(self,spars,rgbpars,conpars,sblank,rgbblank,units):
		#
		if self.sheet_text == None:
			return
		if len(spars) == 0:
			messagebox.showinfo('Error', 'Parameters not found')
			return
		#
		book = xlwt.Workbook()
		sheet1 = book.add_sheet(self.sheet_text,cell_overwrite_ok=True)
		style = xlwt.easyxf('font: bold 1')
		# Titles
		sheet1.write(0,0,'Saturation P.',style)
		sheet1.write(0,1,'RGB P.',style)
		sheet1.write(0,2,'Concentration',style)
		sheet1.write(0,3,'Sat.for Blank',style)
		sheet1.write(0,4,'RGB for Blank',style)
		sheet1.write(0,5,'Unit',style)
		# Data Insertion
		def insert_data(sheet,vals,loc):
			for i,e in enumerate(vals):
				sheet.write(i+1,loc,str(e))
		#
		insert_data(sheet1,spars,0)
		insert_data(sheet1,rgbpars,1)
		insert_data(sheet1,conpars,2)
		insert_data(sheet1,sblank,3)
		insert_data(sheet1,rgbblank,4)
		insert_data(sheet1,units,5)
		#
		book.save(self.file_text)
		book.save(TemporaryFile())

	def export_result(self,unknown,result,unit):
		#
		if self.sheet_text == None:
			return
		if result == None:
			messagebox.showinfo('Error', 'Result not found')
			return
		#
		book = xlwt.Workbook()
		sheet1 = book.add_sheet(self.sheet_text,cell_overwrite_ok=True)
		style = xlwt.easyxf('font: bold 1')
		# Titles
		sheet1.write(0,0,'Parameter of Unk.',style)
		sheet1.write(0,1,'Concentration',style)
		sheet1.write(0,2,'Unit',style)
		# Data Insertion
		sheet1.write(1,0,round(unknown,5),style)
		sheet1.write(1,1,round(result,5),style)
		sheet1.write(1,2,unit,style)
		#
		book.save(self.file_text)
		book.save(TemporaryFile())
