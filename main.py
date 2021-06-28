import cv2
import time
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import cvzone
import pyfakewebcam

# Capture the image and set the size
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4,480)

# load the images
harput = cv2.imread("images/harput.jpg")
bursa = cv2.imread("images/bursa.jpg")
tirebolu = cv2.imread("images/harput.jpg")

# resize the images
resized_image_harput = cv2.resize(harput, (640, 480),interpolation = cv2.INTER_AREA) 
resized_image_tirebolu = cv2.resize(bursa, (640, 480),interpolation = cv2.INTER_AREA) 
resized_image_bursa = cv2.resize(tirebolu, (640, 480),interpolation = cv2.INTER_AREA) 

#init cvzone fpsreader
fpsReader = cvzone.FPS()

#init selfie segmentator
segmentor = SelfiSegmentation()

#init fake webcam
camera = pyfakewebcam.FakeWebcam('/dev/video4', 640, 480)

while True:

    success, frame = cap.read()

    #segment the image
    segmented = segmentor.removeBG(frame, resized_image_harput, threshold=0.8)


    # imgStacked = cvzone.stackImages([segmented,frame], 2,1)

    #fpsreader if needed 
    # _, imgStacked = fpsReader.update(imgStacked, color=(0,0,255))
    
    # cv2.imshow("image", imgStacked)
    # cv2.imshow("image", resized_image_harput)
    
    # cv2.imshow("segmented", segmented)

    #fix the colors
    converted = cv2.cvtColor(segmented,cv2.COLOR_BGR2RGB)

    #put segmented and converted image into the fake webcam
    camera.schedule_frame(converted)

    time.sleep(1/30.0)
    # cv2.imshow("image", frame)
    cv2.waitKey(1)

