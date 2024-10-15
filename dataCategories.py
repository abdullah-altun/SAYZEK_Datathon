import json
import cv2
import os
import shutil
from sklearn.model_selection import train_test_split
import glob

import utils as ut

if not(os.path.exists("data/DataCategori")):
    os.mkdir("data/DataCategori")

if not(os.path.exists("data/DataCategori/train")):
    os.mkdir("data/DataCategori/train")
    os.mkdir("data/DataCategori/train/images")
    os.mkdir("data/DataCategori/train/labels")
if not(os.path.exists("data/DataCategori/valid")):
    os.mkdir("data/DataCategori/valid")
    os.mkdir("data/DataCategori/valid/images")
    os.mkdir("data/DataCategori/valid/labels")


trainData,validData = train_test_split(glob.glob("data/bicubic/images/**"),test_size=0.33,random_state=42)

for path in trainData:
    name = path.split("/")[-1][:-4]

    labelPath = f"data/bicubic/labels/{name}.txt"
    
    with open(labelPath,"r") as f:
        data = f.read()
    f.close()

    bboxtext = ""

    for bbox in data.split("\n"):
        if len(bbox) > 0:
            if int(bbox.split(" ")[0]) == 3:
                bboxtext += "1 "
                bboxtext += " ".join(bbox.split(" ")[1:])
                bboxtext += "\n"
    
    if len(bboxtext) > 0:
        imgTopath = f"data/DataCategori/train/images/{name}.jpg"

        shutil.copy(path,imgTopath)

        labelToPath = f"data/DataCategori/train/labels/{name}.txt"
        with open(labelToPath,"w") as f:
            f.write(bboxtext)
        f.close()


for path in validData:
    name = path.split("/")[-1][:-4]

    labelPath = f"data/bicubic/labels/{name}.txt"
    
    with open(labelPath,"r") as f:
        data = f.read()
    f.close()

    bboxtext = ""

    for bbox in data.split("\n"):
        if len(bbox) > 0:
            if int(bbox.split(" ")[0]) == 3:
                bboxtext += "1 "
                bboxtext += " ".join(bbox.split(" ")[1:])
                bboxtext += "\n"
    
    if len(bboxtext) > 0:
        imgTopath = f"data/DataCategori/valid/images/{name}.jpg"

        shutil.copy(path,imgTopath)

        labelToPath = f"data/DataCategori/valid/labels/{name}.txt"
        with open(labelToPath,"w") as f:
            f.write(bboxtext)
        f.close()


for path in glob.glob("data/DataCategori/**/labels/*"):
    with open(path,"r") as f:
        data = f.read()
    f.close()

    bboxText = ""
    for bbox in data.split("\n"):
        if len(bbox) > 0:
            bboxText += "0 "
            bboxText += " ".join(bbox.split(" ")[1:])
            bboxText += "\n"
            
    with open(path,"w") as f:
        f.write(bboxText)
    f.close()