from PIL import Image  #python image library import image processing
import glob
import os

from matplotlib import image
from numpy import quantile


dir_path = os.path.dirname(os.path.realpath(__file__)) # get directory from file
dir_path= os.path.join(dir_path, '*.png')
# print(glob.glob('D:/IT/Python/Python Automation Tutorial/image_conversion/*.png'))
print(glob.glob(dir_path))

for file in glob.glob(dir_path):
    im = Image.open(file)
    rgb_im = im.convert("RGB")
    rgb_im.save(file.replace("png", "jpg"), quality = 95)


