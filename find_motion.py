import cv2
from spot_diff import spot_diff
import time
import numpy as np
import os
import cv2
from time import gmtime, strftime
import shutil
import datetime

def find_motion():
	filename = "stoleVideo.mp4"
	frames_per_second = 24.0
	res = '720p'


	def change_res(cap, width, height):
		cap.set(3, width)
		cap.set(4, height)

	STD_DIMENSIONS =  {
		"480p": (640, 480),
		"720p": (1280, 720),
		"1080p": (1920, 1080),
		"4k": (3840, 2160),
	}

	def get_dims(cap, res='1080p'):
		width, height = STD_DIMENSIONS["480p"]
		if res in STD_DIMENSIONS:
			width,height = STD_DIMENSIONS[res]

		change_res(cap, width, height)
		return width, height

	VIDEO_TYPE = {
		'avi': cv2.VideoWriter_fourcc(*'XVID'),
		#'mp4': cv2.VideoWriter_fourcc(*'H264'),
		'mp4': cv2.VideoWriter_fourcc(*'XVID'),
	}

	def get_video_type(filename):
		filename, ext = os.path.splitext(filename)
		if ext in VIDEO_TYPE:
			return  VIDEO_TYPE[ext]
		return VIDEO_TYPE['avi']

	motion_detected = False
	is_start_done = False

	cap = cv2.VideoCapture(0)
	out = cv2.VideoWriter(filename, get_video_type(filename), 25, get_dims(cap, res))

	check = []
	
	print("waiting for 2 seconds")
	time.sleep(2)
	frame1 = cap.read()

	_, frm1 = cap.read()
	frm1 = cv2.cvtColor(frm1, cv2.COLOR_BGR2GRAY)

	
	while True:
		_, frm2c = cap.read()
		frm2 = cv2.cvtColor(frm2c, cv2.COLOR_BGR2GRAY)

		diff = cv2.absdiff(frm1, frm2)

		_, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

		contors = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

		#look at it
		contors = [c for c in contors if cv2.contourArea(c) > 25]


		if len(contors) > 5:
			cv2.putText(frm2c, "motion detected", (50,50), cv2.FONT_HERSHEY_SIMPLEX,2, (0,255,0),2)
			out.write(frm2c)
			motion_detected = True
			is_start_done = False

		elif motion_detected and len(contors) < 3:
			if (is_start_done) == False:
				start = time.time()
				is_start_done = True
				end = time.time()

			end = time.time()

			print(end-start)
			if (end - start) > 4:
				frame2 = cap.read()
				out.release()
				cap.release()
				cv2.destroyAllWindows()

				dir = 'stolen'
				for f in os.listdir(dir):
					os.remove(os.path.join(dir, f))

				videoFileDestination = "C:\\Users\\adith\\OneDrive\\Documents\\PES\\Hackathons\\Tri-NIT\\"+str(filename)
				shutil.move(str(videoFileDestination), 'C:\\Users\\adith\\OneDrive\\Documents\\PES\\Hackathons\\Tri-NIT\\stolen')
				
				x = spot_diff(frame1, frame2)
				if x == 0:
					print("running again")
					return

				else:
					print("found motion sending mail")
					return

		else:
			cv2.putText(frm2c, "no motion detected", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)

		cv2.imshow("winname", frm2c)

		_, frm1 = cap.read()
		frm1 = cv2.cvtColor(frm1, cv2.COLOR_BGR2GRAY)

		if cv2.waitKey(1) == 27:
			cv2.destroyAllWindows()
			break
		
	return

