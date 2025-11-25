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
        model_choice = st.selectbox("Choose Model", ["yolo12n.pt", "yolov8n.pt"])
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
    proc_frame.image(img_box, channels="BGR", caption="Processed", width="stretch")

cap.release()
