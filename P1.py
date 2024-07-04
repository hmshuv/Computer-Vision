import cv2 as cv 
import numpy as np


img  = cv.imread("chicky_512.png", 0) 

print(img)

cv.imshow("your image", img)

cv.waitKey(1)

cv.destroyAllWindows()

cv.imwrite("chicky_copy.png", img)