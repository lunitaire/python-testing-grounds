#!/usr/bin/python3
#Atrian Wagner 
from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import *
root = Tk()

PROGRAM_NAME = " tkinter oekaki "
root.title(PROGRAM_NAME)
root.geometry("750x500")
root.config(background = "gray")


bgcolor = 'white'
wdraw = 3
drawcolor = 'black'
steps = 5

menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
# all file menu-items will be added here next
menu_bar.add_cascade(label='File', menu=file_menu)
root.config(menu=menu_bar)

panedwindow = ttk.Panedwindow(root, orient = HORIZONTAL)
panedwindow.pack(fill=BOTH, expand=TRUE)
tools = ttk.Frame(panedwindow, width = 30, height = 30)
tools.pack(fill=Y, side = LEFT)
colorpicker = Canvas(tools, width = 60, height = 40)
colorpicker.pack()

def getcolor():
	color = askcolor()
	hexcolor = color[1]
	return hexcolor

drawclr = colorpicker.create_rectangle((10, 10, 30, 30), outline="#000",fill=drawcolor)
colorpicker.tag_bind(drawclr, "<Button-1>", lambda x: setdrawcolor())

def setdrawcolor():
    global drawcolor
    drawcolor = getcolor()
    colorpicker.itemconfigure(drawclr, fill=drawcolor)

bgclr = colorpicker.create_rectangle((35, 10, 55, 30), outline="#000", fill=bgcolor)
colorpicker.tag_bind(bgclr, "<Button-1>", lambda x: setbgcolor())
entry = ttk.Entry(tools,width = 10)
entry.pack()

def setbgcolor():
    global bgcolor
    bgcolor = getcolor()
    colorpicker.itemconfigure(bgclr, fill=bgcolor)
    canvas.itemconfigure(canvasbg, fill = bgcolor, outline = bgcolor)
    
def drawdebug(event):
	global prev
	prev = event
#	print('type: {}'.format(event.type))
#	print('widget: {}'.format(event.widget))
#	print('num: {}'.format(event.num))
#	print('x:{}'.format(event.x))
#	print('y: {}'.format(event.y))
#	print('x_root: {}'.format(event.x_root))
#	print('y_root: {}'.format(event.y_root))
    
mainframe = ttk.Frame(panedwindow, relief = GROOVE, borderwidth=2)
panedwindow.add(tools,weight=0)
panedwindow.add(mainframe,weight=4)
canvas = Canvas(mainframe, width = 640, height = 480, background = bgcolor)
canvas.pack()

canvasbg = canvas.create_rectangle((0, 0, 645, 485), fill=bgcolor, outline = bgcolor)

def draw(event):
	global prev
	canvas.create_line(prev.x, prev.y, event.x, event.y, fill=drawcolor,width = wdraw)
	x = canvas.canvasx(event.x)
	y = canvas.canvasy(event.y)
	#, smooth = True, splinesteps = steps
	prev = event
#, dash=(1, 4) add in dash option

canvas.bind('<ButtonPress-1>', drawdebug)
canvas.bind('<B1-Motion>', draw)




root.mainloop()
