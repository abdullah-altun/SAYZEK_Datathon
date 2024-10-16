import os
import glob
import cv2
import numpy as np

from ultralytics import YOLO


import json
from pycocotools.coco import COCO

annotation_file_path = 'annotations/train.json'

coco_ann = COCO(annotation_file=annotation_file_path)
imgfile2imgid = {coco_ann.imgs[i]['file_name']: i for i in coco_ann.imgs.keys()}

with open('image_file_name_to_image_id.json', 'w') as f:

   json.dump(imgfile2imgid, f)

image_file_name_to_image_id = json.load(open('image_file_name_to_image_id.json'))
results = []



colors = {"build":(0,0,0),"silo":(0,0,255),"road":(0,255,0),"futbol":(255,0,0)}
categors = {"build":1,"silo":4,"road":2,"futbol":3}

roadModel = YOLO("models/road.pt")
builModel = YOLO("models/build.pt")
siloModel = YOLO("models/silo.pt")
futbolModel = YOLO("models/futbol.pt")


def process_detection(model,modelName,frame,img_id):
    global resultsJson
    results = model(frame)

    frameAlt = frame.copy()
    con = frame.shape[0]
    frameAlt = cv2.resize(frameAlt,(512,512))
    for result in results:
        boxes = result.boxes.cpu().numpy()
        for box in boxes:
            r = box.xyxy[0].astype(int)
            color = colors[modelName]

            score = box.conf.item()

            x1,y1,x2,y2 = r
            cv2.rectangle(frame,(x1,y1),(x2,y2),color,1)

            if con == 1024:
                x1 = int(x1/2)
                x2 = int(x2/2)
                y1 = int(y1/2)
                y2 = int(y2/2)

            width = x2-x1
            height = y2-y1
            bbox = np.array([x1,y1,width,height])
            label = categors[modelName]
            res = {

           'image_id': img_id,
           'category_id': int(label),
           'bbox': list(bbox.astype('float64')),
           'score': float("{:.8f}".format(score))
            }

            resultsJson.append(res)
                    
            # cv2.rectangle(frameAlt,(x1,y1),(x2,y2),color,1)

    return frame,frameAlt

imageIdx = 1
resultsJson = []
for path in glob.glob("images/**"):
    name = path.split("/")[-1][:-4]
    img = cv2.imread(path)
    width = int(img.shape[1] * 2)
    height = int(img.shape[0] * 2)
    new_dimensions = (width, height)
    
    resized_image = cv2.resize(img, new_dimensions, interpolation=cv2.INTER_CUBIC)
    img_id = image_file_name_to_image_id[path.split("/")[-1]]

    resized_image,alt = process_detection(builModel,"build",resized_image,img_id)
    resized_image,alt= process_detection(futbolModel,"futbol",resized_image,img_id)
    resized_image,alt = process_detection(siloModel,"silo",resized_image,img_id)
    resized_image,alt = process_detection(roadModel,"road",resized_image,img_id)

    
    
    
    cv2.imshow("image",resized_image)
    # cv2.imshow("image2",alt)

    
    if cv2.waitKey(1) == "q":
        break

cv2.destroyAllWindows()


with open('your_name.json', 'w') as f:
   json.dump(resultsJson, f)