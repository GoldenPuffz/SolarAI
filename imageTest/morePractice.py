import cv2
import os

images = []
path = "C:\Users\vphan\Desktop\imageTest\pictures"
for filename in os.listdir(path):
    img = cv2.imread(path)
    if img is not None:
        images.append(img)
    