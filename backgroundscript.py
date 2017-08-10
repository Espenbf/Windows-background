from shutil import copy
from PIL import Image

import os

#Fix path
directory = 'C:\\Users\\Ebay\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets'

#Must exist
#This is the folder you set to run backgroud pictures from
to_dir = 'C:\\Users\\Ebay\\Documents\\background'

for filename in os.listdir(directory):
    complete_path = directory+'\\'+filename
    statinfo = os.stat(complete_path)
    size = statinfo.st_size
    new_file_path = to_dir + "\\" + filename
    if size > 1000000:
        if not os.path.isfile(new_file_path+".png"):
            im = Image.open(complete_path)
            size = im.size  # (width,height) tuple

            #Checks dimensions
            if size[0] > size[1]:
                copy(complete_path, to_dir)
                os.rename(new_file_path, new_file_path+".png")
                im = Image.open(new_file_path+".png")

