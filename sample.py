
from tkinter import* 
import tkinter as tk 

root = Tk() 
root.geometry('1000x600+500+100')
root.resizable(False,False)

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def mov(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    canvas.move(obj,x,y)
    canvas.update()

canvas=Canvas(root,width=800,height=600,bg="red")
canvas.pack(fill=BOTH,expand=1)

obj=canvas.create_text(100,50,text="Object",fill='blue',font=('Gotham Medium', 30,"bold"),anchor="nw")

canvas.tag_bind(obj,"<Button-1>",drag_start)
canvas.tag_bind(obj,'<B1-Motion>',mov)

root.mainloop()