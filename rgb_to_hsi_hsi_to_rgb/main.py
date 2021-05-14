import cv2
from rgb_to_hsi import RGB_TO_HSI
import hsi_to_rgb

path = "/Users/calap/img_processing/Lenna.png"
img = cv2.imread(path,1)
hsi = rgb_to_hsi.RGB_TO_HSI(img)
rgb = hsi_to_rgb.hsi_to_rgb(hsi)


cv2.imshow('Orjinal Img', img)
#Display hsv img
#Display rgb img

cv2.imshow("HSI Img",hsi)
cv2.imshow("HSi to rgb", rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
