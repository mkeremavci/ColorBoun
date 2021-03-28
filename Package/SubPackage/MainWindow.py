'''
MainWindow.py
Last Edit: 2020.04.15
'''

# GUI
from tkinter import *
from tkinter import filedialog
# Image
from PIL import Image, ImageTk, ImageFilter
# Graph
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
# Others
import math

# MainWindow
class MainWindow():

	def __init__(self):
		# Creating Window
		self.window = Tk()
		self.window.title('ColorBoun - NRG')
		self.window.geometry('800x700')

		# Creating Buttons
		self.btn1 = Button(self.window, text="Pick an Image", height = 2, width = 18)
		self.btn1.place(x=30,y=10)
		self.btn2 = Button(self.window, text="Color Identificator", height = 2, width = 18) #SubWindow
		self.btn2.place(x=220,y=10)
		self.btn3 = Button(self.window, text="Export as Excel", height = 2, width = 18)
		self.btn3.place(x=410,y=10)
		self.btn4 = Button(self.window, text="Exit", height = 2, width = 18)
		self.btn4.place(x=600,y=10)
		self.btn5 = Button(self.window, text="Process on HVS", height = 1, width = 15)
		self.btn5.place(x=480,y=220)
		self.btn6 = Button(self.window, text="Process on RGB", height = 1, width = 15)
		self.btn6.place(x=640,y=220)
		self.btn7 = Button(self.window, text="Show Graph", height = 1, width = 15)
		self.btn7.place(x=640,y=620)
		self.btn8 = Button(self.window, text="Result", height = 1, width = 15)
		self.btn8.place(x=480,y=620)
		self.btn9 = Button(self.window, text="Add Blur", height = 1, width = 10)
		self.btn9.place(x=690,y=70)
		self.btn10 = Button(self.window, text="ROI", height = 1, width = 10)
		self.btn10.place(x=610,y=110)

		# Creating Image and Graph Canvas
		self.canvas1 = Canvas(self.window, width = 440, height = 330) #Image
		self.canvas1.place(x=20,y=50)

		# Creating Text Boxes
		self.txt1 = Text(self.window, bg = '#A99B98', height=1, width=5) #Sat.
		self.txt1.configure(state='disabled')
		self.txt1.place(x=560,y=110)
		self.txt2 = Text(self.window, bg = '#A99B98', height=1, width=5) #R
		self.txt2.configure(state='disabled')
		self.txt2.place(x=500,y=150)
		self.txt3 = Text(self.window, bg = '#A99B98', height=1, width=5) #G
		self.txt3.configure(state='disabled')
		self.txt3.place(x=580,y=150)
		self.txt4 = Text(self.window, bg = '#A99B98', height=1, width=5) #B
		self.txt4.configure(state='disabled')
		self.txt4.place(x=660,y=150)
		self.txt5 = Text(self.window, bg = '#A99B98', height=1, width=10) #Avg.RGB
		self.txt5.configure(state='disabled')
		self.txt5.place(x=580,y=190)
		self.txt6 = Text(self.window, bg = '#A99B98', height=8, width=16) #Parameters
		self.txt6.configure(state='disabled')
		self.txt6.place(x=480,y=270)
		self.txt7 = Text(self.window, bg = '#A99B98', height=8, width=16) #Cons
		self.txt7.configure(state='disabled')
		self.txt7.place(x=640,y=270)
		self.txt8 = Text(self.window, bg = '#A99B98', height=1, width=16) #Color Parameter of Unkwn
		self.txt8.configure(state='disabled')
		self.txt8.place(x=610,y=390)
		self.txt9 = Text(self.window, bg = '#A99B98', height=1, width=12) #Coeff. x
		self.txt9.configure(state='disabled')
		self.txt9.place(x=530,y=460)
		self.txt11 = Text(self.window, bg = '#A99B98', height=1, width=12) #Constant
		self.txt11.configure(state='disabled')
		self.txt11.place(x=640,y=460)
		self.txt12 = Text(self.window, bg = '#A99B98', height=1, width=20) #Cons. of Unkwn
		self.txt12.configure(state='disabled')
		self.txt12.place(x=480,y=530)
		self.txt13 = Text(self.window, bg = '#A99B98', height=1, width=20) #Unit
		self.txt13.configure(state='disabled')
		self.txt13.place(x=480,y=590)

		# Creating Labels
		self.lbl1 = Label(self.window, text="Gaussian Blur:") #Top Right
		self.lbl1.place(x=480,y=70)
		self.lbl2 = Label(self.window, text="Saturation:")
		self.lbl2.place(x=480,y=110)
		self.lbl3 = Label(self.window, text="R:")
		self.lbl3.place(x=480,y=150)
		self.lbl4 = Label(self.window, text="G:")
		self.lbl4.place(x=560,y=150)
		self.lbl5 = Label(self.window, text="B:")
		self.lbl5.place(x=640,y=150)
		self.lbl6 = Label(self.window, text="Average RGB:")
		self.lbl6.place(x=480,y=190)
		self.lbl7 = Label(self.window, text="Parameters:") #Mid Right
		self.lbl7.place(x=480,y=245)
		self.lbl8 = Label(self.window, text="Concentration:")
		self.lbl8.place(x=640,y=245)
		self.lbl9 = Label(self.window, text="Color of Unknown:")
		self.lbl9.place(x=480,y=390)
		self.lbl10 = Label(self.window, text="Regression Equation:") #Bottom Right
		self.lbl10.place(x=480,y=430)
		self.lbl11 = Label(self.window, text="y =")
		self.lbl11.place(x=480,y=460)
		self.lbl12 = Label(self.window, text="x")
		self.lbl12.place(x=620,y=460)
		self.lbl13 = Label(self.window, text="Concentration of Unknown:")
		self.lbl13.place(x=480,y=500)
		self.lbl14 = Label(self.window, text="Concentration Unit:")
		self.lbl14.place(x=480,y=560)

		# Creating Scales
		self.scale1 = Scale(self.window, from_=0, to=12, orient=HORIZONTAL) #Determine Gaussian Blur
		self.scale1.place(x=580,y=50)

		# Default Image and its Parameters
		self.im = Image.open("Package/bounlogo.jpg")
		self.origin = self.im # Original Image
		self.px = self.im.load()
		self.imsize = self.im.size
		photo = self.im.resize((440, 330), Image.ANTIALIAS)
		photo = ImageTk.PhotoImage(photo)
		self.canvas1.image = photo
		self.canvas1.create_image(3,3,anchor='nw',image=photo)

		# Pixel Parameters
		self.s = None
		self.rgb = [None,None,None]
		self.avrrgb = None
		self.hex = None
		self.unknown = None

		# Regression Parameters 'y = a + b*x'
		self.a, self.b = None, None
		self.result = None
		# self.display_graph([1,2,3,4],[1,2,3,4])

		# Mouse Location
		self.x, self.y = 0, 0
		self.botx, self.boty = 0,0
		self.p_x, self.p_y = None, None
		self.p_botx, self.p_boty = None, None
		self.rect = None

	def add_image(self):
		imfile = filedialog.askopenfilename(filetypes = [("Image File","*.jpeg *.png *.tiff *.jpg")])
		self.im = Image.open(imfile)
		self.origin = self.im
		self.px = self.im.load()
		self.imsize = self.im.size
		photo = self.im.resize((440, 330), Image.ANTIALIAS)
		photo = ImageTk.PhotoImage(photo)
		self.canvas1.image = photo
		self.canvas1.create_image(3,3,anchor='nw',image=photo)

	def add_blur(self):
		radius = self.scale1.get()
		if radius == 0:
			self.im = self.origin
			self.px = self.im.load()
			photo = self.im.resize((440, 330), Image.ANTIALIAS)
			photo = ImageTk.PhotoImage(photo)
			self.canvas1.image = photo
			self.canvas1.create_image(3,3,anchor='nw',image=photo)
		else:
			self.im = self.origin.filter(ImageFilter.GaussianBlur(radius = radius))
			self.px = self.im.load()
			photo = self.im.resize((440, 330), Image.ANTIALIAS)
			photo = ImageTk.PhotoImage(photo)
			self.canvas1.image = photo
			self.canvas1.create_image(3,3,anchor='nw',image=photo)

	def get_pixel_value(self,x,y):
		p_x, p_y = round(x * self.imsize[0] / 440), round(y * self.imsize[1] / 330)
		#
		if p_x >= self.imsize[0]:
			p_x = self.imsize[0] - 1
		if p_y >= self.imsize[1]:
			p_y = self.imsize[1] - 1
		#
		self.p_x, self.p_y = p_x, p_y
		#
		for i in range(3):
			self.rgb[i] = self.px[p_x,p_y][i]
		self.avrrgb = sum(self.rgb) / 3
		#
		minrgb, maxrgb = min(self.rgb), max(self.rgb)
		if maxrgb == 0:
			self.s = 0
		else:
			self.s = (maxrgb - minrgb) / maxrgb

	def get_pixel_area(self,x,y,botx,boty):
		p_x1, p_y1 = round(x * self.imsize[0] / 440), round(y * self.imsize[1] / 330)
		p_x2, p_y2 = round(botx * self.imsize[0] / 440), round(boty * self.imsize[1] / 330)
		#
		if p_x1 >= self.imsize[0]:
			p_x1 = self.imsize[0] - 1
		if p_y1 >= self.imsize[1]:
			p_y1 = self.imsize[1] - 1
		if p_x2 >= self.imsize[0]:
			p_x2 = self.imsize[0] - 1
		if p_y2 >= self.imsize[1]:
			p_y2 = self.imsize[1] - 1
		#
		self.p_x, self.p_y, self.p_botx, self.p_boty = p_x1, p_y1, p_x2, p_y2
		#
		if p_x1 >= p_x2:
			start_x, stop_x = p_x2, p_x1
		else:
			start_x, stop_x = p_x1, p_x2
		if p_y1 >= p_y2:
			start_y, stop_y = p_y2, p_y1
		else:
			start_y, stop_y = p_y1, p_y2
		#
		px_rgb, rgb_min, rgb_max = [], [], []
		#
		sum_r, sum_g, sum_b = 0, 0, 0
		count = 0
		for i in range(start_x,stop_x+1):
			for j in range(start_y,stop_y+1):
				sum_r += self.px[i,j][0]
				sum_g += self.px[i,j][1]
				sum_b += self.px[i,j][2]
				#
				for k in range(3):
					px_rgb.append(self.px[i,j][k])
				rgb_min.append(min(px_rgb))
				rgb_max.append(max(px_rgb))
				px_rgb.clear()
				#
				count += 1
		self.rgb[0] = round(sum_r/count)
		self.rgb[1] = round(sum_g/count)
		self.rgb[2] = round(sum_b/count)
		self.avrrgb = (sum_r + sum_g + sum_b) / (3 * count)
		#
		sum_s = 0
		for i in range(count):
			if rgb_max[i] == 0:
				sum_s += 0
			else:
				temp_s = (rgb_max[i] - rgb_min[i]) / rgb_max[i]
				sum_s += temp_s
		self.s = sum_s/count


	def get_hex(self):
		self.hex = '#{:02x}{:02x}{:02x}'.format(self.rgb[0], self.rgb[1], self.rgb[2])

	def regression_equation(self,parameter,concentration):
		if len(parameter) == 0:
			self.a, self.b = 0, 0
			return
		#
		param_2 = sum([a*b for a,b in zip(parameter,parameter)])
		param_cons = sum([a*b for a,b in zip(parameter,concentration)])
		if (len(parameter)*param_2-(sum(parameter)**2)) == 0 or (len(parameter)*param_2-(sum(parameter)**2)) == 0:
			self.a, self.b = 0, 0
			return
		self.a = (sum(concentration)*param_2 - sum(parameter)*param_cons) / (len(parameter)*param_2-(sum(parameter)**2))
		self.b = (len(parameter)*param_cons - sum(parameter)*sum(concentration)) / (len(parameter)*param_2-(sum(parameter)**2))

	def print_regression(self):
		#
		def print_value(obj,val):
			obj.configure(state='normal')
			obj.delete('1.0',END)
			if val == None:
				obj.configure(state='disabled')
				return
			obj.insert(END,round(val,5))
			obj.configure(state='disabled')
		#
		print_value(self.txt9,self.b)
		print_value(self.txt11,self.a)

	def solution(self,parameter,unit):
		self.result = self.a + self.b*parameter
		#
		def print_value(obj,val):
			obj.configure(state='normal')
			obj.delete('1.0',END)
			if val == None:
				obj.configure(state='disabled')
				return
			try:
				obj.insert(END,round(val,6))
			except:
				obj.insert(END,val)
			obj.configure(state='disabled')
		#
		print_value(self.txt12,self.result)
		print_value(self.txt13,unit)


	def calculate_unknown(self,unknown,blank):
		if self.s == None:
			return
		if unknown == 0 or len(blank) == 0:
			self.unknown = None
			self.txt8.configure(state='normal')
			self.txt8.delete('1.0',END)
			self.txt8.insert(END,str(self.unknown))
			self.txt8.configure(state='disabled')
			return
		#
		temp = sum(blank)/len(blank)
		if temp == 0:
			self.unknown = None
		else:
			self.unknown = math.log(temp,10) - math.log(unknown,10)
		#
		self.txt8.configure(state='normal')
		self.txt8.delete('1.0',END)
		try:
			self.txt8.insert(END,str(round(self.unknown,5)))
		except:
			self.txt8.insert(END,str(self.unknown))
		self.txt8.configure(state='disabled')

	def print_pixel_values(self):
		#
		def print_value(obj,val):
			obj.configure(state='normal')
			obj.delete('1.0',END)
			if val == None:
				obj.configure(state='disabled')
				return
			obj.insert(END,val)
			obj.configure(state='disabled')
		#
		print_value(self.txt1,str(round(self.s,3)))
		print_value(self.txt2,str(self.rgb[0]))
		print_value(self.txt3,str(self.rgb[1]))
		print_value(self.txt4,str(self.rgb[2]))
		print_value(self.txt5,str(round(self.avrrgb,3)))

	def display_graph(self,parameter,concentration):
		fig = Figure(figsize=(4, 3), dpi=60)
		axes = fig.add_subplot(111)
		line, = axes.plot(concentration,parameter,'b*')
		point, = axes.plot(self.result,self.unknown,'ro')
		axes.autoscale()
		axes.set_ylabel('Color Parameters')
		graph = FigureCanvasTkAgg(fig, master=self.window)
		self.canvas2 = graph.get_tk_widget()
		self.canvas2.place(x=20,y=390)
		self.canvas2.configure(width = 440, height = 320)

	def print_main_param(self,parameter,concentration):
		def print_list(obj,vals):
			obj.configure(state='normal')
			obj.delete('1.0',END)
			for i in range(len(vals)):
				try:
					temp = str(round(vals[i],5)) + '\n'
				except:
					temp = vals[i] + '\n'
				obj.insert(END,temp)
			obj.configure(state='disabled')
		#
		if len(parameter) > 0:
			print_list(self.txt6,parameter)
			print_list(self.txt7,concentration)
