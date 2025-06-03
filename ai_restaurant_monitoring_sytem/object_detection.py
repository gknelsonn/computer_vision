from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

video_path = r"C:\Users\Admin\Desktop\restaurant monitoring system\test_video.mp4"
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results =model.track(frame, classes=[0, 60], persist = True)

    annotated_frame = results[0].plot()
    cv2.imshow("Monitoring", annotated_frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()