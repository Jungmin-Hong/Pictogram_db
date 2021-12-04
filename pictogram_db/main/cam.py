import mediapipe as mp
import cv2
import math
import matplotlib.pyplot as plt
import pandas as pd

import time

from pose_angle import getCal

def calculateAngle(i, j, k):
    try:
        x1, y1 = results.pose_landmarks.landmark[mp_holistic.PoseLandmark(i).value].x, results.pose_landmarks.landmark[mp_holistic.PoseLandmark(i).value].y
        x2, y2 = results.pose_landmarks.landmark[mp_holistic.PoseLandmark(j).value].x, results.pose_landmarks.landmark[mp_holistic.PoseLandmark(j).value].y
        x3, y3 =results.pose_landmarks.landmark[mp_holistic.PoseLandmark(k).value].x, results.pose_landmarks.landmark[mp_holistic.PoseLandmark(k).value].y
    
        length_ij = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        length_jk = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
        length_ki = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)

        angle_cos2 = int(math.degrees(math.acos((length_ij ** 2 + length_jk ** 2 - length_ki ** 2) / (2 * length_ij * length_jk))))
        
        angle_atan = int(math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2)))

        return angle_cos2

    except:

        return 0
    #print("제2 코사인을 이용시 각도=> ", angle_cos2)
    #print("arctan를 이용시 q각도=> ", angle_atan)
    
    


# mp_drawing = mp.solutions.drawing_utils
# mp_holistic = mp.solutions.holistic

# cap = cv2.VideoCapture(0)

# with mp_holistic.Holistic() as holistic:
    
#     while cap.isOpened():
#         ret, frame = cap.read()
        
#         image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         results = holistic.process(image)

#         image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

#         mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)

#         # if results.pose_landmarks:
#         #     for i in range(33):
#         #         print(results.pose_landmarks(i).name)  # 질점 이름
#         #         # print(results.pose_landmarks.landmark[results.pose_landmarks.PoseLandmark(i).value])

#         cv2.imshow('Pose Landmark', image)

#         if cv2.waitKey(10) & 0xFF == ord('q'):
#             break
    
# cap.release()
# cv2.destroyAllWindows()

# import mediapipe as mp
# import cv2

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

cap = cv2.VideoCapture(0)

with mp_holistic.Holistic() as holistic:
    while cap.isOpened():
        ret, frame = cap.read()

        # color 채널 변경
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # holistic 적용
        results = holistic.process(image)

        # imshow를 위해 채널 변경
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)

        # print(results.pose_landmarks.landmark[mp_holistic.PoseLandmark(15).value].x)  #19
        # print(results.pose_landmarks.landmark[mp_holistic.PoseLandmark(15).value].y)
        # def getCal():
        L_arm = calculateAngle(12, 14, 16) #L_arm
        L_gyeo = calculateAngle(14, 12, 24) #L_gyeo
        L_hip = calculateAngle(12, 24, 26) #L_hip
        L_knee = calculateAngle(24, 26, 28) #L_knee
        R_arm = calculateAngle(11, 13, 15) #R_arm
        R_gyeo = calculateAngle(13, 11, 23) #R_gyeo
        R_hip = calculateAngle(11, 23, 25) #R_hip
        R_knee = calculateAngle(23, 25, 27) #R_knee
        
        # print(f"""L_arm: {L_arm}, 
        # L_gyeo: {L_gyeo}, 
        # L_hip: {L_hip}, 
        # L_knee: {L_knee},
        # R_arm: {R_arm}, 
        # R_gyeo: {R_gyeo}, 
        # R_hip: {R_hip}, 
        # R_knee: {R_knee} """)

        getCal(L_arm, L_gyeo, L_hip, L_knee, R_arm, R_gyeo, R_hip, R_knee)

        cv2.imshow('Pose Landmark', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

