'''
App.py
Last Edit: 2020.04.15
'''

# GUI
from tkinter import *
#
from Package.SubPackage import MainWindow
from Package.SubPackage import SubWindow
from Package.SubPackage import ExcelWindow

# App
class App():

	def __init__(self):
		# Main Window
		self.mw = MainWindow.MainWindow()
		self.mainfuncs()

		# Other Windows
		self.sw = None
		self.ex = None

		# Parameters
		self.spars = []
		self.rgbpars = []
		self.conpars = []
		self.sblank = []
		self.rgbblank = []
		self.units = []
		self.unit = ''

		# Mode
		self.mode = None

	def hvs_mode(self):
		self.mode = 'HVS'
		#
		temppars = []
		tempblank = []
		tempcons = []
		for i in range(len(self.spars)):
			if self.spars[i] == 'not given':
				continue
			else:
				temppars.append(self.spars[i])
				tempcons.append(self.conpars[i])
		for i in range(len(self.sblank)):
			if self.sblank[i] == 'not given':
				continue
			else:
				tempblank.append(self.sblank[i])
		#
		self.mw.print_main_param(self.spars,self.conpars)
		self.mw.calculate_unknown(self.mw.s,tempblank)
		self.mw.regression_equation(temppars,tempcons)
		self.mw.print_regression()

	def rgb_mode(self):
		self.mode = 'RGB'
		#
		temppars = []
		tempblank = []
		tempcons = []
		for i in range(len(self.spars)):
			if self.rgbpars[i] == 'not given':
				continue
			else:
				temppars.append(self.rgbpars[i])
				tempcons.append(self.conpars[i])
		for i in range(len(self.sblank)):
			if self.rgbblank[i] == 'not given':
				continue
			else:
				tempblank.append(self.rgbblank[i])
		#
		self.mw.print_main_param(self.rgbpars,self.conpars)
		if self.mw.s != None:
			self.mw.calculate_unknown(self.mw.avrrgb,tempblank)
		self.mw.regression_equation(temppars,tempcons)
		self.mw.print_regression()

	def result(self):
		if self.mw.s != None:
			self.mw.solution(self.mw.unknown,self.unit)
		else:
			return

	def show_graph(self):
		if self.mw.result == None:
			return
		if self.mode == 'HVS':
			self.mw.display_graph(self.spars,self.conpars)
		elif self.mode == 'RGB':
			self.mw.display_graph(self.rgbpars,self.conpars)

	def change_sub_view(self):
		if self.sw != None:
			try:
				self.sw.set_labels(self.mw)
				self.sw.set_color_area(self.mw)
			except:
				self.sw = None

	def click_mouse(self,event):
		self.mw.x, self.mw.y = event.x, event.y
		#
		self.mw.botx, self.mw.boty = self.mw.x, self.mw.y
		self.mw.canvas1.coords(self.mw.rect, self.mw.x, self.mw.y, self.mw.botx, self.mw.boty)
		#
		self.mw.get_pixel_value(event.x,event.y)
		self.mw.get_hex()
		self.mw.print_pixel_values()
		self.change_sub_view()
		if self.mode == 'HVS':
			self.hvs_mode()
		elif self.mode == 'RGB':
			self.rgb_mode()

	def motion_mouse(self,event):
		self.mw.botx, self.mw.boty = event.x, event.y
		self.mw.canvas1.coords(self.mw.rect, self.mw.x, self.mw.y, self.mw.botx, self.mw.boty)

	def roi_color(self):
		self.mw.get_pixel_area(self.mw.x,self.mw.y,self.mw.botx,self.mw.boty)
		self.mw.get_hex()
		self.mw.print_pixel_values()
		self.change_sub_view()
		if self.mode == 'HVS':
			self.hvs_mode()
		elif self.mode == 'RGB':
			self.rgb_mode()

	def print_current_parameters(self):
		#
		def print_list(obj,vals):
			obj.configure(state='normal')
			obj.delete('1.0',END)
			for i in range(len(vals)):
				try:
					temp = str(round(vals[i],5)) + '\n'
				except:
					temp = str(vals[i]) + '\n'
				obj.insert(END,temp)
			obj.configure(state='disabled')
		#
		print_list(self.sw.txt1,self.spars)
		print_list(self.sw.txt2,self.rgbpars)
		print_list(self.sw.txt3,self.conpars)

	def color_identificator(self):
		self.sw = SubWindow.SubWindow(self.mw)
		self.print_current_parameters()
		self.subfuncs()
		self.sw.window.mainloop()

	def add_entries(self):
		self.sw.add_given(self.spars,self.rgbpars,self.conpars,self.sblank,self.rgbblank,self.units)
		self.unit = self.units[0]

	def add_calculated(self):
		self.sw.add_calculated(self.spars,self.rgbpars,self.conpars,self.sblank,self.rgbblank,self.units,self.mw.s,self.mw.avrrgb)
		self.unit = self.units[0]

	def remove_one(self):
		self.sw.remove_one(self.spars,self.rgbpars,self.conpars,self.sblank,self.rgbblank,self.units)
		if len(self.spars) == 0:
			self.unit = ''

	def remove_all(self):
		self.sw.remove_all(self.spars,self.rgbpars,self.conpars,self.sblank,self.rgbblank,self.units)
		self.unit = ''

	def export_main(self):
		self.ew.get_file_name('Main')
		self.ew.export_result(self.mw.unknown,self.mw.result,self.unit)
		if self.ew.sheet_text == None:
			return
		self.ew.window.destroy()

	def export_from_main(self):
		self.ew = ExcelWindow.ExcelWindow()
		self.ew.btn1.configure(command = self.export_main)
		self.ew.window.mainloop()

	def export_sub(self):
		self.ew.get_file_name('Sub')
		self.ew.export_parameters(self.spars,self.rgbpars,self.conpars,self.sblank,self.rgbblank,self.units)
		if self.ew.sheet_text == None:
			return
		self.ew.window.destroy()

	def export_from_sub(self):
		self.ew = ExcelWindow.ExcelWindow()
		self.ew.btn1.configure(command = self.export_sub)
		self.ew.window.mainloop()

	def import_sub(self):
		self.spars, self.rgbpars, self.conpars, self.sblank, self.rgbblank, self.units = [],[],[],[],[],[]
		self.sw.import_excel(self.spars,self.rgbpars,self.conpars,self.sblank,self.rgbblank,self.units)
		if len(self.spars) != 0:
			self.unit = self.units[0]
		def print_list(obj,vals):
			obj.configure(state='normal')
			obj.delete('1.0',END)
			for i in range(len(vals)):
				try:
					temp = str(round(vals[i],5)) + '\n'
				except:
					temp = str(vals[i]) + '\n'
				obj.insert(END,temp)
			obj.configure(state='disabled')
		print_list(self.sw.txt1,self.spars)
		print_list(self.sw.txt2,self.rgbpars)
		print_list(self.sw.txt3,self.conpars)

	def add_image(self):
		self.mw.add_image()
		self.mw.rect = None
		self.mw.rect = self.mw.canvas1.create_rectangle(self.mw.x, self.mw.y, self.mw.x, self.mw.y, dash=(2,2), fill='', outline='white')
		self.mw.canvas1.bind('<B1-Motion>',self.motion_mouse)

	def add_blur(self):
		self.mw.add_blur()
		self.mw.rect = None
		self.mw.rect = self.mw.canvas1.create_rectangle(self.mw.x, self.mw.y, self.mw.x, self.mw.y, dash=(2,2), fill='', outline='white')
		self.mw.canvas1.bind('<B1-Motion>',self.motion_mouse)		

	def mainfuncs(self):
		# Mouse Click and Rectangle
		self.mw.canvas1.bind('<Button-1>', self.click_mouse)
		self.mw.rect = self.mw.canvas1.create_rectangle(self.mw.x, self.mw.y, self.mw.x, self.mw.y, dash=(2,2), fill='', outline='white')
		self.mw.canvas1.bind('<B1-Motion>',self.motion_mouse)
		# Add Image
		self.mw.btn1.configure(command = self.add_image)
		# Add Blur
		self.mw.btn9.configure(command = self.add_blur)
		# Exit
		self.mw.btn4.configure(command = self.mw.window.quit)
		# HVS Mode
		self.mw.btn5.configure(command = self.hvs_mode)
		# RGB Mode
		self.mw.btn6.configure(command = self.rgb_mode)
		# Result
		self.mw.btn8.configure(command = self.result)
		# Show Graph
		self.mw.btn7.configure(command = self.show_graph)
		#
		self.mw.btn2.configure(command = self.color_identificator)
		# Export to Excel
		self.mw.btn3.configure(command = self.export_from_main)
		# ROI Color
		self.mw.btn10.configure(command = self.roi_color)

	def subfuncs(self):
		# Add with Given Entries
		self.sw.btn6.configure(command = self.add_entries)
		# Remove One
		self.sw.btn3.configure(command = self.remove_one)
		# Remove All
		self.sw.btn4.configure(command = self.remove_all)
		# Export to Excel
		self.sw.btn2.configure(command = self.export_from_sub)
		# Calculate and Add
		self.sw.btn7.configure(command = self.add_calculated)
		# Import Excel
		self.sw.btn1.configure(command = self.import_sub)

	def start_system(self):
		self.mw.window.mainloop()
