import cv2 as cv 
import numpy as np

print("hello")
ls = cv.imread("chicky_512.png", 0)
arr = np.array(ls)
print(arr)