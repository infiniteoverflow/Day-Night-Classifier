import os
import glob
import matplotlib.image as mping
import cv2

def load_dataset(image_dir):
    ''' Loads the images from the image_dir path'''
    im_list = []
    image_type = ["day","night"]

    for im_type in image_type:
        for file in glob.glob(os.path.join(image_dir,image_type,"*")):
            im = mping.imread(file)

            if not im is None:
                im_list.append((im,im_type))

    return im_list

