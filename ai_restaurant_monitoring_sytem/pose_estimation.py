import mediapipe as mp
import cv2

mp_pose = mp.solutions.pose

def is_sitting(frame):
    with mp_pose.Pose(min_detection_confidence=0.5) as pose:
        results = pose.process(frame)
        if results.pose_landmarks:
            # Hip (landmark 23) vs. Knee (landmark 25) position
            hip_y = results.pose_landmarks.landmark[23].y
            knee_y = results.pose_landmarks.landmark[25].y
            return hip_y > knee_y  # Hip is lower than knee = sitting
        return False

# Test with a seated/standing image
image = cv2.imread(r"C:\Users\Admin\Desktop\restaurant monitoring system\test_image1.jpg")
print("Is sitting?", is_sitting(image))