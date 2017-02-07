import os
from os.path import basename

gfiles = []

def find_files():
    for root, dirnames, files in os.walk("/Users/smitaldesai/Desktop/Resources/group_13_2017-02-03"):
        for file in files:
            if file.startswith("group_"):
               gfiles.append(os.path.join(root, file))


find_files()

for file in gfiles:
    print os.path.dirname(file) +"/" + basename(file)
    print os.path.dirname(file) + "/ico_new_food_placeholder.png"
    os.rename(file, os.path.dirname(file) + "/ico_new_food_placeholder.png")