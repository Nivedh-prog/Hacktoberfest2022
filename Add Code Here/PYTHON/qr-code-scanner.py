import cv2 as cv
from PIL import Image
import numpy as np


import cv2 as cv
from PIL import Image
import numpy as np
import mysql.connector
cam_port = 0
cam = cv.VideoCapture(cam_port)

result, image = cam.read()

# create a qrcode detector
detect=cv.QRCodeDetector()
if result:
    kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
    image_sharp = cv.filter2D(src=image, ddepth=-1, kernel=kernel)

    # saving image in local storage
    cv.imwrite("Qld.png", image)
    cv.imwrite("new.png", image_sharp)

    cv.waitKey(2400)
    cv.destroyAllWindows()


data,bbox,sqrcode=detect.detectAndDecode(image)

# bbox is the main thing in the qrcode
# if it exist it will give us the data
if bbox is not None:
    print(data)
else:
    data = "NULL"
    print("img not visible")
