""" """ 
###############  with qtinker#################################
""" import cv2
import numpy as np
from yolo_segmentation import YOLOSegmentation
import os
import sqlite3
from datetime import datetime

def create_table_if_not_exists(conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS vehicle_data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    serial_no TEXT,
                    time_detected TEXT,
                    vehicle_height REAL
                )''')
    conn.commit()

def insert_data(conn, serial_no, time_detected, vehicle_height):
    c = conn.cursor()
    c.execute('''INSERT INTO vehicle_data (serial_no, time_detected, vehicle_height) 
                 VALUES (?, ?, ?)''', (serial_no, time_detected, vehicle_height))
    conn.commit()

def main():
    video_input_path = "calibration_video6.mp4"
    model_path = "best9.pt"

    yolo_segmentation = YOLOSegmentation(model_path)
    video_capture = cv2.VideoCapture(video_input_path)

    if not video_capture.isOpened():
        print("Error opening video file.")
        return

    ret, frame = video_capture.read()
    if not ret:
        print("Failed to read video")
        return

    height, width = frame.shape[:2]
    print(f"Video dimensions: {width}x{height}")

    if width < 250:
        print("The line position x=250 is outside of the video width.")
        return

    out = cv2.VideoWriter('final_output.avi', cv2.VideoWriter_fourcc(*'XVID'), 10, (width, height))

    snapshot_taken = False

    # Connect to the SQLite database
    conn = sqlite3.connect('vehicle_data.db')
    create_table_if_not_exists(conn)

    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if not ret:
            break

        cv2.line(frame, (250, 0), (250, height), (255, 0, 0), 1)
        cv2.putText(frame, f'Press q to exit ', (550, 650), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
        _, _, seg_contours, scores = yolo_segmentation.detect(frame)
        print(f"Detected {len(seg_contours)} contours")
        if not seg_contours:
            snapshot_taken = False  # Reset the flag if no contours are detected
        for seg, score in zip(seg_contours, scores):
            if score > 0.90:
                cv2.drawContours(frame, [seg], -1, (0, 255, 0), 1)
                min_x = np.min(seg[:, 0])
                max_x = np.max(seg[:, 0])

                mask_height_pixels = np.max(seg[:, 1]) - np.min(seg[:, 1])

                if mask_height_pixels <= 1500:
                    pixel_to_cm_ratio = 1.7249
                else:
                    pixel_to_cm_ratio = 1.6481

                mask_height_cm = mask_height_pixels / pixel_to_cm_ratio
                cv2.putText(frame, f'Mask Height: {mask_height_pixels}px', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.putText(frame, f'Mask Height: {mask_height_cm:.2f} cm', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                
                print(f"Contour bounds: min_x={min_x}, max_x={max_x}")
                if min_x <= 250 <= max_x and not snapshot_taken:
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    insert_data(conn, 'ABC123', timestamp, mask_height_cm)
                    snapshot_taken = True

        cv2.imshow('Live Segmentation press q to exit application', frame)
        out.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    out.release()
    cv2.destroyAllWindows()

    # Close the database connection
    conn.close()

if __name__ == '__main__':
    main()


 """

""" import cv2
import numpy as np
from yolo_segmentation import YOLOSegmentation
import os
import sqlite3
from datetime import datetime

def create_table_if_not_exists(conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS vehicle_data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    serial_no TEXT,
                    time_detected TEXT,
                    vehicle_height REAL
                )''')
    conn.commit()

def insert_data(conn, serial_no, time_detected, vehicle_height):
    c = conn.cursor()
    c.execute('''INSERT INTO vehicle_data (serial_no, time_detected, vehicle_height) 
                 VALUES (?, ?, ?)''', (serial_no, time_detected, vehicle_height))
    conn.commit()

def main():
    video_input_path = "calibration_video6.mp4"
    model_path = "best9.pt"

    yolo_segmentation = YOLOSegmentation(model_path)
    video_capture = cv2.VideoCapture(video_input_path)

    if not video_capture.isOpened():
        print("Error opening video file.")
        return

    ret, frame = video_capture.read()
    if not ret:
        print("Failed to read video")
        return

    height, width = frame.shape[:2]
    print(f"Video dimensions: {width}x{height}")

    if width < 250:
        print("The line position x=250 is outside of the video width.")
        return

    out = cv2.VideoWriter('final_output.avi', cv2.VideoWriter_fourcc(*'XVID'), 10, (width, height))

    #snapshot_taken = False
    #crossed_line = False  # Flag to check if mask has crossed the line

    # Connect to the SQLite database
    conn = sqlite3.connect('vehicle_data.db')
    create_table_if_not_exists(conn)

    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if not ret:
            break

        cv2.line(frame, (250, 0), (250, height), (255, 0, 0), 1)
        cv2.putText(frame, f'Press q to exit ', (550, 650), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
        _, _, seg_contours, scores = yolo_segmentation.detect(frame)
        print(f"Detected {len(seg_contours)} contours")
        if not seg_contours:
            snapshot_taken = False  # Reset the flag if no contours are detected
            crossed_line = False  # Reset line crossing status

        for seg, score in zip(seg_contours, scores):
            if score > 0.90:
                cv2.drawContours(frame, [seg], -1, (0, 255, 0), 1)
                min_x = np.min(seg[:, 0])
                max_x = np.max(seg[:, 0])
                
                
                mask_height_pixels = np.max(seg[:, 1]) - np.min(seg[:, 1])

                if mask_height_pixels <= 1500:
                    pixel_to_cm_ratio = 1.7249
                else:
                    pixel_to_cm_ratio = 1.6481
                
                mask_height_cm = mask_height_pixels / pixel_to_cm_ratio
                cv2.putText(frame, f'Mask Height: {mask_height_pixels}px', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.putText(frame, f'Mask Height: {mask_height_cm:.2f} cm', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                
                if min_x <= 250 <= max_x and not snapshot_taken and not crossed_line:
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    insert_data(conn, 'ABC123', timestamp, mask_height_cm)
                    snapshot_taken = True

                if max_x <0:  # Check if mask has completely crossed the line
                    crossed_line = True
                    print('line crossed')

        cv2.imshow('Live Segmentation press q to exit application', frame)
        out.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    out.release()
    cv2.destroyAllWindows()

    # Close the database connection
    conn.close()

if __name__ == '__main__':
    main()  """

import cv2
import numpy as np
from yolo_segmentation import YOLOSegmentation
import os
import sqlite3
from datetime import datetime

def create_table_if_not_exists(conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS vehicle_data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    serial_no TEXT,
                    time_detected TEXT,
                    vehicle_height REAL
                )''')
    conn.commit()

def insert_data(conn, serial_no, time_detected, vehicle_height):
    c = conn.cursor()
    c.execute('''INSERT INTO vehicle_data (serial_no, time_detected, vehicle_height) 
                 VALUES (?, ?, ?)''', (serial_no, time_detected, vehicle_height))
    conn.commit()

def main():
    video_input_path = "OneDrive_1_5-13-2024/calibration_video6.mp4"
    model_path = "OneDrive_1_5-13-2024/best10.pt"

    yolo_segmentation = YOLOSegmentation(model_path)
    video_capture = cv2.VideoCapture(video_input_path)

    if not video_capture.isOpened():
        print("Error opening video file.")
        return

    ret, frame = video_capture.read()
    if not ret:
        print("Failed to read video")
        return

    height, width = frame.shape[:2]
    print(f"Video dimensions: {width}x{height}")

    if width < 250:
        print("The line position x=250 is outside of the video width.")
        return

    out = cv2.VideoWriter('final_output.avi', cv2.VideoWriter_fourcc(*'XVID'), 10, (width, height))

    #snapshot_taken = False
    #crossed_line = False  # Flag to check if mask has crossed the line

    # Connect to the SQLite database
    conn = sqlite3.connect('vehicle_data.db')
    create_table_if_not_exists(conn)

    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if not ret:
            break

        cv2.line(frame, (250, 0), (250, height), (255, 0, 0), 1)
        cv2.putText(frame, f'Press q to exit ', (550, 650), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
        _, _, seg_contours, scores = yolo_segmentation.detect(frame)
        print(f"Detected {len(seg_contours)} contours")
        if not seg_contours:
            snapshot_taken = False  # Reset the flag if no contours are detected
            crossed_line = False  # Reset line crossing status

        for seg, score in zip(seg_contours, scores):
            if score > 0.20:
                cv2.drawContours(frame, [seg], -1, (0, 255, 0), 1)
                min_x = np.min(seg[:, 0])
                max_x = np.max(seg[:, 0])
                
                
                mask_height_pixels = np.max(seg[:, 1]) - np.min(seg[:, 1])

                if mask_height_pixels <= 1500:
                    pixel_to_cm_ratio = 1.7249
                else:
                    pixel_to_cm_ratio = 1.6481
                
                mask_height_cm = mask_height_pixels / pixel_to_cm_ratio
                cv2.putText(frame, f'Mask Height: {mask_height_pixels}px', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.putText(frame, f'Mask Height: {mask_height_cm:.2f} cm', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                
                if min_x <= 250 <= max_x and not snapshot_taken and not crossed_line:
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    insert_data(conn, 'ABC123', timestamp, mask_height_cm)
                    snapshot_taken = True

                if max_x <500:  # Check if mask has completely crossed the line
                    crossed_line = True
                    print('line crossed')

        cv2.imshow('Live Segmentation press q to exit application', frame)
        out.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    out.release()
    cv2.destroyAllWindows()

    # Close the database connection
    conn.close()

if __name__ == '__main__':
    main() 
