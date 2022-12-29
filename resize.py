# Required Libraries
import concurrent.futures

import cv2
from os import listdir
from os.path import isfile, join
import argparse

# Argument parsing variable declared
ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image",
                required=True,
                help="Path to folder")

args = vars(ap.parse_args())

# Find all the images in the provided images folder
mypath = args["image"]
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


def resize(n):
    path = join(mypath, onlyfiles[n])

    # Load the image in img variable
    img = cv2.imread(path, 1)

    # Define a resizing Scale
    # To declare how much to resize
    resize_width = 256
    resize_height = 256
    resized_dimensions = (resize_width, resize_height)

    # Create resized image using the calculated dimensions
    resized_image = cv2.resize(img, resized_dimensions, interpolation=cv2.INTER_AREA)

    # Save the image in Output Folder
    cv2.imwrite('output\\' + onlyfiles[n] + '_resized.jpg', resized_image)


# Iterate through every image
# and resize all the images.
with concurrent.futures.ThreadPoolExecutor(max_workers=64) as executor:
    for n in range(0, len(onlyfiles)):
        executor.submit(resize(n))

print("Images resized Successfully")
# python resize.py --image 'path/to/images/folder/'
# example:
# python resize.py --image 'C:\Users\Tuan\Desktop\dataset warehouse\Mountain'
