import cv2
import os
import face_recognition
import shutil

cam = cv2.VideoCapture(0)

r = 0

print()
print("********** Register Your Face **********")
print()
n = input("Enter your name: ")
print()
print("Getting the camera ready..")

cv2.namedWindow("Capture")
if "Registered" not in os.listdir():
    os.mkdir("Registered")

os.chdir("Registered")

print()
print("Press Space whenever ready..")
print("Press Esc to cancel the registration..")
print()

while True:
    ret, frame = cam.read()
    cv2.imshow("Capture", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        r = 1
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "{}.jpg".format(n)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        break

if r is 0:
    picture_of_me = face_recognition.load_image_file((n+".jpg"))
    my_face_encoding = face_recognition.face_encodings(picture_of_me)
    if len(my_face_encoding) == 0:
        print("We couldn't recognize any face !")
        print("Please try again !!")
        shutil.rmtree("Registered")
    else:
        print("Registration Successful !!")
elif r is 1:
    print("Registration Cancelled !!")

cam.release()
