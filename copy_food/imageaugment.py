#!/usr/bin/env python2
from imgaug import augmenters as iaa
from optparse import OptionParser
import numpy as np
import cv2
import sys
import os

def parse_args():
    parser = OptionParser(usage='%prog [OPTIONS]')
    parser.add_option("-s", "--source", dest="sourcepath", default="./", help='The source path where your images in, will be processed later. default path is "%default".')
    parser.add_option("-d", "--dest", dest="destinationpath", default="./after_process/", help='The destination path where you want to store the images after processing. default path is "%default".')
    options, args = parser.parse_args()
    print(options.sourcepath)
    if ('./' and '/') not in options.sourcepath:
        parser.error('-s options requires a acceptable path name. like "./" or "/" ')
    if len(args) > 0:
        parser.error('Do not need to type any arguments in this application.')
    
    return options

seq = iaa.Sequential([
    iaa.Crop(px=(0, 16)), # crop images from each side by 0 to 16px (randomly chosen)
    iaa.Fliplr(0.5), # 0.5 is the probability, horizontally flip 50% of the images
    iaa.GaussianBlur(sigma=(3.0, 5.0)) # blur images with a sigma of 0 to 3.0
])

def main():
    options = parse_args()
    if not os.path.exists(options.sourcepath): print('this source path not exist !!'); return
    try:
        os.mkdir(options.destinationpath)
    except OSError, e:
        if e.errno != os.errno.EEXIST:
            raise
    image_list = []
    for img_name in os.listdir(options.sourcepath):
        if ".jpg" in img_name:
            image_list.append(img_name)
    ## load single image
    #for img_name in image_list:        
    #    image = cv2.imread(options.sourcepath+"/"+img_name, cv2.IMREAD_COLOR)
    #    image = seq.augment_image(image)  
    #    cv2.imwrite(options.destinationpath+"/copy_"+img_name, image)
    #    print(img_name+" has been completed")
   
    ## load multiple image
    images = np.empty((len(image_list),512,512,3))
    for i in range(0, len(image_list)):
        images[i] = cv2.imread(options.sourcepath+"/"+image_list[i], cv2.IMREAD_COLOR)
    print(images.shape)
    images = seq.augment_images(images)
    for i in range(0, len(image_list)):
        cv2.imwrite(options.destinationpath+"/"+image_list[i], images[i])
    print("All images under "+options.sourcepath+" have been completed--------------")
    

    

#images = np.random.randint(0, 255, (16, 128, 128, 3), dtype=np.uint8)
#images = cv2.imread('binoculars-cc0.jpeg',cv2.IMREAD_COLOR)
#cv2.imshow('image', images)
#images = seq.augment_image(images)
#cv2.imshow('image2', images)
#cv2.waitKey(0)

if __name__ == "__main__":
    main()
