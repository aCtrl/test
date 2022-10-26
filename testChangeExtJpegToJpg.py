"""
递归将某个磁盘目录下的jpeg文件的扩展名修改为jpg
Author: 吴伽锐
e-mail: 82683619@qq.com
git:    https://github.com/aCtrl/testPython.git
"""

import os

PATH = r'.'     # 文件所在目录


def change_jpeg_to_jpg():
    """
    将目录下的jpep文件扩展名改为jpg
    """
    files_list = os.listdir(PATH)   # 获取目录下所有文件的名称

    # 遍历所有文件并将.jpep文件改为.jpg
    for file in files_list:
        file_name_split_list = file.split('.')
        if file_name_split_list[-1] == 'jpeg':          # 判断扩展名是否为jpeg
            file_name_split_list[-1] = 'jpg'            # 将扩展名jpeg改为jpg
            new_file = '.'.join(file_name_split_list)   # 新文件名
            new_file_path = PATH + r'\\' + new_file     # 新文件名全路径
            os.renames(file, new_file_path)             # 重命名
            print(file + r' --> ' + new_file)


if __name__ == '__main__':
    change_jpeg_to_jpg()

