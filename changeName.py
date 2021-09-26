import os
import shutil


sourcePath = 'E:\\projects\\002slyy-mbxt\\04Coding\\source'
targetPath = 'E:\\projects\\002slyy-mbxt\\04Coding\\target'

# 文件夹不存在时，创建
def mk_save_dir(path):
    if not os.path.exists(path):
        # 不存在则创建
        os.mkdir(path)
    # else:
    #     # 存在时，清空文件夹
    #     rm_files = 'rm -rf ' + path + '/*'
    #     res = os.system(rm_files)
    #     if res == 0:
    #         print("清空文件夹" + path + "成功")
    #     pass


def rename(source_dir, target_dir):
    filelist = os.listdir(source_dir)
    for file in filelist:
        oldFile = os.path.join(source_dir, file)
        # if path is folder, traversal it
        if os.path.isdir(oldFile):
            # 新建target对应子文件夹
            newDir = os.path.join(targetPath, file)
            if not os.path.exists(newDir):
                os.mkdir(newDir)
            rename(oldFile, os.path.join(targetPath, file))
        # else is file, rename
        ## has '-'
        if file.find('-') >= 0:
            file = file.replace('-', '_')
        if os.path.isdir(oldFile):
            continue
        newFile = os.path.join(target_dir, file)
        shutil.copyfile(oldFile, newFile)


if __name__ == '__main__':
    mk_save_dir(targetPath)
    rename(sourcePath, targetPath)

    print("转换完成！")