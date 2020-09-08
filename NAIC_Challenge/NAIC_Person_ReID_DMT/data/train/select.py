import os
import shutil

# f = open('/home/lijiaqi/LiuHongzhi/ReID/NAIC_Challenge/NAIC_Person_ReID_DMT/data/train/name_wolabel.txt', 'r')
# select_list = []
# for line in f.readlines():
#     line = line.strip('\n')
#     # print("line: ",line)
#     img = line.strip('\n')
#     select_list.append(img)
# f.close()

# img_root = '/home/lijiaqi/LiuHongzhi/ReID/NAIC_Challenge/data/train/'
# tar_root = '/home/lijiaqi/LiuHongzhi/ReID/NAIC_Challenge/data/train_wolabel/'
# filenames = os.listdir(img_root)
# for filename in filenames:
#     # line = line.strip('\n')
#     # print("line: ",line)
#     # img, pid = line.strip('\n').split(':')
#     # img = line.strip()
#     if filename in select_list:
#         src = img_root + filename
#         print("in: ", src)
#         dist = tar_root + filename
#         # # shutil.copy(src, dist)
#         shutil.move(src, dist)
#         # print(filename)
#     else:
#         continue

# (py36pt16) [lijiaqi@localhost NAIC_Person_ReID_DMT]$ ls -l|grep "^-"| wc -l
# train w/ label  69973
# train w/o label  20778


img_root = '/home/lijiaqi/LiuHongzhi/ReID/NAIC_Challenge/data/train/'
img_list = []
filenames = os.listdir(img_root)
for filename in filenames:
    img_list.append(filename)

f = open('/home/lijiaqi/LiuHongzhi/ReID/train/label.txt', 'r')
wf = open('/home/lijiaqi/LiuHongzhi/ReID/NAIC_Challenge/data/train/train_label.txt', 'w')
select_list = []
for line in f.readlines():
    line = line.strip('\n')
    # print("line: ",line)
    img, pid = line.strip('\n').split(':')
    if img in img_list:
        print(line, file=wf)
wf.close()
f.close()
