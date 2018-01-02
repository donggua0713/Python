

import os, stat, re

for files in (os.listdir("C:\\Users\\dongdong.yu\\Documents")):
    if 'txt' in files:
        print(os.getcwd() + '\\' + files)
