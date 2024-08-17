import os
import cv2

# first version: taking 1 ROI from each image and saving it in txt file
# second version : we want multiple ROI per image

imagefol = "C:/Users/HP/Documents/.vscode/Edge AI/Annotation app/Images"
annotationsfol = "C:/Users/HP/Documents/.vscode/Edge AI/Annotation app/Labels"

imlist = os.listdir(imagefol) # will have the image names

font = cv2.FONT_HERSHEY_COMPLEX
fontscale = 1
color = (0, 0, 255)
thickness = 2

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
            
    with open(os.path.join(annotationsfol, dst_txt), 'w') as f:
        while(1):
            r = cv2.selectROI(img) #returns x0 y0 width height
            # print(r)
            
            if r[0] < 200 and r[1] < 200: #manipulating an exit when clicked on the top left corner
                break
            
            s = ''
            r1 = cv2.selectROI(img)
            
            if r1[0] > 490 and r1[0] < 600 and r1[1] > 0 and r1[1] < 30:
                s = 'car'
            
            if r1[0] > 990 and r1[0] < 1100 and r1[1] > 0 and r1[1] < 30:
                s = 'person'
            boxess = []
            boxess = [r[0], r[1], r[0] + r[2], r[1] + r[3]] #r0 -> x0, r1 ->y0, r2 -> width, r3 -> height
            f.write(s + ' {} {} {} {}'.format(*boxess) + '\n')
            
            #there are various annotation format requirement
            #xmin ymin xmax ymax
            #xmin ymin width height
            #ymin xmin ymax xmax etc...
    f.close()    

# What did we learn?
# a. Image reading, depth of image, range of image
# b. using selectROI
# c. creating annotations with selectROI, i.e. select any number of object
# with any label from multiple images
# d. some annotation formats x0 y0 x1 y1, x0 y0 width height, y0 y1 x0 x1 etc

# label 0 0 0 x0 y1 x0 x1 in normalized coordinates
# normalized coordinates = x0/im_width, y0/im_height
# img.shape -> rows/ height, cols/ width, color channels