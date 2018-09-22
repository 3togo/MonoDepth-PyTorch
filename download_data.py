import os
import wget
files=open('kitti_archives_to_download.txt','r').readlines()
src_dir=os.path.expanduser('~/git/datasets/KittiAvg')
for mfile in files:
    mfile=mfile.strip()
    basename=os.path.basename(mfile)
    date_dir=basename[:10]
    src_date_dir=os.path.join(src_dir,date_dir)
    print(src_date_dir)
    # root,ext=os.path.splitext(sub_dir)
    # print(mfile)
    # #print("[%s]"%src_sub_dir)
    data_date_dir=os.path.join('data_dir',date_dir)
    print("data_date_dir=%s"%data_date_dir)
    print("src_date_dir=%s"%src_date_dir)
    if not os.path.isdir(data_date_dir):
        print('create root link')
        os.symlink(src_date_dir,data_date_dir)
    data_date_sub_dir=os.path.join(data_date_dir, basename[:-4])
    print('data_date_sub_dir=%s'%data_date_sub_dir)
    if not os.path.isdir(data_date_sub_dir):
        src_date_sub_dir=os.path.join(src_date_dir, basename[:-4])
        print('src_date_sub_dir=%s'%src_date_sub_dir)
        if os.path.isdir(src_date_sub_dir):
            print('create sub link')
            os.symlink(src_date_sub_dir, data_date_sub_dir)
        else:
            data_zip=os.path.join(data_date_dir,basename)
            print("data_zip=%s"%data_zip)
            if not os.path.isfile(data_zip):
                print('download now')
                filename=wget.download(mfile, out=data_date_dir)
        
        
