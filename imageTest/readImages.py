import os
import cv2 as cv

test_files = []
DirPath = os.getcwd()#I'm a bit confused here
Files = os.listdir(DirPath)
for File in Files:
    imgPath = os.path.join(DirPath, File)
    print(imgPath)
    image = cv.imread(imgPath, cv.IMREAD_ANYCOLOR)
    cv.imshow('image', image)
    cv.waitKey(0)
    test_files.append(image)

cv.destroyAllWindows()
