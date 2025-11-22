from ultralytics import solutions
import streamlit as st


st.title("YOLO Inference with Ultralytics Solutions")

inf = solutions.Inference(
    model="yolo11n.pt",  # you can use any model that Ultralytics support, i.e. YOLO11, or custom trained model
)

inf.inference()
