import cv2
from keras.models import Model
import keras.backend as K
from keras.applications import vgg16
from keras.models import Model
import numpy as np
import pdb

def preprocess_img(img):
	img = np.expand_dims(img, axis=0)
	img = vgg16.preprocess_input(img)
	# caffe: will convert the images from RGB to BGR,
    # then will zero-center each color channel with
    # respect to the ImageNet dataset, without scaling.
	# converts the image to -1 and 1
	return img

def deprocess_img(x,img_nrows, img_ncols):

	x = x.reshape((img_nrows, img_ncols, 3))
	x[:, :, 0] += 103.939
	x[:, :, 1] += 116.779
	x[:, :, 2] += 123.68
	x = x.astype(np.float32)
	x = np.clip(x, 0, 255).astype('uint8')
	return x

def dilate_mask(mask):
	loose_mask = cv2.GaussianBlur(mask, (35,35) , 35/3)
	loose_mask[loose_mask>=0.1] = 1
	return loose_mask
