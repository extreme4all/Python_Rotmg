import numpy as np
from PIL import ImageGrab
import cv2
import time
from key_input import VK_CODE, press, pressAndHold, pressHoldRelease, release, typer

def roi(img,vertices):
    # region of interest
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices,255)
    masked = cv2.bitwise_and(img, mask)
    return masked

def process_img(original_image):
    processed_img= cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img,threshold1=200,threshold2=300)
    # roi stuf
    vertices = np.array([[0,0],[600,0],[600,600],[0,600]])
    processed_img = roi(processed_img,[vertices])
    return processed_img

def screen_record(): 
    last_time = time.time()
    while(True):
        # 800x600 windowed mode
        screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        new_screen = process_img(screen)
        #print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window',new_screen)
        #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

screen_record()
