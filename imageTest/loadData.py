import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

DATADIR = "C:\Users\vphan\Desktop\imageTest\pictures"

CATEGORIES = ['healthy','defects']

training_data = []

IMG_SIZE = 50

def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR. category)#path to healthy oy defects dir
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            img_array = cv2.imread(os.path.join(path,img))#my images are named by numbers, example: 1.jpg 2.jpg etc
            new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))#resize images so they're 50x50
            training_data.append([new_array, class_num])
            #plt.imshow(img_array)
            #plt.show()
        
create_training_data()
print(len(training_data))


