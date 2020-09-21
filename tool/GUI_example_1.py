#!/usr/bin/python3
# coding= utf-8

#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# Create instance
win = tk.Tk()   

# Add a title       
win.title("Attribute Label Tool")  

# Modify adding a Label
a_label = ttk.Label(win, text="A Label")
a_label.grid(column=0, row=0)

# Modified Button Click Function
def click_me(): 
    action.configure(text='Hello ' + name.get() + ' ' + 
                     number_chosen.get())

# Changing our Label
ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

# Adding a Button
action = ttk.Button(win, text="Click Me!", command=click_me)   
action.grid(column=2, row=1)                                 # <= change column to 2

# Creating three checkbuttons
ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)                   

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)                   

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.deselect()
check3.grid(column=2, row=4, sticky=tk.W)                     

# GUI Callback function 
def checkCallback(*ignoredArgs):
    # only enable one checkbutton
    if chVarUn.get(): check3.configure(state='disabled')
    else:             check3.configure(state='normal')
    if chVarEn.get(): check2.configure(state='disabled')
    else:             check2.configure(state='normal') 

# trace the state of the two checkbuttons
chVarUn.trace('w', lambda unused0, unused1, unused2 : checkCallback())    
chVarEn.trace('w', lambda unused0, unused1, unused2 : checkCallback())   


# Using a scrolled Text control    
scrol_w  = 30
scrol_h  =  3
scr = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)
#### scr.grid(column=0, row=5, sticky='WE', columnspan=3)                    
scr.grid(column=0, row=5, columnspan=3)              # sticky property removed   


# First, we change our Radiobutton global variables into a list
colors = ["Blue", "Gold", "Red"]   

# We have also changed the callback function to be zero-based, using the list 
# instead of module-level global variables 
# Radiobutton Callback
def radCall():
    radSel=radVar.get()
    if   radSel == 0: win.configure(background=colors[0])  # zero-based
    elif radSel == 1: win.configure(background=colors[1])  # using list
    elif radSel == 2: win.configure(background=colors[2])

# create three Radiobuttons using one variable
radVar = tk.IntVar()

# Next we are selecting a non-existing index value for radVar
radVar.set(99)                                 
 
# Now we are creating all three Radiobutton widgets within one loop
for col in range(3):                             
    curRad = tk.Radiobutton(win, text=colors[col], variable=radVar, 
                            value=col, command=radCall)          
    curRad.grid(column=col, row=6, sticky=tk.W)             # row=6

# Create a container to hold labels
buttons_frame = ttk.LabelFrame(win, text=' Labels in a Frame ')
buttons_frame.grid(column=0, row=7) 
# buttons_frame.grid(column=1, row=7)                # now in col 1

# Place labels into the container element
ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0, sticky=tk.W)

name_entered.focus()      # Place cursor into name Entry
#======================
# Start GUI
#======================
win.mainloop()



# from PIL import Image, ImageTk # 导入图像处理函数库
# import tkinter as tk           # 导入GUI界面函数库

# # 创建窗口 设定大小并命名
# window = tk.Tk()
# window.title('图像显示界面')
# window.geometry('600x500')
# global img_png           # 定义全局变量 图像的
# var = tk.StringVar()    # 这时文字变量储存器

# # 创建打开图像和显示图像函数
# def Open_Img():
#     global img_png
#     var.set('已打开')
#     Img = Image.open('1.jpg')
#     img_png = ImageTk.PhotoImage(Img)

# def Show_Img():
#     global img_png
#     var.set('已显示')   # 设置标签的文字为 'you hit me'
#     label_Img = tk.Label(window, image=img_png)
#     label_Img.pack()

# # 创建文本窗口，显示当前操作状态
# Label_Show = tk.Label(window,
#     textvariable=var,   # 使用 textvariable 替换 text, 因为这个可以变化
#     bg='blue', font=('Arial', 12), width=15, height=2)
# Label_Show.pack()
# # 创建打开图像按钮
# btn_Open = tk.Button(window,
#     text='打开图像',      # 显示在按钮上的文字
#     width=15, height=2,
#     command=Open_Img)     # 点击按钮式执行的命令
# btn_Open.pack()    # 按钮位置
# # 创建显示图像按钮
# btn_Show = tk.Button(window,
#     text='显示图像',      # 显示在按钮上的文字
#     width=15, height=2,
#     command=Show_Img)     # 点击按钮式执行的命令
# btn_Show.pack()    # 按钮位置

# # 运行整体窗口
# window.mainloop()

# from PIL import ImageTk
# from tkinter import *
# import PIL
# import tkinter as tk
# import os

# class GetCode(object):

#     def __init__(self):

#         self.data={}  # 存放返回值
#         self.root = tk.Tk()
#         self.root.geometry('640x800') 
#         self.root.resizable(width=False,height=False)   # 固定长宽不可拉伸

#         self.textLabel=tk.Label(self.root,text="请输入验证码：").pack() # 标签
#         self.textStr=StringVar()
#         self.textEntry=tk.Entry(self.root,textvariable=self.textStr)
#         self.textStr.set("")
#         self.textEntry.pack()  # 输入框

#         im=PIL.Image.open("1.jpg")
#         img=ImageTk.PhotoImage(im)
#         imLabel=tk.Label(self.root,image=img).pack() # 显示图片

#         self.but = tk.Button(self.root,text="确认",command=self.return_code).pack(fill="x") # 按键
#         self.root.mainloop()

#     def return_code(self):
#         # 返回输入框内容
#         self.data["code"]=self.textStr.get()
#         self.root.destroy()           # 关闭窗体
#         os.remove("test.jpg")         # 删除图片
#         print("输入框内容：" %self.data["code"]) 

# if __name__ == '__main__':
#     GetCode()


# import tkinter as tk
# from tkinter import ttk # ttk比tk功能和美观方面更强大。
# from tkinter import scrolledtext #从tkinter模块导入scrolledtext类（输入滚动文本框）
# # Create instane

# win = tk.Tk()  #导入tk库中Tk类构造实例win,最底层容器，之后label和button要嵌入到其上。
 
# #Add a title
# win.title('Note book')
 
# #Adding a Label that will get modified
# #将win这个父类容器传递给标签label，之后label会显示在win窗口上。
# #a_label = ttk.Label(win, text = 'This is my note book！')
# #a_label.grid(column = 0,row = 0)
 
# # Modified Button Click Function:
# def click_me():
#     action.configure(text  = 'Hello！ ' + name.get() + number_chosen.get())
 
# # Changing our label
# ttk.Label(win,text = 'Enter a name!  :').grid(column = 0,row = 0)
# ttk.Label(win,text = 'Choose a number! ').grid(column = 1,row = 0)
# #Adding a Text box entry widget
# name = tk.StringVar()  #声明tkinter变量
# name_entered = ttk.Entry(win,width = 12, textvariable = name) #Entry是一个文本输入控件
# name_entered.grid(column = 0,row = 1)
# name_entered.focus()     # 放置一个光标（cursor）在文本控件输入框
 
# number = tk.StringVar()
# number_chosen = ttk.Combobox(win,width = 12, textvariable = number, state = 'readonly')
# number_chosen['values'] = (1,2,4,6,10,12)  #虽然未在元组加‘’，但由于之前定义为StringVar()，故为字符串
# number_chosen.grid(column = 1,row = 1)
# number_chosen.current(0)
 
# #Adding a Button
# action = ttk.Button(win, text = 'Click Me', command = click_me)
# action.grid(column = 2,row = 1)
# #action.configure(state = 'disable')  #禁用button按钮


# #Creating three checkbuttons
# #创建了三个按钮部件
# chVarDis = tk.IntVar()
# check1 = tk.Checkbutton(win,text = 'Disable', variable = chVarDis, state = 'disable')
# check1.select()
# check1.grid(column = 0,row = 4, sticky = tk.W)  #利用sticky属性使得这些按钮始终与网格左对齐
 
# chVarUn = tk.IntVar()
# check2 =  tk.Checkbutton(win,text = 'unCheked', variable = chVarUn)
# check2.deselect()
# check2.grid(column = 1,row = 4, sticky = tk.W)
 
# chVarEn = tk.IntVar()
# check3 =  tk.Checkbutton(win,text = 'Enable', variable = chVarEn)
# check3.select()
# check3.grid(column = 2,row = 4, sticky = tk.W)


# #Radiobutton Globals
# COLOR1 = 'Blue'
# COLOR2 = 'Gold'
# COLOR3 = 'Red'
# #Radiobutton callbak
# def radCall():
#     radSel = radVar.get()
#     if   radSel == 1: win.configure(background = COLOR1)
#     elif radSel == 2: win.configure(background = COLOR2)
#     elif radSel == 3: win.configure(background = COLOR3)
 
# #Creat three radiobuttons using one variable
# radVar = tk.IntVar()
# rad1 = tk.Radiobutton(win,text = COLOR1, variable = radVar, value = 1, command = radCall)
# rad1.grid(column = 0,row = 5,sticky = tk.W,columnspan = 3)
 
# rad2 = tk.Radiobutton(win,text = COLOR2, variable = radVar, value = 2, command = radCall)
# rad2.grid(column = 1,row = 5,sticky = tk.W,columnspan = 3)
 
# rad3 = tk.Radiobutton(win,text = COLOR3, variable = radVar, value = 3, command = radCall)
# rad3.grid(column = 2,row = 5,sticky = tk.W,columnspan = 3)
 
# #Using a scrolled Text control
# scrol_w = 40
# scrol_h = 3
# scr = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)
# scr.grid(column = 0,columnspan = 3)

# #=====================
# #Start
# #=====================
# win.mainloop()


# # Create instance
# win = tk.Tk()

# # Add  a title
# win.title("hello world")

# win.geometry('640x800')                    # 是x 不是*
# win.resizable(width=True, height=True)     # 宽高可变, 默认为True

# # Adding a label
# ttk.Label(win, text="A Label").grid(column=0, row=0)

# # Adding a label that will be modify
# a_label = ttk.Label(win, text="B Label")
# a_label.grid(column=0, row=1)


# # Button Click Event Function
# def click_me():
#     action.configure(text="** I have been click! **")
#     a_label.configure(foreground='red')
#     a_label.configure(text='A red label')


# # Adding a Button
# action = ttk.Button(win, text="Click me!", command=click_me)
# action.grid(column=1, row=1)


# # Button Click Event Function
# def click_me_1():
#     action_1.configure(text="Hello " + name.get())


# # Changin our label
# ttk.Label(win, text="Enter a name: ").grid(column=0, row=2)

# # Adding a Text box entry widgt
# name = tk.StringVar()
# name_entered = ttk.Entry(win, width=12, textvariable=name)
# name_entered.grid(column=0, row=3)

# # Adding a Button
# action_1 = ttk.Button(win, text="Click me!", command=click_me_1)
# action_1.grid(column=1, row=3)

# # Start GUI
# win.mainloop()


# #-*- coding: utf-8 -*
# #======================
# #imports
# #======================
# import tkinter as tk
# from tkinter import ttk # ttk比tk功能和美观方面更强大。
# from tkinter import scrolledtext #从tkinter模块导入scrolledtext类（输入滚动文本框）
# # Create instane
 
# win = tk.Tk()  #导入tk库中Tk类构造实例win,最底层容器，之后label和button要嵌入到其上。
 
# #Add a title
# win.title('Note book')
 
# #Adding a Label that will get modified
# #将win这个父类容器传递给标签label，之后label会显示在win窗口上。
# #a_label = ttk.Label(win, text = 'This is my note book！')
# #a_label.grid(column = 0,row = 0)
 
# # Modified Button Click Function:
# def click_me():
#     action.configure(text  = 'Hello！ ' + name.get() + number_chosen.get())
 
# # Changing our label
# ttk.Label(win,text = 'Enter a name!  :').grid(column = 0,row = 0)
# ttk.Label(win,text = 'Choose a number! ').grid(column = 1,row = 0)
# #Adding a Text box entry widget
# name = tk.StringVar()  #声明tkinter变量
# name_entered = ttk.Entry(win,width = 12, textvariable = name) #Entry是一个文本输入控件
# name_entered.grid(column = 0,row = 1)
# name_entered.focus()     # 放置一个光标（cursor）在文本控件输入框
 
# number = tk.StringVar()
# number_chosen = ttk.Combobox(win,width = 12, textvariable = number, state = 'readonly')
# number_chosen['values'] = (1,2,4,6,10,12)  #虽然未在元组加‘’，但由于之前定义为StringVar()，故为字符串
# number_chosen.grid(column = 1,row = 1)
# number_chosen.current(0)
 
# #Adding a Button
# action = ttk.Button(win, text = 'Click Me', command = click_me)
# action.grid(column = 2,row = 1)
# #action.configure(state = 'disable')  #禁用button按钮
 
# #Creating three checkbuttons
# #创建了三个按钮部件
# chVarDis = tk.IntVar()
# check1 = tk.Checkbutton(win,text = 'Disable', variable = chVarDis, state = 'disable')
# check1.select()
# check1.grid(column = 0,row = 4, sticky = tk.W)  #利用sticky属性使得这些按钮始终与网格左对齐
 
# chVarUn = tk.IntVar()
# check2 =  tk.Checkbutton(win,text = 'unCheked', variable = chVarUn)
# check2.deselect()
# check2.grid(column = 1,row = 4, sticky = tk.W)
 
# chVarEn = tk.IntVar()
# check3 =  tk.Checkbutton(win,text = 'Enable', variable = chVarEn)
# check3.select()
# check3.grid(column = 2,row = 4, sticky = tk.W)
 
 
# #Radiobutton Globals
# COLOR1 = 'Blue'
# COLOR2 = 'Gold'
# COLOR3 = 'Red'
# #Radiobutton callbak
# def radCall():
#     radSel = radVar.get()
#     if   radSel == 1: win.configure(background = COLOR1)
#     elif radSel == 2: win.configure(background = COLOR2)
#     elif radSel == 3: win.configure(background = COLOR3)
 
# #Creat three radiobuttons using one variable
# radVar = tk.IntVar()
# rad1 = tk.Radiobutton(win,text = COLOR1, variable = radVar, value = 1, command = radCall)
# rad1.grid(column = 0,row = 5,sticky = tk.W,columnspan = 3)
 
# rad2 = tk.Radiobutton(win,text = COLOR2, variable = radVar, value = 2, command = radCall)
# rad2.grid(column = 1,row = 5,sticky = tk.W,columnspan = 3)
 
# rad3 = tk.Radiobutton(win,text = COLOR3, variable = radVar, value = 3, command = radCall)
# rad3.grid(column = 2,row = 5,sticky = tk.W,columnspan = 3)
 
# #Using a scrolled Text control
# scrol_w = 40
# scrol_h = 3
# scr = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)
# scr.grid(column = 0,columnspan = 3)
# #=====================
# #Start
# #=====================
# win.mainloop()