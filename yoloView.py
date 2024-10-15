import cv2
import os
import glob

import utils as ut

dataPath = glob.glob("data/DataCategori/train/images/**")

idx = 0
colors = {"0":(0,0,0),"1":(255,0,0),"2":(0,255,0),"3":(0,0,255)}
while True:
    img = cv2.imread(dataPath[idx])
    name = dataPath[idx].split("/")[-1][:-4]
    labelPath = f"data/DataCategori/train/labels/{name}.txt"
    
    with open(labelPath,"r") as f:
        data = f.read()
    f.close()
    
    h,w = img.shape[1],img.shape[0]
    for bbox in data.split("\n"):
        
        if len(bbox) > 0:
            categori = bbox.split(" ")[0]
            color = colors[categori]
            xmin, ymin, xmax, ymax = ut.yolo_label_to_coco(bbox.split(" ")[1:],w,h)
            img = cv2.rectangle(img,(xmin,ymin),(xmax,ymax),color,1)

    text = f"{idx}/{len(dataPath)}"
    img = cv2.putText(img,text,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)
    cv2.imshow("image",img)

    if cv2.waitKey(10) == ord("q"):
        break
    elif cv2.waitKey(10) == ord("d"):
        idx += 1
        if idx > len(dataPath)-1:
            idx = 0

    elif cv2.waitKey(10) == ord("a"):
        idx -= 1
        if idx < 0:
            idx = len(dataPath) -1

    