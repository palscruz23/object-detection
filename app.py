from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration
import av
import threading
from ultralytics import YOLO

class YOLOProcessor(VideoProcessorBase):
    def __init__(self):
        self.model = YOLO("yolov8n.pt")  # Use nano for speed
        self.lock = threading.Lock()
        self.result_frame = None

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        
        # Only process if not already processing
        if self.lock.acquire(blocking=False):
            try:
                results = self.model(img, verbose=False)
                self.result_frame = results[0].plot()
            finally:
                self.lock.release()
        
        # Return last processed frame (or original if none yet)
        output = self.result_frame if self.result_frame is not None else img
        return av.VideoFrame.from_ndarray(output, format="bgr24")
    
webrtc_streamer(key="yolo", video_processor_factory=YOLOProcessor)