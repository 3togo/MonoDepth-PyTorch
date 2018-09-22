import glob, os
script_dir=os.path.dirname(os.path.abspath(__file__))
dirs=glob.glob('*/')
print(dirs)
if not os.path.isdir('kitti'):
    os.mkdir('kitti')
for mdir in dirs:
    if mdir=='kitti':
        continue
    subdirs= glob.glob(os.path.join(mdir,'*/'))
    for subdir in subdirs:
        base_dir=subdir.split('/')[-2]
        print("base_dir=[%s]"%base_dir)
        target_dir=os.path.join(script_dir, 'kitti', base_dir)
        if not os.path.islink(target_dir):
            print("create link for [%s]"%target_dir)
            os.symlink(subdir, target_dir )
        
        
