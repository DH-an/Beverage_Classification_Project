import os
from PIL import Image
import torch
from tqdm import tqdm

IMG_FORMATS = ['.jpg', '.png', '.JPG', '.PNG']


def image_file_list(image_folder_path):
    # 폴더에서 파일 서치하는 함수

    all_root = []
    for (path, dir, files) in os.walk(image_folder_path):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext in IMG_FORMATS:
                root = os.path.join(path, filename)
                all_root.append(root)
            else:
                print('no image found...')
                continue

    return all_root


def expand2square(pil_image, background_color):
    width, height = pil_image.size
    if width == height:
        return pil_image
    elif width > height:
        result = Image.new(pil_image.mode, (width, width), background_color)
        result.paste(pil_image, (0, (width-height) // 2))
        return result
    else:
        result = Image.new(pil_image.mode, (height, height), background_color)
        result.paste(pil_image, ((height-width) // 2, 0))
        return result