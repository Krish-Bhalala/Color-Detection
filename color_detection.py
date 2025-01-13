import cv2

# for VideoCapture(<webcam Number>) we will have to specify the webcam id, by default the main/primary webcam is assigned 0 and reast as 1,2,3,....
webcam = cv2.VideoCapture(0)

# Now we will display the frames/pictures captured by the webcam for approx every 1ms (usually faster than that)
while True:
    # READING FRAME
    ret, frame = webcam.read()

    # PROCESSING FRAME
    
    # DISPLAYING FRAME 
    cv2.imshow("processed frame", frame)

    # CLOSING THE WEBCAM 
    # we will display current frome for 1ms and close the current frame 
    # for closing webcam, we will wait for an interrupt from keyboard (specifically char 'q') to close the webcame loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 



