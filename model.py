from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("yolov8x.pt")
    model.train(data='custom.yaml',imgsz=1024, epochs=100, batch=12)