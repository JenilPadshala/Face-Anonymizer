import argparse
import os
import cv2
import mediapipe as mp
import numpy as np

def process_img (img, face_detection):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_detection.process(img_rgb)

    H, W, _ = img.shape
    if results.detections is not None:
        for detection in results.detections:
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box
            x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height
            x1 = int(x1*W)
            y1 = int(y1*H)
            w = int(w*W)
            h = int(h*H)

            img[y1:y1 + h, x1:x1 + w, :] = cv2.blur(img[y1:y1 + h, x1:x1 + w, :], (100, 100))
    return img



args = argparse.ArgumentParser()
args.add_argument("--mode", default='image', choices=['image', 'video', 'webcam'])
args.add_argument("--srcPath", default='./data/testImg.png')
args.add_argument("--dstFileName", default='testImg_output.png')

args = args.parse_args()

output_dir = './output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# read image
img_path = './data/testImg.png'
img = cv2.imread(img_path)
#detect faces
mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(min_detection_confidence=0.5, model_selection=0) as face_detection:
    if args.mode in ["image"]:
        img = cv2.imread(args.srcPath)
        H, W, _ = img.shape
        img = process_img(img, face_detection)
        cv2.imwrite(os.path.join(output_dir, args.dstFileName), img)

    elif args.mode in ["video"]:

        cap = cv2.VideoCapture(args.srcPath)
        frame_rate = cap.get(cv2.CAP_PROP_FPS)
        ret, frame = cap.read()

        output_video = cv2.VideoWriter(os.path.join(output_dir, 'output.mp4'), cv2.VideoWriter_fourcc(*'mp4v'), frame_rate, (frame.shape[1], frame.shape[0]))

        while ret:
            frame = process_img(frame, face_detection)
            output_video.write(frame)

            ret, frame = cap.read()
        cap.release()
        output_video.release()
    
    elif args.mode in ["webcam"]:
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        while ret:
            frame = process_img(frame, face_detection)
            cv2.imshow('frame', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
            ret, frame = cap.read()

        cap.release()
        cv2.destroyAllWindows()