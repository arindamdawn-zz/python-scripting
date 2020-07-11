import os
from PIL import Image

# fetch all the files from the source folder
dirname = 'images'
output_dirname = 'generated'
images_list = os.listdir(dirname)

# check if output folder exits otherwise create it
if not os.path.exists(output_dirname):
    os.makedirs(output_dirname)

for image in images_list:
    # split the filename to separate the format and name
    name, format = os.path.splitext(image)

    original = Image.open(f'{dirname}\{image}')

    # resize image to a standard size and to reduce file size
    size = 1000, 1000
    # thumbnail maintains aspect ratio
    original.thumbnail(size)

    # save image as png format
    original.save(f'{output_dirname}\{name}.png')
