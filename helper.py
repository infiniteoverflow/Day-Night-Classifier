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

def standardize_image(image):
    '''Resizes the image to (600x1100) size'''
    return cv2.resize(image,(1100,600))

def encode(label):
    '''Provide numerical value to each label
    day = 1,
    night=0
    '''
    numerical_val = 0
    if label == "Day":
        numerical_val = 1

    return numerical_val

def standardize(image_list):
    ''' Integrates the standardize_image and encode functions
    to standardize the complete list of images'''
    standard_list = []

    for item in image_list:
        image = item[0]
        label = item[1]

        image = standardize_image(image)
        label = encode[label]

        standard_list.append((image,label))

    return standard_list
