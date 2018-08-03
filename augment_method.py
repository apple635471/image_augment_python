from imgaug import augmenters as iaa

def method1():
    seq = iaa.Sequential([
        #iaa.Crop(px=(0, 16)), # crop images from each side by 0 to 16px (randomly chosen)
        #iaa.Fliplr(0.5), # 0.5 is the probability, horizontally flip 50% of the images
        #iaa.GaussianBlur(sigma=(3.0, 5.0)) # blur images with a sigma of 0 to 3.0
        iaa.AdditiveGaussianNoise(scale=0.2*255, per_channel=0.5)
    ])
    return seq
