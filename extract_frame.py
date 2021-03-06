import cv2
import os
import sys
import skvideo.io
import numpy as np

video_root = '/m/data/med/video_bg'
frame_root = '/m/data/med/frame_bg'


def extract_frame(video_name):
    # print(video_name)
    video_path = os.path.join(video_root, video_name)
    frame_path = video_name[0:video_name.find('.')]
    frame_folder_path = os.path.join(frame_root, frame_path)
    if os.path.exists(frame_folder_path) and os.listdir(frame_folder_path):
        return
    print(video_name)
    try:
        os.mkdir(frame_folder_path)
    except OSError:
        pass

    to_read = 0
    try:
        # videogen = skvideo.io.vread(video_path) # too high memory usage
        videogen = skvideo.io.vreader(video_path) # use more CPU, but much lower memory
        videometadata = skvideo.io.ffprobe(video_path)
        frame_rate = videometadata['video']['@r_frame_rate']
        frame_rate = int(frame_rate.split('/')[0]) / int(frame_rate.split('/')[1])
        num_frames = np.int(videometadata['video']['@nb_frames'])
        print('  total frames: ', num_frames)
        print('  frame rate: ', frame_rate)
        # while to_read < num_frames:
        #     frame = cv2.cvtColor(videogen[to_read], cv2.COLOR_BGR2RGB)
        #     cv2.imwrite(os.path.join(frame_folder_path, 'frame_' + str(to_read) + '.jpg'), frame)
        #     to_read = to_read + 2 * frame_rate
        for frame in videogen:
            if to_read % (frame_rate * 2) == 0:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                cv2.imwrite(os.path.join(frame_folder_path, 'frame_' + str(to_read) + '.jpg'), frame)
            to_read += 1
    except:
        file = open('error.txt', 'a')
        file.write(video_name + '\n')
        file.close()
        return


def main():
    if sys.argv[1] and sys.argv[1] == 'reprocess':
        files = open('error.txt', 'r').readlines()
        print(len(files))
    else:
        files = os.listdir(video_root)
        files.sort()
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
    except:
        start = 0
        end = len(files)
    for file in files[start:end]:
        file = file.strip()
        print(file)
        if file.endswith('.mp4'):
            extract_frame(file)


if __name__ == '__main__':
    main()
