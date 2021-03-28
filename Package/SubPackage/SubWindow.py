'''
SubWindow.py
Last Edit: 2020.04.15
'''

# GUI
from tkinter import *
from tkinter import filedialog
# Others
import math
import xlrd
from xlrd import open_workbook

# SubWindow
class SubWindow():

	def __init__(self,mw):
		# Creating Window
		self.window = Tk()
		self.window.title('Color Identificator')
		self.window.geometry('480x480+800+110')

		# Creating Buttons
		self.btn1 = Button(self.window, text="Select an Existing Curve", height = 2, width = 20)
		self.btn1.place(x=50,y=430)
		self.btn2 = Button(self.window, text="Export the Curve", height = 2, width = 20)
		self.btn2.place(x=250,y=430)
		self.btn3 = Button(self.window, text="Remove Last Item", height = 1, width = 20) #Remove Sat.
		self.btn3.place(x=25,y=240)
		self.btn4 = Button(self.window, text="Remove All Items", height = 1, width = 20) #Remove RGB
		self.btn4.place(x=225,y=240)
		self.btn6 = Button(self.window, text="Add", height = 1, width = 20) #Add according to the user's input
		self.btn6.place(x=25,y=215)
		self.btn7 = Button(self.window, text="Calculate and Add", height = 1, width = 20) #Add according to selected area/pixel
		self.btn7.place(x=225,y=215)

		# Creating Image Canvas
		self.canvas1 = Canvas(self.window, width = 250, height = 60) #Color Sample
		self.canvas1.place(x=120,y=40)
		self.set_color_area(mw)

		# Creating Text Boxes
		self.txt1 = Text(self.window, bg = '#A99B98', height=9, width=20) #S.Parameters
		self.txt1.configure(state='disabled')
		self.txt1.place(x=20,y=295)
		self.txt2 = Text(self.window, bg = '#A99B98', height=9, width=20) #RGB.Parameters
		self.txt2.configure(state='disabled')
		self.txt2.place(x=170,y=295)
		self.txt3 = Text(self.window, bg = '#A99B98', height=9, width=20) #Cons.
		self.txt3.configure(state='disabled')
		self.txt3.place(x=320,y=295)

		# Creating Labels
		self.lbl1 = Label(self.window, text='X location: ') #Top
		self.lbl1.place(x=20,y=10)
		self.lbl2 = Label(self.window, text='Y location: ')
		self.lbl2.place(x=170,y=10)
		self.lbl3 = Label(self.window, text='Sat.: ') #Top Left
		self.lbl3.place(x=20,y=30)
		self.lbl4 = Label(self.window, text='R: ')
		self.lbl4.place(x=20,y=50)
		self.lbl5 = Label(self.window, text='G: ')
		self.lbl5.place(x=20,y=70)
		self.lbl6 = Label(self.window, text='B: ')
		self.lbl6.place(x=20,y=90)
		self.lbl7 = Label(self.window, text='Average RGB: ')
		self.lbl7.place(x=320,y=10)
		self.lbl9 = Label(self.window, text="Measured Saturation:")
		self.lbl9.place(x=20,y=110)
		self.lbl10 = Label(self.window, text="Measured RGB:")
		self.lbl10.place(x=170,y=110)
		self.lbl11 = Label(self.window, text="Saturation for Blank:")
		self.lbl11.place(x=20,y=160)
		self.lbl12 = Label(self.window, text="RGB for Blank:")
		self.lbl12.place(x=170,y=160)
		self.lbl13 = Label(self.window, text="Sample Concentration:")
		self.lbl13.place(x=320,y=110)
		self.lbl14 = Label(self.window, text="Saturation Parameters:") #Top Right
		self.lbl14.place(x=20,y=270)
		self.lbl15 = Label(self.window, text="RGB Parameters:")
		self.lbl15.place(x=170,y=270)
		self.lbl16 = Label(self.window, text="Concentration:")
		self.lbl16.place(x=320,y=270)
		self.lbl17 = Label(self.window, text="Unit:") #Right
		self.lbl17.place(x=320,y=160)
		self.set_labels(mw)

		# Creating Entries
		vcmd = (self.window.register(self.validate),'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

		self.ent1 = Entry(self.window, width=10) #Given Saturation
		self.ent1.place(x=20,y=135)
		self.ent2 = Entry(self.window, width=10) #Given RGB
		self.ent2.place(x=170,y=135)
		self.ent3 = Entry(self.window, width=10) #Sample Concentration
		self.ent3.place(x=320,y=135)
		self.ent4 = Entry(self.window, width=10) #Saturation for Blank
		self.ent4.place(x=20,y=185)
		self.ent5 = Entry(self.window, width=10) #RGB for Blank
		self.ent5.place(x=170,y=185)
		self.ent6 = Entry(self.window, width=10) #Unit
		self.ent6.place(x=320,y=185)

		# self.ent1 = Entry(self.window, width=10, validate = 'key', validatecommand = vcmd) #Given Saturation
		# self.ent1.place(x=220,y=135)
		# self.ent2 = Entry(self.window, width=10, validate = 'key', validatecommand = vcmd) #Given RGB
		# self.ent2.place(x=220,y=185)
		# self.ent3 = Entry(self.window, width=10, validate = 'key', validatecommand = vcmd) #Sample Concentration
		# self.ent3.place(x=220,y=235)
		# self.ent4 = Entry(self.window, width=10, validate = 'key', validatecommand = vcmd) #Saturation for Blank
		# self.ent4.place(x=20,y=235)
		# self.ent5 = Entry(self.window, width=10, validate = 'key', validatecommand = vcmd) #RGB for Blank
		# self.ent5.place(x=20,y=285)
		# self.ent6 = Entry(self.window, width=10) #Unit
		# self.ent6.place(x=420,y=235)

	def validate(self, action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
		if value_if_allowed:
			try:
				float(value_if_allowed)
				return True
			except ValueError:
				return False
		else:
			return False

	def set_labels(self,obj):
		if obj.x == 0:
			return
		#
		def get_label(name,val):
			return name + str(round(val,3))
		#
		self.lbl1.configure(text = get_label('X location: ',obj.p_x))
		self.lbl2.configure(text = get_label('Y location: ',obj.p_y))
		self.lbl3.configure(text = get_label('Sat.: ',obj.s))
		self.lbl4.configure(text = get_label('R: ',obj.rgb[0]))
		self.lbl5.configure(text = get_label('G: ',obj.rgb[1]))
		self.lbl6.configure(text = get_label('B: ',obj.rgb[2]))
		self.lbl7.configure(text = get_label('Average RGB: ',obj.avrrgb))

	def set_color_area(self,obj):
		if obj.x == 0:
			return
		self.canvas1.configure(bg = obj.hex)

	def remove_one(self,spars,rgbpars,conpars,sblank,rgbblank,units):
		def print_param_list(obj,onelist):
			obj.configure(state='normal')
			obj.delete('1.0',END)
			for i in range(len(onelist)):
				try:
					temp = str(round(onelist[i],5)) + '\n'
				except:
					temp = str(onelist[i]) + '\n'
				obj.insert(END,temp)
			obj.configure(state='disabled')

		#
		if len(spars) > 0:
			spars.pop()
			rgbpars.pop()
			conpars.pop()
			sblank.pop()
			rgbblank.pop()
			units.pop()
			print_param_list(self.txt1,spars)
			print_param_list(self.txt2,rgbpars)
			print_param_list(self.txt3,conpars)

	def remove_all(self,spars,rgbpars,conpars,sblank,rgbblank,units):
		def remove_item(obj):
			obj.configure(state='normal')
			obj.delete('1.0',END)
			obj.configure(state='disabled')
		#
		if len(spars) > 0:
			remove_item(self.txt1)
			remove_item(self.txt2)
			remove_item(self.txt3)
			for i in range(len(spars)):
				spars.pop()
				rgbpars.pop()
				conpars.pop()
				sblank.pop()
				rgbblank.pop()
				units.pop()

	def add_given(self,spars,rgbpars,conpars,sblank,rgbblank,units):
		#
		def control_val(val1,val2,type_val):
			if type_val == 'number':
				try:
					return math.log10(float(val1)/float(val2)), float(val1)
				except:
					return 'not given', 'not given'
			elif type_val == 'string':
				try:
					return float(val1), str(val2)
				except:
					return 'error', 'error'
		#
		spar, sbla = control_val(self.ent4.get(),self.ent1.get(),'number')
		rgbpar, rgbbla = control_val(self.ent5.get(),self.ent2.get(),'number')
		conpar, un = control_val(self.ent3.get(),self.ent6.get(),'string')
		#
		if un == 'error' or un == '':
			self.ent1.delete(0,END)
			self.ent2.delete(0,END)
			self.ent3.delete(0,END)
			return
		else:
			spars.append(spar)
			sblank.append(sbla)
			rgbpars.append(rgbpar)
			rgbblank.append(rgbbla)
			conpars.append(conpar)
			units.append(un)
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
		print_list(self.txt1,spars)
		print_list(self.txt2,rgbpars)
		print_list(self.txt3,conpars)
		#
		self.ent1.delete(0,END)
		self.ent2.delete(0,END)
		self.ent3.delete(0,END)

	def add_calculated(self,spars,rgbpars,conpars,sblank,rgbblank,units,s,avrrgb):
		#
		def control_val(val1,val2):
			try:
				return math.log10(float(val1)/val2), float(val1)
			except:
				return 'not given', 'not given'
		#
		spar, sbla = control_val(self.ent4.get(),s)
		rgbpar, rgbbla = control_val(self.ent5.get(),avrrgb)
		try:
			conpar, un = float(self.ent3.get()), self.ent6.get()
		except:
			conpar, un = 'error', 'error'
		#
		if un == 'error' or un == '':
			self.ent3.delete(0,END)
			return
		else:
			spars.append(spar)
			sblank.append(sbla)
			rgbpars.append(rgbpar)
			rgbblank.append(rgbbla)
			conpars.append(conpar)
			units.append(un)
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
		print_list(self.txt1,spars)
		print_list(self.txt2,rgbpars)
		print_list(self.txt3,conpars)
		#
		self.ent1.delete(0,END)
		self.ent2.delete(0,END)
		self.ent3.delete(0,END)

	def import_excel(self,spars,rgbpars,conpars,sblank,rgbblank,units):
		exfile = filedialog.askopenfilename(filetypes = [("Excel File","*.xls *.xlsx")])
		if len(exfile) == 0:
			return
		book = open_workbook(exfile)
		sheet1 = book.sheet_by_index(0)
		for i in range(1,sheet1.nrows):
			try:
				spars.append(float(sheet1.cell(i,0).value))
			except:
				spars.append(sheet1.cell(i,0).value)
			try:
				rgbpars.append(float(sheet1.cell(i,1).value))
			except:
				rgbpars.append(sheet1.cell(i,1).value)
			try:
				conpars.append(float(sheet1.cell(i,2).value))
			except:
				conpars.append(sheet1.cell(i,2).value)
			try:
				sblank.append(float(sheet1.cell(i,3).value))
			except:
				sblank.append(sheet1.cell(i,3).value)
			try:
				rgbblank.append(float(sheet1.cell(i,4).value))
			except:
				rgbblank.append(sheet1.cell(i,4).value)
			units.append(sheet1.cell(i,5).value)
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
		print_list(self.txt1,spars)
		print_list(self.txt2,rgbpars)
		print_list(self.txt3,conpars)
