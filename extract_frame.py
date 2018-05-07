import cv2
import os

video_path = 'F:\\activity_net.1.3\\video'
video_name = os.listdir(video_path)
frame_path = 'I:\\activity_net\\frame'


def extract_frame(file_name):
    file_path = os.path.join(video_path, file_name)

    file_index = file_name[0:file_name.find('.')]

    frame_full_path = os.path.join(frame_path, file_index)

    try:
        os.mkdir(frame_full_path)
    except OSError:
        pass

    cap = cv2.VideoCapture(file_path)
    # the index of the frame to read
    to_read = 0

    total_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    while to_read < total_frame:
        ret, frame = cap.read()
        if ret is True:
            cv2.imwrite(os.path.join(frame_full_path, 'img_' + str(int(to_read)) + '.jpg'), frame)
        to_read = to_read + 2 * fps
        cap.set(1, to_read)


def main():
    video_file = os.listdir(video_path)
    for i in video_file:
        extract_frame(i)


if __name__ == '__main__':
    main()
