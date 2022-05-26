# -*- coding: utf-8 -*-
"""Task_OpenCv.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11vxPXPUcfQVe2_sQmMEp7YRPYN7cH26S
"""



import cv2
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
image = cv2.imread(path)
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
plt.show()

# convert to hsv colorspace
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_bound = np.array([50, 20, 20])   #Green color lower bound
upper_bound = np.array([100, 255, 255]) #Green color upper bound

mask = cv2.inRange(hsv, lower_bound, upper_bound)

#define kernel size  
kernel = np.ones((7,7),np.uint8)
# Remove unnecessary noise from mask
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

segmented_img = cv2.bitwise_and(image, image, mask=mask)

contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
output = cv2.drawContours(segmented_img, contours, 1, (1, 1, 1), 0)
# Showing the output
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))