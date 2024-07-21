import mediapipe as mp
import time
import cv2
import numpy as np



def add_tracking_to_video(path,output_path):
    """
    This function processes an input video to detect whether each person
    in the frames is focusing or not by determining the direction in which
    they are looking. It then draws the detection results onto the video,
    highlighting faces, the direction of gaze, and providing alerts if
    the majority of people in the frame are unfocused.

    input str : path for the video

    output mp4 : The processed video is saved to the specified output path.

    """
    # Create a VideoCapture object
    cap = cv2.VideoCapture(path)

    # Check if the video was opened successfully
    if not cap.isOpened():
        print("Error: Could not open video file.")
        exit()
        # Release the VideoCapture object and close all windows
        cap.release()
        cv2.destroyAllWindows()

    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.7, max_num_faces=5)

    sec=2
    focused_per_time = [sec]
    begin = time.time()
    last = 0
    nbfocus = 0
    alert_repetition=0
    # Define video writer parameters
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Video codec
    fps = cap.get(cv2.CAP_PROP_FPS)  # Get FPS from input video
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while True:
        check = time.time()
        if int(check - begin) % sec == 0 and int(check - begin) > last:
            last = int(check - begin)
            focused_per_time.append(nbfocus)
        ret, image = cap.read()
        # Break the loop if there are no more frames
        if not ret:
            break
        start = time.time()
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
                if (y < -5):
                    text = "looking Left"
                elif (y > 5):
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
            end = time.time()
            totaltime = end - start
            fps = 1 / totaltime
            # kan 3adad el nass mrakza a9al men noss
            if nbfocus < (len(result.multi_face_landmarks) / 2) :
                cv2.rectangle(image, (0, 0), (img_w, img_h), (0, 0, 255), 8)
                cv2.putText(image, "aleart :majorety of students unfocused", (10, 30), cv2.FONT_HERSHEY_PLAIN, 1.3,
                            (0, 0, 255), 2)
                alert_repetition=10
            if alert_repetition>0:
                cv2.rectangle(image, (0, 0), (img_w, img_h), (0, 0, 255), 8)
                cv2.putText(image, "aleart :majorety of students unfocused", (10, 30), cv2.FONT_HERSHEY_PLAIN, 1.3,
                            (0, 0, 255), 2)
                alert_repetition-=1
            cv2.putText(image, f'FPS:{int(fps)}', (20, img_h-20), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
            cv2.putText(image, f'focused:{nbfocus}/{len(result.multi_face_landmarks)}', (img_w-180, img_h-20),
                        cv2.FONT_HERSHEY_PLAIN,
                        1.5, (0, 255, 0), 2)

        # Display the frame
        writer.write(image)

        # Exit the video display when the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    writer.release()

#add_tracking_to_video("exemple_vid.mp4","result.mp4")