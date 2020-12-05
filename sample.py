
from tkinter import* 
import tkinter as tk 

root = Tk() 
root.geometry('1000x600+500+100')
root.resizable(False,False)

def drag_start(event):
    widget = event.widget
    widget.startX,widget.startY = event.x,event.y

def mov(event):
    widget = event.widget
    widget.move(obj,event.x-widget.startX,event.y-widget.startY)
    widget.startX,widget.startY = event.x,event.y


canvas=Canvas(root,width=800,height=600,bg="red")
canvas.pack(fill=BOTH,expand=1)

obj=canvas.create_text(100,50,text="Object",fill='blue',font=('Gotham Medium', 30,"bold"),anchor="nw")

canvas.tag_bind(obj,"<Button-1>",drag_start)
canvas.tag_bind(obj,'<B1-Motion>',mov)

root.mainloop()
