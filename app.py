import streamlit as st
from ultralytics import YOLO
import cv2
import os
import numpy as np
from PIL import Image

st.set_page_config(
        page_title="YOLO Experience",
        page_icon=":eyes:",
        layout="wide",
        )

st.title("YOLO Experience")

# Apply CSS
st.markdown("""
    <style>
        [data-testid="stImage"] {
            width: 50% !important;
            margin-left: auto;
            margin-right: auto;
        }
        
        [data-testid="stImage"] > img {
            width: 100% !important;
        }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.header("Settings")
    application_mode = st.selectbox("Application", ["Object Detection", "Pose Recognition"])
    if application_mode == "Object Detection":
        model_choice = st.selectbox("Choose Model", ["yolo12n.pt", "yolov8n.pt", "yolov8m-oiv7"])
    elif application_mode == "Pose Recognition":
        model_choice = st.selectbox("Choose Model", ["yolo11n-pose.pt", "yolov8n-pose.pt"]) 

    confidence = st.slider("Confidence Threshold",
                              min_value = 0.0,
                              max_value = 1.0,
                              value = 0.5,
                              step = 0.05)
    iou = st.slider("Intersect Over Union (IoU) Threshold",
                              min_value = 0.0,
                              max_value = 1.0,
                              value = 0.5,
                              step = 0.05)

model = YOLO(model_choice)

if application_mode == "Object Detection":
    st.subheader("Detection Output")
elif application_mode == "Pose Recognition":
    st.subheader("Pose Recognition")


proc_frame = st.empty()
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # orig_frame.image(frame, channels="BGR", caption="Original")
    results = model(frame,
                    conf = confidence,
                    iou = iou, 
                    verbose=False
                    )
    
    img_box = results[0].plot() # Draw bounding box
    # img_box = cv2.cvtColor(img_box, cv2.COLOR_BGR2RGB) # Convert color from BGR to RGB
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # img_canny = cv2.Canny(gray, 50, 150)
    # img_canny = cv2.cvtColor(img_canny, cv2.COLOR_GRAY2BGR)

    # Black canvas for edges
    edge_image = frame.copy()
    
    # For each detection
    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        
        # Extract and process ROI
        roi = gray[y1:y2, x1:x2]
        edges = cv2.Canny(roi, 50, 150)
        
       
        # Place edges back in the image at box location
        edge_image[y1:y2, x1:x2][edges > 0] = [0, 255, 0]
        
        # Draw bounding box
        cv2.rectangle(edge_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        # # Add label if enabled
        # if show_labels:
        #     class_id = int(box.cls[0])
        #     conf = float(box.conf[0])
        #     label = f"{result.names[class_id]} {conf:.2f}"
            
        #     cv2.putText(edge_image, label, (x1, y1 - 10),
        #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, hex_to_bgr(edge_color), 2)
    
    edge_image_rgb = cv2.cvtColor(edge_image, cv2.COLOR_BGR2RGB)
    proc_frame.image(edge_image_rgb, caption="Processed Frame", width="stretch")


    # proc_frame.image(edge_image, caption="Processed Frame", width="stretch")

cap.release()
