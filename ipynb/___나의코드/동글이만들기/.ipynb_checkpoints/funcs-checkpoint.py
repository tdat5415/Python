import numpy as np
from PIL import Image, ImageFont, ImageDraw, ImageChops


def get_opt(temp, img1, img2, mask, w, h):
    i = np.random.randint(-1*w, w+1)
    j = np.random.randint(-1*h, h+1)
    
    image_trans = ImageChops.offset(img2, i, j)

    temp_img = Image.blend(img1, image_trans, alpha=0.5) #이미지 겹쳐본다
    temp_img = np.array(temp_img)
    for k in range(130, 256):
        if k in temp_img:
            return None

    temp_img = Image.blend(mask, image_trans, alpha=0.5) #이미지 겹쳐본다
    temp_img = np.array(temp_img)
    for k in range(130, 256):
        if k in temp_img:
            return None
        
    d = np.linalg.norm([i,j]) # 유클리드 거리


    return i, j, d
