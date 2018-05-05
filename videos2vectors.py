
def main():
	video_path = ''
	frame_path = ''
	vector_path = ''
	for video in video_path:
		frames = extract_frame(file)
		get_vector_imgNet(frames)
		get_vector_places365(frames)
		combine()

if __name__ == '__main__':
    main()
