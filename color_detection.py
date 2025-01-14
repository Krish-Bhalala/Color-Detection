import cv2
from util import get_color_limits
from PIL import Image

# for VideoCapture(<webcam Number>) we will have to specify the webcam id, by default the main/primary webcam is assigned 0 and reast as 1,2,3,....
webcam = cv2.VideoCapture(0)

# the color in BGR to detect 
COLOR = [255,0,0] 

# Now we will display the frames/pictures captured by the webcam for approx every 1ms (usually faster than that)
while True:
    # READING FRAME
    ret, frame = webcam.read()

    # PROCESSING FRAME
    # first we will convert frame to HSV to better filter out our color
    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # now compute the hsv value range for creating mask
    lowerLimit, upperLimit = get_color_limits(COLOR)

    # now we will create the mask which filters out the color range 
    mask = cv2.inRange(hsv_img, lowerLimit, upperLimit)

    # now convert the image array back to array 
    mask_img = Image.fromarray(mask)

    # now create a box around the detected object mask 
    box = mask_img.getbbox()

    # now draw the box on the img 
    if box is not None:
        x1,y1,x2,y2 = box
        cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,255), 5)


    # DISPLAYING FRAME 
    cv2.imshow("processed frame", frame)

    # CLOSING THE WEBCAM 
    # we will display current frome for 1ms and close the current frame 
    # for closing webcam, we will wait for an interrupt from keyboard (specifically char 'q') to close the webcame loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 



