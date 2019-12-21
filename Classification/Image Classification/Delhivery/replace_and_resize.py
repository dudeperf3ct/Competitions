from PIL import Image
import os
from tqdm import tqdm
import pandas as pd
import matplotlib.pyplot as plt

img_path = '/media/dudeperf3ct/New Volume/x_ray_image_recognition_data_updated/x_ray_image_recognition_data/x_ray_images/test_xray_images'

train_data = pd.read_csv('test.csv')

_PIL_INTERPOLATION_METHODS = {
    'nearest': Image.NEAREST,
    'bilinear': Image.BILINEAR,
    'bicubic': Image.BICUBIC,
}
def loadimg(img, target_size=(224, 224), interpolation='nearest'):
    if target_size is not None:
        width_height_tuple = (target_size[1], target_size[0])
    if img.size != width_height_tuple:
        if interpolation not in _PIL_INTERPOLATION_METHODS:
            raise ValueError(
                'Invalid interpolation method {} specified. Supported '
                'methods are {}'.format(
                    interpolation,
                    ", ".join(_PIL_INTERPOLATION_METHODS.keys())))
        resample = _PIL_INTERPOLATION_METHODS[interpolation]
        img = img.resize(width_height_tuple, resample)
    return img

def preprocess_imgs(images):
    for imgs in tqdm(images):
        img = Image.open(os.path.join(img_path, imgs))
        resized_img = loadimg(img, target_size=(224, 224), interpolation='nearest')
        resized_img.save(os.path.join(img_path, imgs))
    return ' '

x = train_data['x_ray_image_file_name']

print ('Start!!!')

train_x = preprocess_imgs(x)

print ('Done!!!!')