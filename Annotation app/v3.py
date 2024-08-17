import os
import cv2

import numpy as np
import matplotlib.pyplot as plt

# first version: taking 1 ROI from each image and saving it in txt file
# second version : we want multiple ROI per image

imagefol = "C:/Users/HP/Documents/.vscode/Edge AI/Annotation app/Images"
annotationsfol = "C:/Users/HP/Documents/.vscode/Edge AI/Annotation app/Labels"

imlist = os.listdir(imagefol) # will have the image names

font = cv2.FONT_HERSHEY_COMPLEX
fontscale = 1
color = (0, 0, 255)
thickness = 2

colorperson = (255, 0, 0)
colorcar = (0, 255, 0)
for im in imlist :
    img = cv2.imread(os.path.join(imagefol, im)) #image is a 3d array containing the RGB image
    #number of bits for the image = rows * columns * 3 * 8
    #RGB 2 gray is not equally weighted
    
    org = (500, 20)
    img = cv2.putText(img, "car", org, font, fontscale, color, thickness, cv2.LINE_AA)
    
    org = (1000, 20)
    img = cv2.putText(img, "person", org, font, fontscale, color, thickness, cv2.LINE_AA)

    org = (100, 20)
    img = cv2.putText(img, "exit", org, font, fontscale, color, thickness, cv2.LINE_AA)
    
    frame = im[:-4]
    #incase your ext is jpeg/tiff you can use frame = im.split(".")[0]
    dst_txt = frame + '.txt'
    
    imb = np.array(img)
    
    with open(os.path.join(annotationsfol, dst_txt), 'r') as f:
        for i in f:
            j = i.split(' ')
            s, x1, y1, x2, y2 = j[0], j[1], j[2], j[3], j[4]
            #print(s, x1, x2, y1, y2)
            if s == 'person':
                color = colorperson
            else :
                color = colorcar
            img = cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), color, thickness= 5)
    
    plt.imshow(img)
    plt.show()

# Take an image and its label (txt file you created with selectroi)
# Display the bb on the image using the txt file using cv2.rectangle
# Now allow the user to add more bb and edit the image