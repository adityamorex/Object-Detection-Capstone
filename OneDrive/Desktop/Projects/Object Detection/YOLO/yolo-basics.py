from ultralytics import YOLO
import cv2 as cv2

model = YOLO()  # initialize
model = YOLO('../Yolo-Weights/yolov8n.pt')  # download pretrained model
results = model("C:/Users/adity/OneDrive/Desktop/Projects/Object Detection/YOLO/Images/image1.jpg", show = True)  # run inference
cv2.waitKey(0)