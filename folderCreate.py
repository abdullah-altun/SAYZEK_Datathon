import shutil
from sklearn.model_selection import train_test_split
import glob
import argparse
import os

def dataCreate(mainPath,toPath):
    trainData,validData = train_test_split(glob.glob(f"{mainPath}/images/**"),test_size=0.33,random_state=42)

    if not(os.path.exists(f"{toPath}")):
        os.mkdir(f"{toPath}")
    if not(os.path.exists(f"{toPath}/train")):
        os.mkdir(f"{toPath}/train")
        os.mkdir(f"{toPath}/train/images")
        os.mkdir(f"{toPath}/train/labels")

    if not(os.path.exists(f"{toPath}/valid")):
        os.mkdir(f"{toPath}/valid")
        os.mkdir(f"{toPath}/valid/images")
        os.mkdir(f"{toPath}/valid/labels")

    for path in trainData:
        name = path.split("/")[-1][:-4]
        labelPath = f"{mainPath}/labels/{name}.txt"
        labelToPath = f"{toPath}/train/labels/{name}.txt"
        imageToPath = f"{toPath}/train/images/{name}.png"
        shutil.copy(path,imageToPath)
        shutil.copy(labelPath,labelToPath)

    for path in validData:
        name = path.split("/")[-1][:-4]
        labelPath = f"{mainPath}/labels/{name}.txt"
        labelToPath = f"{toPath}/valid/labels/{name}.txt"
        imageToPath = f"{toPath}/valid/images/{name}.png"

        shutil.copy(path,imageToPath)
        shutil.copy(labelPath,labelToPath)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Folder Create")
    parser.add_argument("--path",type=str,help="Dosyanın yolu")
    parser.add_argument("--folder_name",type=str,help="Dosyanın yolu")

    args = parser.parse_args()
    dataCreate(args.path,args.folder_name)