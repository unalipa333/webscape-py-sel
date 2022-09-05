#Pillow is an image editing library in python. 
import os 
from PIL import Image, ImageEnhance, ImageFilter

path = './imgs'
pathOut = '/editedImgs'

for filename in os.listdir(path):
    