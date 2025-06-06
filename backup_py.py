# src directory and optional src file
# dst directory and file (optional) add current date adding to the folder

import shutil
import time
from datetime import date
import os
import sys
os.chdir(sys.path[0])
def make_backup(src_dir='.', src_file_name=None, dst_dir='', dst_file_name=None):
    today = date.today()
    date_format = today.strftime("_%d_%b_%Y_")
    try:

        if src_file_name:
            src_dir = src_dir + src_file_name
        else:
            print("You didn't give a name of file, so we'll work on whole directory")
        try:
            if dst_file_name and dst_dir:
                arc = dst_file_name
                dst_dir = dst_dir + date_format
                if not os.path.exists(dst_dir):
                    os.makedirs(dst_dir)
                shutil.copy2(src_dir, dst_dir)
                time.sleep(5)
                shutil.make_archive(arc, 'zip', dst_dir)
                print("Backup Succeeded!")

            elif dst_dir:
                dst_dir = dst_dir + date_format
                if os.path.exists(dst_dir):
                    shutil.rmtree(dst_dir)
                shutil.copy2(src_dir, dst_dir)
                print("Backup Succeeded!")

        except FileNotFoundError:
            print("File does not exist!,\
                  please give the complete path")
    except PermissionError:
        if dst_dir and dst_file_name:
            if dst_dir:
                shutil.rmtree(dst_dir)
            arc = dst_file_name
            # dst_dir = dst_dir + date_format
            shutil.copytree(src_dir, dst_dir)
            shutil.make_archive(arc, 'gztar', dst_dir)
        else:
            # dst_dir = dst_dir + date_format
            shutil.copytree(src_dir, dst_dir)

make_backup(dst_dir="backup", dst_file_name='archived')