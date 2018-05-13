import cv2
import os

video_root = '/m/data/med/video'
frame_root = '/m/data/med/frame'


def extract_frame(video_name):
    video_path = os.path.join(video_root, video_name)
    frame_path = video_name[0:video_name.find('.')]
    frame_folder_path = os.path.join(frame_root, frame_path)
    try:
        os.mkdir(frame_folder_path)
    except OSError:
        pass

    cap = cv2.VideoCapture(video_path)
    to_read = 0
    total_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    while to_read < total_frame:
        ret, frame = cap.read()
        if ret is True:
            cv2.imwrite(os.path.join(frame_folder_path, 'img_' + str(int(to_read)) + '.jpg'), frame)
        to_read = to_read + 2 * fps
        cap.set(1, to_read)


def main():
    files = os.listdir(video_root)
    for file in files:
        if file.endswith('.mp4'):
        extract_frame(file)


if __name__ == '__main__':
    main()
