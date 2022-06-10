from PIL import ImageEnhance
import os
import numpy as np
from PIL import Image


def Brightness(root_path, img_name): #亮度增强
    image = Image.open(os.path.join(root_path, img_name))
    enh_bri = ImageEnhance.Brightness(image)
    brightness = 1.5
    image_brightened = enh_bri.enhance(brightness)
    return image_brightened


def Contrast(root_path, img_name): #对比度增强
    image = Image.open(os.path.join(root_path, img_name))
    enh_con = ImageEnhance.Contrast(image)
    contrast = 1.5
    image_contrasted = enh_con.enhance(contrast)
    return image_contrasted


def crop(root_path, img_name): #随机裁剪
    img = Image.open(os.path.join(root_path, img_name))
    crop_img = img.crop((100, 100, 250, 250))
    return crop_img


def flip(root_path, img_name): #左右翻转
    img = Image.open(os.path.join(root_path, img_name))
    filp_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    return filp_img


def rotation(root_path, img_name): #随机旋转
    img = Image.open(os.path.join(root_path, img_name))
    random_angle = np.random.randint(-2, 2) * 90
    if random_angle == 0:
        rotation_img = img.rotate(-90)
    else:
        rotation_img = img.rotate(random_angle)
    return rotation_img



def createImage(imageDir, saveDir):
    for name in sorted(os.listdir(imageDir)):
        print(name)
        saveName1 = "bright" + name + ".jpg"
        saveImage1 = Brightness(imageDir, name)
        saveImage1.save(os.path.join(saveDir, saveName1))

        saveName2 = "contrast" + name + ".jpg"
        saveImage2 = Contrast(imageDir, name)
        saveImage2.save(os.path.join(saveDir, saveName2))

        saveName3 = "crop" + name + ".jpg"
        saveImage3 = crop(imageDir, name)
        saveImage3.save(os.path.join(saveDir, saveName3))

        saveName4 = "flip" + name + ".jpg"
        saveImage4 = flip(imageDir, name)
        saveImage4.save(os.path.join(saveDir, saveName4))

        saveName5 = "rotate" + name + ".jpg"
        saveImage5 = rotation(imageDir, name)
        saveImage5.save(os.path.join(saveDir, saveName5))
