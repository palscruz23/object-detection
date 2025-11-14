import cv2

# Replace with YOUR camera's IP and password
IP = "192.168.20.32"  # Your camera's IP
PASSWORD = "12345678"  # Your password

# Try these URLs one by one:
urls = [
    f"rtsp://admin:{PASSWORD}@{IP}:554/stream1",
    f"rtsp://admin:{PASSWORD}@{IP}:554/test1",
    f"rtsp://admin:{PASSWORD}@{IP}:554/live",
    f"rtsp://admin:{PASSWORD}@{IP}:554/11",
    f"rtsp://admin:{PASSWORD}@{IP}:554/onvif1",
    f"rtsp://admin:{PASSWORD}@{IP}:554/h264_stream",
]

for url in urls:
    print(f"Trying: {url}")
    cap = cv2.VideoCapture(url)
    
    if cap.isOpened():
        ret, frame = cap.read()
        if ret:
            print(f"✓ SUCCESS with: {url}")
            cv2.imshow('Linklemo Camera', frame)
            cv2.waitKey(3000)
            cv2.destroyAllWindows()
            cap.release()
            break
        cap.release()
    else:
        print(f"✗ Failed")