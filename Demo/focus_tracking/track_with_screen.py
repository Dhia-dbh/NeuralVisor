import mediapipe as mp
import time
import cv2
import numpy as np
from PIL import Image
import pyautogui
import keyboard


def track_focus_screen(sec=1):
    """
    This function captures the screen, detects whether each student
    appearing in the frames is focusing or not by determining the direction
    in which they are looking, and tracks the number of focused students
    at specified intervals.

    Parameters:
    sec (int, optional): The interval (in seconds) at which to update the focus status. Default is 1 second.
    Returns:
    list[int]: A list where the first element is the number of seconds (sec), and the subsequent elements are the number of focused students for each period.
    """
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.3, min_tracking_confidence=0.3, max_num_faces=5)

    mp_drawing = mp.solutions.drawing_utils

    drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

    focused_per_time = [sec]
    begin = time.time()
    last = 0
    nbfocus = 0
    screen_width, screen_height = pyautogui.size()

    while True:
        check = time.time()
        if int(check-begin)%sec==0 and int(check-begin)>last:
            image = pyautogui.screenshot()

            # Convert the image to a numpy array
            image = np.array(image)

            # Convert RGB to BGR (OpenCV uses BGR by default)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Resize the frame
            image = cv2.resize(image, (screen_width, screen_height))
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
            last =int(check-begin)
            focused_per_time.append(nbfocus)


        #get out
        if keyboard.is_pressed('esc'):
            break
    return focused_per_time

def track_focus_screenshot(path):
    """
    This function takes an image file path as input,
    processes the image to detect whether each person
    appearing in it is focusing or not by determining
    the direction in which they are looking,
    and returns the number of focused individuals.

    Parameters:
    path (str): The file path of the image to be processed.
    Returns:
    int: The number of focused students detected in the image.
    """

    image=Image.open(path)
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.3, max_num_faces=5)

    mp_drawing = mp.solutions.drawing_utils

    drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)


    nbfocus = 0
    screen_width, screen_height = pyautogui.size()
    # Convert the image to a numpy array
    image = np.array(image)

    # Convert RGB to BGR (OpenCV uses BGR by default)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Resize the frame
    image = cv2.resize(image, (screen_width, screen_height))
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
        print(len(result.multi_face_landmarks))
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

def track_focus_screenshot_with_draw(path):
    """
    track focus level of the students that appear on the screen
    screenrecordes the screen and passes it through facemash
    then calculates the direction in which the student is looking
    and decides whether the student is focusing or not


    :param sec: number of second the capture the focus level
    :return list[int]: array where the first element is the number of sec and the rest is number of focused student for that period
    """
    image=Image.open(path)
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.2, min_tracking_confidence=0.3, max_num_faces=5)

    mp_drawing = mp.solutions.drawing_utils

    drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)


    nbfocus = 0
    screen_width, screen_height = pyautogui.size()
    # Convert the image to a numpy array
    image = np.array(image)

    # Convert RGB to BGR (OpenCV uses BGR by default)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Resize the frame
    image = cv2.resize(image, (screen_width, screen_height))
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
                        nose_3d = (lm.x * img_w, lm.y * img_h, lm.z )
                        face_2d.append(nose_2d)
                        face_3d.append(nose_3d)
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
            print(x,y)
            if (y < -3.5):
                text = "looking Left"
            elif (y > 3.9):
                text = "looking right"
            elif (x < -10):
                text = "Looking down"
            else:
                nbfocus += 1
                text = "forword"
            face_region = np.array([
                [lm.x * img_w, lm.y * img_h] for lm in face_landmarks.landmark
            ], dtype=np.int64)

            # Calculate bounding box coordinates based on minimum and maximum x/y values
            min_x = np.min(face_region[:, 0])
            max_x = np.max(face_region[:, 0])
            min_y = np.min(face_region[:, 1])
            max_y = np.max(face_region[:, 1])
            cv2.putText(image, text, (min_x - 5, min_y - 5), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)

            # Draw the square around the face
            cv2.rectangle(image, (min_x, min_y), (max_x, max_y), (0, 255, 0), 2)
        # kan 3adad el nass mrakza a9al men noss
        if nbfocus < (len(result.multi_face_landmarks) / 2):
            pass
    cv2.imshow("Focus Detection", image)

    # Keep the window open until 'q' key is pressed
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q')or keyboard.is_pressed('esc'):
            break
    return nbfocus


#print(track_focus_screen())
#path= "screenshot.png"
#track_focus_screenshot_with_draw(path)