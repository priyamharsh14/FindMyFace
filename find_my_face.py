import os
import face_recognition
from optparse import OptionParser
import shutil
import time
from PIL import Image
import threading
from queue import Queue

print()
print("  ______ _           _   __  __         ______")
print(" |  ____(_)         | | |  \/  |       |  ____|")
print(" | |__   _ _ __   __| | | \  / |_   _  | |__ __ _  ___ ___ ")
print(" |  __| | | '_ \ / _` | | |\/| | | | | |  __/ _` |/ __/ _ \ ")
print(" | |    | | | | | (_| | | |  | | |_| | | | | (_| | (_|  __/ ")
print(" |_|    |_|_| |_|\__,_| |_|  |_|\__, | |_|  \__,_|\___\___| ")
print("                                 __/ |")
print("                                |___/              ver. 1.2")
print()
print("Author: Priyam Harsh")
print()

parser = OptionParser(usage="Usage: %prog path",version="%prog 1.2")
(options, args) = parser.parse_args()

if len(args) != 1:
    parser.error("[-] Please enter the path to the pictures")

results = []
cdir = os.getcwd()

if "Registered" in os.listdir():
    os.chdir("Registered")
    regface = (os.listdir())[0]
    my_face_encoding = face_recognition.face_encodings(face_recognition.load_image_file(regface))[0]
    my_pics = []
    print("[+] Make sure that your registered face is clear")
    print("[+] Otherwise the program may not work very accurately !!")
    print()
    print("[+] Please Wait while we process all your pics")
else:
    print("[-] No registered face found !!")
    print("[-] Register your face first using register_my_face.py")
    exit()

os.chdir(args[0])
print()

if "my_pictures" in os.listdir():
    shutil.rmtree("my_pictures")
    plist = os.listdir(args[0])
    os.mkdir("my_pictures")
else:
    plist = os.listdir(args[0])
    os.mkdir("my_pictures")

def threader():
    while True:
        worker = q.get()
        Job(worker)
        q.task_done()

def Job(i):
    ext = (i.split("."))[1]
    if ext == "jpg" or ext == "jpeg" or ext == "png":
        img = Image.open(i)
        width, height = img.size
        img = img.resize((width//4, height//4))
        img.save("comp"+i)
        unknown_face_encoding = face_recognition.face_encodings(face_recognition.load_image_file("comp"+i))
        results = [face_recognition.compare_faces([my_face_encoding], en, tolerance=0.45) for en in unknown_face_encoding]
        for ch in results:
            if True in ch:
                with threading.Lock():
                    print("[+] Found Your Face in",i)
                shutil.copy(i,"my_pictures")
        results = []
        os.remove("comp"+i)

q = Queue()

for x in range(10):
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start()

start = time.time()

for worker in plist:
    q.put(worker)

q.join()

end = time.time()

os.chdir(cdir)
shutil.rmtree("Registered")

print()
print("[+] Time Taken:",(end - start))
