import os
import glob
import cv2
import numpy as np

from ultralytics import YOLO



colors = {"build":(0,0,0),"silo":(0,0,255),"road":(0,255,0),"futbol":(255,0,0)}

builModel = YOLO("models/build.pt")
siloModel = YOLO("models/silo.pt")
futbolModel = YOLO("models/futbol.pt")


def process_detection(model,modelName,frame):
    results = model(frame)

    for result in results:
        boxes = result.boxes.cpu().numpy()
        for box in boxes:
            r = box.xyxy[0].astype(int)
            color = colors[modelName]

            x1,y1,x2,y2 = r
            cv2.rectangle(frame,(x1,y1),(x2,y2),color,1)
    return frame


for path in glob.glob("data/Test/images/**"):
    name = path.split("/")[-1][:-4]
    img = cv2.imread(path)
    width = int(img.shape[1] * 2)
    height = int(img.shape[0] * 2)
    new_dimensions = (width, height)
    resized_image = cv2.resize(img, new_dimensions, interpolation=cv2.INTER_CUBIC)

    resized_image = process_detection(builModel,"build",resized_image)
    resized_image = process_detection(futbolModel,"futbol",resized_image)
    resized_image = process_detection(siloModel,"silo",resized_image)
    
    cv2.imshow("image",resized_image)
    
    if cv2.waitKey(1000) == "q":
        break

cv2.destroyAllWindows()
