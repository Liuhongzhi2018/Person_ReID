#coding= utf-8
#!/usr/bin/python3
import os
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext, filedialog, messagebox
from tkinter.filedialog import askopenfilename, askopenfile, asksaveasfile
from PIL import Image, ImageTk

index, image_num = 0, 0
select_img, select_path, save_txt_path = '', '', ''
imgs_dict = {}
filenames = []
imgin = ''


def choose_file(img=None, lots=False):
    global select_path
    global select_img
    global imgin
    select_file = img
    if not lots:
        select_file = filedialog.askopenfilename(title='选择图片')

    select_img = select_path + '/' + select_file if lots else select_file
    e.set(select_img)

    fp = open(select_img, 'r')
    load = Image.open(select_img)
    fp.close()
    w, h = load.size[0], load.size[1]
    if w > 512 and h > 512:
        width, height = 512, 512
        load = load.resize((width, height), Image.ANTIALIAS)

    render = ImageTk.PhotoImage(load)
    imgin = tk.Label(window, image=render)
    imgin.configure(image=render)
    imgin.image = render

    # place location
    std_x, std_y = 25, 25
    cw, ch = load.size[0], load.size[1]
    cur_loc_x, cur_loc_y = std_x + 256 - cw // 2, std_y + 256 - ch // 2
    imgin.place(x=cur_loc_x, y=cur_loc_y)


def choose_pre_file(self):
    global index
    global image_num
    global filenames
    global select_img
    global imgin
    index -= 1
    if index == -image_num:
        index = 0
    imgin.destroy()
    choose_file(filenames[index], lots=True)


def choose_next_file(self):
    global index
    global image_num
    global filenames
    global select_img
    global imgin
    # os.remove(select_img)
    window.update_idletasks()
    index += 1
    if index == image_num:
        index = 0
    imgin.destroy()
    choose_file(filenames[index], lots=True)


def choose_files():
    global image_num
    global filenames
    global select_path
    select_path = filedialog.askdirectory(title='选择图片路径')
    filenames = os.listdir(select_path)
    image_num = len(filenames)
    if not image_num:
        print("Error! ")
    choose_file(filenames[0], lots=True)


def save_file(self):
    global save_txt_path
    global select_img
    # tk.messagebox.showinfo(title='提示', message='请确认属性正确！')
    retval = tk.messagebox.askokcancel(title='提示', message='请确认  属性选择  正确！')
    if save_txt_path == '':
        tk.messagebox.showwarning(title='注意', message='当前未选择保存路径，已默认保存在当前路径')
        save_txt_path = './attribute.txt'
    if not retval:
        return
    fw = open(save_txt_path, 'a')
    res = ''
    for item in attribute_dict.items():
        # print(item)
        res += str(item[0]) + ':' + str(item[1]) + ' '
    # print("select_img: ", select_img)
    line = select_img + ' ' + res
    f.set(line)
    print(line, file=fw)
    fw.close()
    tk.messagebox.showinfo(title='提示', message='已保存属性')


def clear_file(img=None, lots=False):
    global imgin
    imgin.destroy()


def flash_attribute(self):
    res = ''
    for item in attribute_dict.items():
        print(item)
        res += str(item[0]) + ':' + str(item[1]) + ' '
    f.set(res)


def hatCall():
    radSel = vhat.get()
    attribute_dict['hat'] = 0
    if radSel == 1:
        attribute_dict['hat'] = 1
        print("有戴")

    elif radSel == 2:
        attribute_dict['hat'] = 2
        print("没戴")
    print(attribute_dict['hat'])


def yiCall():
    radSel = vyi.get()
    attribute_dict['clo'] = 0
    if radSel == 1:
        attribute_dict['clo'] = 1
        print("有穿")
    elif radSel == 2:
        attribute_dict['clo'] = 2
        print("没穿")
    print(attribute_dict['clo'])


def open_file(img=None, lots=False):
    global select_path
    global select_img
    global imgin
    select_file = img
    if not lots:
        select_file = filedialog.askopenfilename(title='选择图片')

    select_img = select_path + '/' + select_file if lots else select_file
    e.set(select_img)

    fp = open(select_img, 'r')
    load = Image.open(select_img)
    fp.close()
    w, h = load.size[0], load.size[1]
    if w > 512 and h > 512:
        width, height = 512, 512
        load = load.resize((width, height), Image.ANTIALIAS)

    render = ImageTk.PhotoImage(load)
    imgin = tk.Label(window, image=render)
    imgin.configure(image=render)
    imgin.image = render

    std_x, std_y = 25, 25
    cw, ch = load.size[0], load.size[1]
    cur_loc_x, cur_loc_y = std_x + 256 - cw // 2, std_y + 256 - ch // 2
    imgin.place(x=cur_loc_x, y=cur_loc_y)


def savefile(self):
    global save_txt_path
    filetypes = [
        ("All Files", '*'),
        ("Python Files", '*.py', 'TEXT'),
        ("Text Files", '*.txt', 'TEXT'),
        ("Config Files", '*.conf', 'TEXT')]
    save_txt_path = tk.filedialog.asksaveasfilename(defaultextension='.txt', filetypes=filetypes)


def Editor():
    tk.messagebox.showinfo("版权声明", "欢迎使用属性标注工具！\n作者： 刘鸿智")


window = tk.Tk()
window.title("属性标注工具 Attribute Label Tool")
window.geometry('800x800')

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='打开 Open', accelerator='Ctrl+o',
                     command=open_file, underline=0)
filemenu.add_command(label='保存 Save', accelerator='Ctrl+s',
                     command=savefile, underline=0)
filemenu.add_separator()
filemenu.add_command(label='退出 Quit', accelerator='Alt+F4',
                     command=window.destroy, underline=0)
menubar.add_cascade(label='文件 File', underline=0, menu=filemenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label='关于此工具 About', underline=0,
                     command=Editor)
menubar.add_cascade(label='帮助 Help', menu=helpmenu)

a_label = ttk.Label(window, text="Attribute List", font=('Times New Roman', 12))
a_label.place(x=610, y=25)

button1 = tk.Button(window, text="选择图像", command=choose_file)
button1.place(x=50, y=550)

button2 = tk.Button(window, text="选择图像路径", command=choose_files)
button2.place(x=50, y=600)

button1 = tk.Button(window, text="清空图像", command=clear_file)
button1.place(x=400, y=600)

button3 = tk.Button(window, text="上一张", command=choose_pre_file)
button3.place(x=200, y=600)

button5 = tk.Button(window, text="下一张", command=choose_next_file)
button5.place(x=300, y=600)

e = tk.StringVar()
e_entry = tk.Entry(window, width=30, textvariable=e)
e_entry.place(x=200, y=550)

f = tk.StringVar()
f_entry = tk.Entry(window, width=20, textvariable=f)
f_entry.place(x=600, y=550)

attribute_dict = {}

group1 = tk.LabelFrame(window, text="是否有戴 安全帽", padx=5, pady=5)
group1.place(x=600, y=75)

group2 = tk.LabelFrame(window, text="是否有穿 反光背心", padx=5, pady=5)
group2.place(x=600, y=175)

vhat = tk.IntVar()
hat1 = tk.Radiobutton(group1, text="有", variable=vhat, value=1, command=hatCall).grid(column=0, row=0, sticky=tk.W)
hat2 = tk.Radiobutton(group1, text="没有", variable=vhat, value=2, command=hatCall).grid(column=1, row=0, sticky=tk.W)

vyi = tk.IntVar()
yi1 = tk.Radiobutton(group2, text="有", variable=vyi, value=1, command=yiCall).grid(column=0, row=0, sticky=tk.W)
yi2 = tk.Radiobutton(group2, text="没有", variable=vyi, value=2, command=yiCall).grid(column=1, row=0, sticky=tk.W)


button6 = tk.Button(window, text="刷新  已选属性", command=flash_attribute)
button6.place(x=600, y=580)

button7 = tk.Button(window, text="保存  此图属性", command=save_file)
button7.place(x=600, y=650)

window.bind('a', choose_pre_file)
window.bind('d', choose_next_file)
window.bind('z', flash_attribute)
window.bind('c', save_file)

window.config(menu=menubar)
window.mainloop()
