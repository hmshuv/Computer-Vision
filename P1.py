import cv2 as cv 
import numpy as np


img  = cv.imread("chicky_512.png", 0) 

print(img)

cv.imshow("your image", img)

k = cv.waitKey(0)

if k == ord('d'):
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite("chicky_copy.png", img)
    cv.destroyAllWindows()



