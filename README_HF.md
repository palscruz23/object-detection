---
title: YOLO Live Object Detection
emoji: 🎯
colorFrom: blue
colorTo: red
sdk: docker
pinned: false
license: mit
---

# 🎯 YOLO Live Object Detection

Real-time object detection using YOLOv8 with live webcam/phone camera feed.

## Features

- **Real-time Detection**: Live object detection from your webcam or phone camera
- **YOLOv8 Nano**: Fast and efficient model for real-time inference
- **WebRTC Support**: Works on both desktop and mobile devices
- **80+ Object Classes**: Detects people, vehicles, animals, and everyday objects

## How to Use

1. Click **START** to begin the video stream
2. Allow camera access when prompted by your browser
3. Point your camera at objects to see real-time detection
4. The bounding boxes and labels will appear on detected objects

## Technical Details

- **Model**: YOLOv8 Nano (yolov8n.pt)
- **Framework**: Ultralytics YOLO, Streamlit, streamlit-webrtc
- **Inference**: Frame-by-frame processing with thread-safe buffering

## Requirements

- Modern web browser with WebRTC support
- Webcam or phone camera
- Stable internet connection

## Performance

The app uses YOLOv8 Nano for optimal balance between speed and accuracy. Frame processing may vary based on server load.

## Privacy

All video processing happens in real-time. No video frames are stored or recorded.
