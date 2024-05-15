import cv2
import numpy as np
import os

cap = cv2.VideoCapture('/Users/minsik/development/Code_and_dataset/game.mp4') #  game,game2,game3 영상 중 선택하여 호출 
bgSubtractor = cv2.createBackgroundSubtractorKNN(history=10, dist2Threshold=200.0)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

kernel_size = 13
kernel_dilation = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
kernel_open = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

#game (원하는 데모 영상에 따라 코드 선택)
lower_color = np.array([21, 215, 220])  
upper_color = np.array([38, 255, 255])

#game2
#lower_color = np.array([31, 100, 190])  
#upper_color = np.array([40, 230, 255])

#game3
#lower_color = np.array([24, 147, 190])  
#upper_color = np.array([36, 187, 236])

frame_count = 0
trajectory_image = np.zeros([360, 640, 3], np.uint8)
point_image = np.zeros([360, 640, 3], np.uint8)

prev_frame = None
current_frame = None
frame_diff = None
motion_mask = None

track_box = None

prediction_frames = 5
prediction_factor = 2.0
predicted_center = None
velocity_x = 0
velocity_y = 0

while(cap.isOpened()):

    rret, frame = cap.read()
    resize_scale = 640. / float(frame.shape[1])

    frame = cv2.resize(frame, None, fx=resize_scale, fy=resize_scale)

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frame_hsv, lower_color, upper_color)
    blur = cv2.GaussianBlur(mask, (5, 5), 0)

    fgmask = bgSubtractor.apply(blur)

    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_DILATE, kernel_dilation)

    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    prev_center = None

    for contour in contours:
        if cv2.contourArea(contour) > 100:
            (x, y), radius = cv2.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius)

            if center is not None:
                predicted_center = center
                if prev_center is not None:
                    velocity_x = (center[0] - prev_center[0]) / prediction_frames
                    velocity_y = (center[1] - prev_center[1]) / prediction_frames
            else:
                if predicted_center is not None:
                    predicted_center = (
                        int(predicted_center[0] + velocity_x * prediction_factor),
                        int(predicted_center[1] + velocity_y * prediction_factor)
                    )

            if center is not None:
                cv2.rectangle(frame, (int(x) - radius, int(y) - radius), (int(x) + radius, int(y) + radius), (255, 0, 0), 2)
                track_box = (int(x) - radius, int(y) - radius, radius * 2, radius * 2)
            elif predicted_center is not None:
                (x, y) = predicted_center
                radius = int(radius)
                cv2.rectangle(frame, (x - radius, y - radius), (x + radius, y + radius), (255, 0, 0), 2)

            prev_center = center
    cv2.circle(frame, center, radius, (0, 255, 0), 2)
    if track_box is not None:
        cv2.rectangle(frame, (track_box[0], track_box[1]), (track_box[0] + track_box[2], track_box[1] + track_box[3]), (255, 0, 0), 3)

    cv2.imshow('frame', frame)
    #cv2.imshow('mask', fgmask)
    #cv2.imshow('hsv', mask)
    k = cv2.waitKey(4)
    if k == 27:
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        break

cap.release()
cv2.destroyAllWindows()
