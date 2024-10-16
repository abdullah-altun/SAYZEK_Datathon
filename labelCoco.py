import json
import os
import glob

import shutil
import utils as ut

from sklearn.model_selection import train_test_split


trainData,validData = train_test_split(glob.glob("data/satim-bicubic/train/labels/**"),test_size=0.33,random_state=42)
validData = glob.glob("data/normal/valid/labels/**")
trainlabelJson = {
    "info":
    {
        "contributor": "",
        "date_created": "",
        "description": "",
        "url": "",
        "version": "",
        "year": ""
    },

    "licenses":[
        {
            "name": "",
            "id": 0,
            "url": ""
        }
    ],
    "images":
    [

    ],

    "annotations":
    [

    ],

    "categories": [
        {
            "id": 1,
            "name": "bina",
            "supercategory": ""
        },
        {
            "id": 2,
            "name": "yol_kesisim",
            "supercategory": ""
        },
        {
            "id": 3,
            "name": "futbol_sahasi",
            "supercategory": ""
        },
        {
            "id": 4,
            "name": "silo",
            "supercategory": ""
        }
    ]
}

validlabelJson = {
    "info":
    {
        "contributor": "",
        "date_created": "",
        "description": "",
        "url": "",
        "version": "",
        "year": ""
    },

    "licenses":[
        {
            "name": "",
            "id": 0,
            "url": ""
        }
    ],
    "images":
    [

    ],

    "annotations":
    [

    ],

    "categories": [
        {
            "id": 1,
            "name": "bina",
            "supercategory": ""
        },
        {
            "id": 2,
            "name": "yol_kesisim",
            "supercategory": ""
        },
        {
            "id": 3,
            "name": "futbol_sahasi",
            "supercategory": ""
        },
        {
            "id": 4,
            "name": "silo",
            "supercategory": ""
        }
    ]
}

w,h = 1024,1024
labelIdx = 1
imageIdx = 1

if not(os.path.exists("data/CocoFormat/train")):
    os.mkdir("data/CocoFormat/train")
if not(os.path.exists("data/CocoFormat/valid")):
    os.mkdir("data/CocoFormat/valid")

def jsonRead(labelJson,labelData,folderName):
    global imageIdx,labelIdx
    for path in labelData:
        name = path.split("/")[-1][:-4]
        imagePath = f"data/normal/valid/images/{name}.png"
        imageToPath = f"data/CocoFormat/{folderName}/{name}.png"
        shutil.copy(imagePath,imageToPath)
        imagesDict = {
            "id": imageIdx,
            "width": 1024,
            "height": 1024,
            "file_name": f"{name}.png",
            "license": 0,
            "flickr_url": "",
            "coco_url": "",
            "date_captured": 0
        }
        labelJson["images"].append(imagesDict)
        
        with open(path,"r") as f:
            labelData = f.read()
        f.close()
        labelList = []
        for label in labelData.split("\n"):
            category = label.split(" ")[0]
            if len(label)>0:
                xmin, ymin, xmax, ymax = ut.yolo_label_to_coco(label.split(" ")[1:],w,h)
                labelDict = {
                    "id": labelIdx,
                    "image_id": imageIdx,
                    "category_id": int(category)+1,
                    "segmentation": [],
                    "area":(xmax-xmin)*(ymax-ymin),
                    "bbox": [
                        xmin,
                        ymin,
                        (xmax-xmin),
                        (ymax-ymin)
                    ],
                    "iscrowd":0,
                    "attributes": {
                        "occluded": False,
                        "rotation": 0.0
                    }
                }
                labelJson["annotations"].append(labelDict)
                labelIdx += 1
            imageIdx += 1
    jsonPath = f"data/CocoFormat/{folderName}.json"
    with open(jsonPath,"w") as f:
        json.dump(labelJson,f)
    f.close()

# jsonRead(trainlabelJson,trainData,"train")
jsonRead(validlabelJson,validData,"valid")