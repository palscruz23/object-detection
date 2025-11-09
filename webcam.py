from ultralytics import YOLO
import cv2
import os

# Add folders if does not exist
if not os.path.exists('data'):
    os.mkdir('data')
if not os.path.exists('output'):
    os.mkdir('output')

model = YOLO('yolov8n.pt')

model.predict(source=0, 
              show=True,
              save=True,
              project='output',
              name='cam',
              exist_ok=True,
              )