import face_recognition
import cv2
import numpy as np

data_dir = "orl_faces/s"

train_files = [data_dir+str(i+1)+"/1.pgm" for i in range(40)]

train_images = [face_recognition.load_image_file(f) for f in train_files]

saved_encodings = [face_recognition.face_encodings(i)[0] for i in train_images]

threshold = 0.6

def closest(encoding):
	i = 0
	min_d = 1
	d = face_recognition.face_distance(saved_encodings,encoding)
	for j in range(len(saved_encodings)):
		if d[j]<min_d:
			i=j+1
			min_d = d[j]
	if min_d>threshold:
		return 0
	return i

correct = 0

for i in range(40):
	for j in range(8):
		file = data_dir+str(i+1)+"/" + str(j+2) + ".pgm"
		# print (file)
		image = face_recognition.load_image_file(file)
		# print (face_recognition.face_encodings(image))
		face_locations = face_recognition.face_locations(image)
		encoding = face_recognition.face_encodings(image, face_locations)
		# encoding = face_recognition.face_encodings(image)
		if len(encoding)==0:
			print ("No: " + file)
			continue
		# print (len(encoding[0]))
		ret = closest(encoding[0])
		if ret==i+1:
			correct+=1
		else:
			print ("Wrong: " + file)
		# print (correct)

print (correct*1.0/360)