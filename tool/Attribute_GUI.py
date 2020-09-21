#coding= utf-8
#!/usr/bin/python3
import os
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext, filedialog
from PIL import Image, ImageTk

index, image_num = 0, 0
select_img, select_path = '', ''
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

    # print("select_file", select_img)
    fp = open(select_img, 'r')
    load = Image.open(select_img)
    fp.close()
    w, h = load.size[0], load.size[1]
    if w > 512 and h > 512:
        width, height = 512, 512
        load = load.resize((width, height), Image.ANTIALIAS)
        # print("load size: ", load.size[0], load.size[1])
    # if w >= h:
    #     width, height = 512, h
    #     load = load.resize((width, height), Image.ANTIALIAS)
    # else:
    #     width, height = w, 512
    #     load = load.resize((width, height), Image.ANTIALIAS)
    # load = Image.open(select_img).resize((width, height), Image.ANTIALIAS)

    # 声明全局变量
    global original
    original = load
    render = ImageTk.PhotoImage(load)
    imgin = tk.Label(window, image=render)
    imgin.configure(image=render)
    imgin.image = render
    imgin.place(x=25, y=25)
    # imgin.destroy()

    # img = ImageTk.PhotoImage(load)
    # label_img = tk.Label(window, image=img)
    # label_img.configure(image=img)
    # label_img.place(x=25, y=25)
    # window.update_idletasks()

    # render = ImageTk.PhotoImage(load)
    # img = tk.Label(window, image=render)
    # img.configure(image=render)
    # img.image = render
    # img.place(x=25, y=25)

    # render = ImageTk.PhotoImage(load)
    # img = tk.Label(window, image=render)
    # img.configure(image=render)
    # img.image = render
    # img.place(x=25, y=25)


def choose_pre_file():
    global index
    global image_num
    global filenames
    global select_img
    global imgin
    # os.remove(select_img)
    # window.update_idletasks()
    index -= 1
    if index == -image_num:
        index = 0
    # print("image_num: ", image_num, " pre cur index: ", index)
    # print("pre filenames[index]: ", filenames[index])
    # window.update_idletasks()
    imgin.destroy()
    choose_file(filenames[index], lots=True)


def choose_next_file():
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
    # print("image_num:", image_num, " next cur index: ", index)
    # print("next filenames[index]: ", filenames[index])
    # window.update_idletasks()
    imgin.destroy()
    choose_file(filenames[index], lots=True)


def choose_files():
    global image_num
    global filenames
    global select_path
    select_path = filedialog.askdirectory(title='选择图片路径')
    # print(select_path)
    filenames = os.listdir(select_path)
    # print("filenames: ", filenames)
    image_num = len(filenames)
    # print("image_num: ", image_num)
    if not image_num:
        print("Error! ")
    choose_file(filenames[0], lots=True)


def save_file():
    global select_img
    fw = open('./attribute.txt', 'a')
    res = ''
    for item in attribute_dict.items():
        print(item)
        res += str(item[0]) + ':' + str(item[1]) + ' '
    print("select_img: ", select_img)
    line = select_img + ' ' + res
    f.set(line)
    print(line, file=fw)
    fw.close()


def flash_attribute():
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


window = tk.Tk()
window.title("Attribute Label Tool")
window.geometry('800x800')

a_label = ttk.Label(window, text="Attribute List", font=('Times New Roman', 12))
a_label.place(x=610, y=25)

button1 = tk.Button(window, text="选择图像", command=choose_file)
button1.place(x=50, y=550)

button2 = tk.Button(window, text="选择图像路径", command=choose_files)
button2.place(x=50, y=600)

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

window.mainloop()
