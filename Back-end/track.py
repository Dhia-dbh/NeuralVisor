import mediapipe as mp
import time
import cv2
import numpy as np
from PIL import Image



def track_focus_screenshot():
    """
    track focus level of the students that appear on the screen
    screenrecordes the screen and passes it through facemash
    then calculates the direction in which the student is looking
    and decides whether the student is focusing or not


    :param sec: number of second the capture the focus level
    :return list[int]: array where the first element is the number of sec and the rest is number of focused student for that period
    """
    path="screenshot.png"
    image=Image.open(path)
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.3, min_tracking_confidence=0.3, max_num_faces=5)

    mp_drawing = mp.solutions.drawing_utils

    drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)


    nbfocus = 0
    
    # Convert the image to a numpy array
    image = np.array(image)

    # Convert RGB to BGR (OpenCV uses BGR by default)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Resize the frame
    
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    result = face_mesh.process(image)
    image.flags.writeable = True

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    img_h, img_w, img_c = image.shape
    face_3d = []
    face_2d = []
    nbfocus = 0

    if result.multi_face_landmarks:
        for face_landmarks in result.multi_face_landmarks:
            face_3d = []
            face_2d = []
            for idx, lm in enumerate(face_landmarks.landmark):
                if idx in [33, 263, 1, 61, 291, 199]:
                    if idx == 1:
                        nose_2d = (lm.x * img_w, lm.y * img_h)
                        nose_3d = (lm.x * img_w, lm.y * img_h, lm.z * 3000)
                    x, y = int(lm.x * img_w), int(lm.y * img_h)

                    face_2d.append([x, y])
                    face_3d.append([x, y, lm.z])

            face_2d = np.array(face_2d, dtype=np.float64)
            face_3d = np.array(face_3d, dtype=np.float64)

            focal_length = 1 * img_w

            cam_matrix = np.array([[focal_length, 0, img_h / 2], [0, focal_length, img_w / 2], [0, 0, 1]])

            dist_matrix = np.zeros((4, 1), dtype=np.float64)

            success, rot_vec, trans_vec = cv2.solvePnP(face_3d, face_2d, cam_matrix, dist_matrix)

            rmat, jac = cv2.Rodrigues(rot_vec)

            angles, mtxR, mtxQ, Qx, Qy, Qz = cv2.RQDecomp3x3(rmat)

            x = angles[0] * 360
            y = angles[1] * 360
            z = angles[2] * 360
            if (y < -10):
                text = "looking Left"
            elif (y > 10):
                text = "looking right"
            elif (x < -10):
                text = "Looking down"
            else:
                nbfocus += 1
                text = "forword"

        # kan 3adad el nass mrakza a9al men noss
        if nbfocus < (len(result.multi_face_landmarks) / 2):
            pass

    return nbfocus

print(track_focus_screenshot())