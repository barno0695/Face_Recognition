import hashlib as hl
import cv2

face = []

def saveFace():
	cap = cv2.VideoCapture(0)
	while(True):
		ret, frame = cap.read()
		if ret == True:
			face.append(hl.sha256(frame).hexdigest())
			cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
		break


def getFace():
	cap = cv2.VideoCapture(0)
	while(True):
		ret, frame = cap.read()
		if ret == True:
			print hl.sha256(frame).hexdigest()
			break
			if hl.sha256(frame).hexdigest() in face:
				break
			cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break


def detectFace():
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
	cap = cv2.VideoCapture(0)
	while(True):
		ret, frame = cap.read()
		img = frame
		if ret == True:
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

			faces = face_cascade.detectMultiScale(gray, 1.3, 5)
			for (x,y,w,h) in faces:
			    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
			    roi_gray = gray[y:y+h, x:x+w]
			    roi_color = img[y:y+h, x:x+w]
			    eyes = eye_cascade.detectMultiScale(roi_gray)
			    for (ex,ey,ew,eh) in eyes:
			        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
			cv2.imshow('img',img)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	
saveFace()
print face
getFace()

# detectFace()

