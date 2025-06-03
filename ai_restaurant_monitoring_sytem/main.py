from datetime import datetime

import cv2
from ultralytics import YOLO
from database import log_customer, log_staff_visit
from pose_estimation import is_sitting
from staff_recognition import recognize_staff

model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture("test_video.mp4")

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

#output video setup
output_video = "output_annotated.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video, fourcc, fps, (frame_width, frame_height))


# Track active customers
active_tables = {}

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model.track(frame, classes=[0, 60], persist=True)

    #Get annotated frame with bounding boxes
    annotated_frame = results[0].plot()


    for box in results[0].boxes:
        if box.cls == 0:  # Person detected
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            person_roi = frame[y1:y2, x1:x2]

            # Check if sitting
            if is_sitting(person_roi):
                table_id = 1  # Assign table ID (simplified for testing)
                if table_id not in active_tables:
                    log_customer(table_id)
                    active_tables[table_id] = datetime.now()

                # Check if staff
                if recognize_staff(person_roi):
                    log_staff_visit(table_id)

    #Write the processed frame to output video
    out.write(annotated_frame)

    cv2.imshow("Monitoring", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Processing complete. Output saved to {output_video}")