import os
from PIL import Image, ImageFilter

# fetch all the files from the source folder
dirname = 'images'
output_dirname = 'branded'
images_list = os.listdir(dirname)
logo = Image.open('logo.png')

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

    # create a copy of the image
    image_copy = original.copy()
    # obtain the position to place the logo

    position = ((image_copy.width - logo.width),
                (image_copy.height - logo.height))
    # The third parameter makes it transparent
    image_copy.paste(logo, position, logo)
    image_copy.save(f'{output_dirname}\{name}.png')
