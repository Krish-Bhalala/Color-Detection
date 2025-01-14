import numpy as np 
import cv2

# this function will select a small sector of hsv values around the specified values, approximately 10 units in either direction of the absolute value
def get_color_limits(color):
    # convert the color value to numpy array
    color_array = np.uint8[[color]]

    # convert the color_array to hsv color
    hsv_color = cv2.cvtColor(color_array, cv2.BGR2HSV)

    # get the hue value from hsv_color
    hue_value = hsv_color[0][0][0]

    # we will  also need to handle red hue wrap-around
    if hue >= 165:  # Upper limit for divided red hue
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
            upperLimit = np.array([180, 255, 255], dtype=np.uint8)
    elif hue <= 15:  # Lower limit for divided red hue
        lowerLimit = np.array([0, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)
    else:
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit
