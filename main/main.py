#   Code by Stoni. Discord > Stoni#0695
#       I own nothing. This is just for da pplz.
#   Map by DayZTV

from tkinter import *
from tkinter import ttk

root = Tk()

root.title("DayZ Plot")
root.geometry("1000x800+0+0")
bgcolor = "#ACACAC"
root.configure(bg=bgcolor)

canvas = Canvas(root)

# set the map to be map
img = PhotoImage(file="map.png")

# makes map
canvas.create_image(0, 0, image=img)
canvas.pack(side=LEFT, fill=BOTH, expand=1)

# makes scrollbars x = x axis, y = y axis.
xsb = Scrollbar(canvas, orient=HORIZONTAL, command=canvas.xview)
ysb = Scrollbar(canvas, orient=VERTICAL, command=canvas.yview)
canvas.configure(yscrollcommand=ysb.set, xscrollcommand=xsb.set)
canvas.configure(scrollregion=(-4000, -3698, 4000, 3698))
xsb.pack(side=BOTTOM, fill=X)
ysb.pack(side=RIGHT, fill=Y)


# start of making pins
# had plans of being able to enter the name of said pin
pin = PhotoImage(file="pin.png")

pinName = ""

# the class to make the pin
# class pinD:
#     def pindrop(event):
#         xpos, ypos = canvas.scan_mark(event.x, event.y)
#         canvas.create_image(xpos, ypos, image=pin, anchor=SE)


# this shit was going to make it so you could move/scroll by clicking and dragging
def getpos(event):
    global mousex, mousey
    mousex, mousey = canvas.scan_mark(event.x, event.y)


dropPin = ttk.Button(root, text="Place Pin", command=canvas.create_image(mousex, mousey, pin))
dropPin.pack(side=TOP, padx=5, pady=5, anchor=N)
dropCamp = ttk.Button(root, text="Place Camp")
dropCamp.pack(side=TOP, padx=5, pady=5, anchor=N)


def move(self):
    canvas.bind("<ButtonPress-1>", self.canvas.scrollstart)
    canvas.bind("<B1-Motion>", self.canvas.scrollmove)


def scrollstart(self, event):
    self.canvas.scan_mark(event.x, event.y)


def scrollmove(self, event):
    self.canvas.scan_dragto(event.x, event.y, gain=1)


#yeet
root.mainloop()
