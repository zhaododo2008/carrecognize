import os
from core import img_math
from core import img_function as predict
import cv2
from PIL import Image, ImageTk
import time


def get_millis():
    millis = int(round(time.time() * 1000))
    return millis


def handle_uploaded_file(f):
    settings_dir = os.path.dirname(__file__)
    PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
    CURRENT_IMAGE = "file/%s.jpg" % (get_millis())
    IMGFILES_FOLDER = os.path.join(PROJECT_ROOT, CURRENT_IMAGE)

    with open(IMGFILES_FOLDER, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    car = RecognizeCar()
    car.pic_path = IMGFILES_FOLDER
    car.from_pic()


    if os.path.exists(IMGFILES_FOLDER):
        os.remove(IMGFILES_FOLDER)


class RecognizeCar:
    pic_path = ""
    viewhigh = 600
    viewwide = 600
    update_time = 0
    thread = None
    thread_run = False
    camera = None
    color_transform = {"green": ("绿牌", "#55FF55"), "yello": ("黄牌", "#FFFF00"), "blue": ("蓝牌", "#6666FF")}

    def __init__(self):
        self.predictor = predict.CardPredictor()
        self.predictor.train_svm()

    def from_pic(self):
            self.thread_run = False
            if self.pic_path:
                img_bgr = img_math.img_read(self.pic_path)
                first_img, oldimg = self.predictor.img_first_pre(img_bgr)

                r_c, roi_c, color_c = self.predictor.img_color_contours(first_img, oldimg)
                r_color, roi_color, color_color = self.predictor.img_only_color(oldimg, oldimg, first_img)

                print(r_c, r_color)
