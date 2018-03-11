# import the open cv2 library
import cv2

# import the frontal face cascade xml
# (containing all the information needed to identify a frontal face)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# function that will do the faces detection given a gray image and it's colored frame
def face_detection(gray, frame):
    # get all the faces detected (in a box format) from the gray image
    # (gray image, the shrinking factor of the analyzed image, number of neighbours)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # run through every face
    for (faceX, faceY, faceWidth, faceHeight) in faces:
        # draw a red box around every face detected on the colored frame
        # (image to draw, top left coordinates, bottom right coordinates, rgb color, box thickness)
        cv2.rectangle(frame, (faceX,faceY), (faceX+faceWidth,faceY+faceHeight), (255,0,0), 4)
    # return the new colored frame
    return frame
# access the main webcam
webcam = cv2.VideoCapture(0);

while True:
    # get the current frame
    ret, frame = webcam.read()
    # if there's a frame to analyze
    if ret is True:
        # get the gray image of the frame (using the convert color function of cv2)
        gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    # if there's no frame to analyze (maybe the webcam is not ready)
    else:
        # go to the next cycle (wait)
        continue
    # get the new colored frame with the face detection box already drawn
    canvas = face_detection(gray, frame)
    # display the new frame
    cv2.imshow('Face Detection', canvas)
    # if a key was pressed and it is the e key
    if cv2.waitKey(1) & 0xFF == ord('e'):
        # exit the loop
        break
# release the webcam used
webcam.release()
# destroy all the windows used by the application
cv2.destroyAllWindows()