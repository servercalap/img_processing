import cv2
import numpy as np
import math


def hsi_to_rgb(img):
    img = img.astype(float) / 255

    RGB_img = np.empty((img.shape[0],img.shape[1],3),float)

    #create empty hsi array

    H = np.empty([img.shape[0],img.shape[1]],dtype=float)
    S = np.empty([img.shape[0],img.shape[1]],dtype=float)
    I = np.empty([img.shape[0],img.shape[1]],dtype=float)

    #create empty rgb array

    r = np.empty([img.shape[0],img.shape[1]],dtype=float)
    g = np.empty([img.shape[0],img.shape[1]],dtype=float)
    b = np.empty([img.shape[0],img.shape[1]],dtype=float)



    for i in range(img.shape[0]):
        for j in range(img.shape[1]):

            H[i,j] = img[i,j][0]
            S[i,j] = img[i,j][1]
            I[i,j] = img[i,j][2]

            if 0<= H[i,j] < 2/3 * math.pi:
                b[i,j] = I[i,j] * (1-S[i,j])
                r[i,j] = I[i,j] * (1+(S[i,j]*math.cos((H[i,j]))/(math.cos(math.pi/3-H[i,j]))))
                g[i,j] = (3*I[i,j] - (r[i,j] + b[i,j]))

            elif ((2/3 *math.pi <= H[i,j]< 4/3 * math.pi)):
                r[i,j] = np.multiply(I[i,j],np.subtract(1-S[i,j]))
                g[i,j] = I[i,j]*(1+((S[i,j]*math.cos((H[i,j] - (2/3*math.pi)))) / (
                        math.cos(math.pi / 3 - (H[i, j] - (2 / 3 * math.pi))))))
                b[i,j] = (3*I - (r[i,j]+g[i,j]))
            elif ((4/3*math.pi<= H[i,j] < 2*math.pi)):
                g[i,j] = I*(1-s[i,j])
                b[i,j] = I*(1+ ((s[i,j] * math.cos((H[i,j]-(4/3*math.pi)))) / (
                         math.cos(math.pi/3 - H[i,j]-(4/3*math.pi)))))
                r[i,j] = (3*I - (g[i,j] + b[i,j]))

    #RGB_img = cv2.merge((r*255,g*255,b*255))
    RGB_img[..., 0] = r * 255
    RGB_img[..., 1] = g * 255
    RGB_img[..., 2] = b * 255

    return RGB_img
