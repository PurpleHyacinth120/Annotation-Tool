#In the first week we explored the selectROI function and built a labeling app.
#Our app will generate rectangular bounding boxes for any number of regions, any categories.
#We also know basics about image depth, how to read images and display them etc.
# In this week, we will generate polygon regions, segmentation labeling and also learn basic image manipulations

import os
import sys

import numpy as np
import cv2
import matplotlib.pyplot as plt

imagefol = "C:/Users/HP/Documents/.vscode/Edge AI/Annotation app/Images"
annotationsfol = "C:/Users/HP/Documents/.vscode/Edge AI/Annotation app/Labels"
segmentfol = 'C:/Users/HP/Documents/.vscode/Edge AI/Annotation app/Segmented'

if not os.path.exists(segmentfol):
    os.makedirs(segmentfol)

font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
color = (0, 0, 255)
thickness = 2
# org1 = (0, 40)
org2 = (500, 50)
org3 = (1000, 50)
org4 = (1500, 50)
colorcar = (255, 150, 255)
colorperson = (255, 150, 15)

imlist = os.listdir(imagefol) # will have the image names

for imag in imlist:
    
    im = cv2.imread(os.path.join(imagefol, imag))

    # im = cv2.putText(im, "next_roi", org1, font, fontScale, color, thickness, cv2.LINE_AA)
    # im = cv2.rectangle(im, (0, 10), (30, 30), color, -1)
    
    im = cv2.putText(im, "next_image", org2, font, fontScale, color, thickness, cv2.LINE_AA)
    im = cv2.rectangle(im, (500, 10), (530, 30), color, -1)

    im = cv2.putText(im, "car", org3, font, fontScale, color, thickness, cv2.LINE_AA)
    im = cv2.rectangle(im, (1000, 10), (1030, 30), color, -1)

    im = cv2.putText(im, "person", org4, font, fontScale, color, thickness, cv2.LINE_AA)
    im = cv2.rectangle(im, (1500, 10), (1530, 30), color, -1)

    
    plt.imshow(im)
    frame = imag[:-4]
    
    imb = np.zeros_like(im) # imb is a black image of same size as im
    #imb = np.ones_like(im)
    #imb = imb *255 # imb is a white image of same size as im
    
    dst_txt = frame + '.txt' # opening txt file here, so it doesn't take time later to open for each poly
    with open(os.path.join(annotationsfol, dst_txt), 'w') as f:
        flag = 1
        while(flag) :
            pl = []
            l = 0
            
            s = '' 
            col = ()      
            while(1) :
                p = plt.ginput(1) # select a single point (x, y) and put it in p
                px, py = p[0][0], p[0][1]
                
                # if px < 50 and py < 50:
                #     #plt.close()
                #     break
                l += 1
                if px > 1000 and py > 10 and px < 1030  and py < 30:
                    s = 'car'
                    col = colorcar
                    break
                
                if px > 1500 and py > 10 and px < 1530  and py < 30:
                    s = 'person'
                    col = colorperson
                    break
                
                if px > 500 and py > 0 and px < 550  and py < 30:
                    plt.close()
                    flag = 0 # to break out of outer while loop
                    break
                pl.append((int(px), int(py)))
                
            #plt.show()
            
            #after inner while loop to draw(image) and write (txt) the poly
            if pl:
                cv2.fillPoly(imb, [np.array(pl)], color = col)
            
        #incase your ext is jpeg/tiff you can use frame = im.split(".")[0]
            f.write(s + ' ')
            for a in pl:
                f.write("(" + str(a[0]) + ', ' + str(a[1]) + ") ")
            f.write('\n')
            
    f.close()
    # after the outer while loop when all polys are written and drawn
    cv2.imwrite(os.path.join(segmentfol, frame + '.png'), imb)
    cv2.imshow('win', imb)
    cv2.waitKey() 
    cv2.destroyAllWindows()
    # run for multiple images
    # save the segmented image using cv2.imwrite()
    # try to save multiple polygons in the same image
