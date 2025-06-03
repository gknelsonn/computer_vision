from deepface import DeepFace
import cv2

def recognize_staff(frame):
    # Save detected face
    cv2.imwrite("temp_face.jpg", frame)
    # Compare with staff database
    try:
        result = DeepFace.find(img_path="temp_face.jpg", db_path=r"C:\Users\Admin\Desktop\restaurant monitoring system\staff_db")
        return len(result[0]) > 0  # True if match found
    except:
        return False

# Test with a staff/non-staff face
image = cv2.imread(r"C:\Users\Admin\Desktop\restaurant monitoring system\test_image1.jpg")
print("Is staff?", recognize_staff(image))