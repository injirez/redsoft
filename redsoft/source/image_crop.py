from PIL import Image
import os


def crop(file_path: str, left: int, top: int, right: int, bottom: int) -> bool:
    try:
        cur_path = os.path.dirname(__file__)
        file_path = cur_path[:-7] + '/' + file_path
        img = Image.open(file_path)
        box = (left, top, right, bottom)
        img_cropped = img.crop(box)
        img_cropped.save(file_path)

        return True
    except:

        return False


