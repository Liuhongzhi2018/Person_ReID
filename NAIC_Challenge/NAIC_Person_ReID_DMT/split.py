# import numpy as np
# import random
# import os.path as osp
# #import pandas as pd
# np.random.seed(seed=2)
#
#
# def split(full_list, shuffle=True, ratio=0.25):
#     n_total = len(full_list)
#     offset = int(n_total * ratio)
#     if n_total == 0 or offset < 1:
#         return [], full_list
#     if shuffle:
#         random.shuffle(full_list)
#     sublist_1 = full_list[:offset]
#     sublist_2 = full_list[offset:]
#     return sublist_1, sublist_2
# dic = {'a':1, 'b':2, 'c':2,'d':3, 'e':3,'f':3, 'g':3,'h':4, 'i':4,'j':4, 'm':4,'l':4, 'o':2}
# dic_new = {}
# for key, val in dic.items():
#     a=[]
#     a.append(key)
#     #print(a)
#     #print(dic_new.keys())
#     if val in dic_new.keys():
#         dic_new[val].append(key)
#     else:
#         dic_new[val]=a
# b=[]
#
# for i in dic_new.keys():
#     b.append(i)
# a,p=split(b)
# #c=pd.DataFrame(dic_new)
# # a=c.sample(frac=0.25)
# # print(a)
# print(b)
# print(a)
# print(p)
# o="orpg/"
# data=[]
# for i in p:
#     for k in dic_new[i]:
#         data.append((osp.join(o,k),i,1))
# print(data)
# print(p[1:])
# print(dic_new)
# def checkid(query, gallery):
#     q = []
#     g = []
#     for i in query:
#         q.append(i[1])
#     for i in gallery:
#         g.append(i[1])
#     for i in q:
#         if i not in g:
#             print("not appear", i)
# q=[(1,2,3),(3,4,1),(5,6,7)]
# g=[(5,6,5),(1,1,1),(9,9,9)]
# checkid(g,q)
import os,shutil


def process_newlabel(label_file):
    newla={}
    for key, val in label_file.items():
        a = []
        a.append(key)

        if val in newla.keys():
            newla[val].append(key)
        else:
            newla[val] = a
    return newla
def process_label(label_file):
    f = open(label_file, encoding="utf-8")
    label={}
    while True:
        content = f.readline()
        if content == '':
            break
        img, id = content.strip().split(':')
        label[img] = id
    return label
# querytxt='/Users/lijiaqi/Downloads/query.txt'
# label='/Users/lijiaqi/Downloads/fast-reid-master/datasets/pengcheng/train/newlabel.txt'
querytxt='/home/lijiaqi/LiuHongzhi/ReID/NAIC_Person_ReID_DMT/data/train/query.txt'
label= '/home/lijiaqi/LiuHongzhi/ReID/NAIC_Person_ReID_DMT/data/train/new_label.txt'
quelis = []
f = open(querytxt)
for line in f:
    quelis.append(str(int(line)))

labeldic=process_label(label)
labelnew=process_newlabel(labeldic)

print(len(labelnew.keys()))
# image='/Users/lijiaqi/Downloads/fast-reid-master/datasets/pengcheng/train/images/'
# quer='/Users/lijiaqi/Downloads/fast-reid-master/datasets/pengcheng/train/query/'
# gal='/Users/lijiaqi/Downloads/fast-reid-master/datasets/pengcheng/train/gallery/'

image='/home/lijiaqi/LiuHongzhi/ReID/NAIC_Person_ReID_DMT/data/train/images/'
quer='/home/lijiaqi/LiuHongzhi/ReID/NAIC_Person_ReID_DMT/data/train/query/'
gal='/home/lijiaqi/LiuHongzhi/ReID/NAIC_Person_ReID_DMT/data/train/gallery/'
for i in quelis:
    shutil.move(image+labelnew[i][0],quer+labelnew[i][0])
    for k in labelnew[i][1:]:
        shutil.move(image+k,gal+k)
#print(labeldic)
