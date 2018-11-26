import face_recognition
import cv2
import win32com.client as wincl
import numpy as np


# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

#init text to speach
speak = wincl.Dispatch("SAPI.SpVoice")

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a pictures and learn how to recognize it.
# Load a pictures and learn how to recognize it.
kosta1 = face_recognition.load_image_file("dataset\\kosta\\1.jpg")
kosta1_face_encoding = face_recognition.face_encodings(kosta1)[0]
kosta2 = face_recognition.load_image_file("dataset\\kosta\\2.jpg")
kosta2_face_encoding = face_recognition.face_encodings(kosta2)[0]
kosta3 = face_recognition.load_image_file("dataset\\kosta\\3.jpg")
kosta3_face_encoding = face_recognition.face_encodings(kosta3)[0]
kosta4 = face_recognition.load_image_file("dataset\\kosta\\4.jpg")
kosta4_face_encoding = face_recognition.face_encodings(kosta4)[0]
kosta5 = face_recognition.load_image_file("dataset\\kosta\\5.jpg")
kosta5_face_encoding = face_recognition.face_encodings(kosta5)[0]

jasmina1 = face_recognition.load_image_file("dataset\\jasmina\\1.jpg")
jasmina1_face_encoding = face_recognition.face_encodings(jasmina1)[0]
jasmina2 = face_recognition.load_image_file("dataset\\jasmina\\2.jpg")
jasmina2_face_encoding = face_recognition.face_encodings(jasmina2)[0]
jasmina3 = face_recognition.load_image_file("dataset\\jasmina\\3.jpg")
jasmina3_face_encoding = face_recognition.face_encodings(jasmina3)[0]
jasmina4 = face_recognition.load_image_file("dataset\\jasmina\\4.jpg")
jasmina4_face_encoding = face_recognition.face_encodings(jasmina4)[0]
jasmina5 = face_recognition.load_image_file("dataset\\jasmina\\5.jpg")
jasmina5_face_encoding = face_recognition.face_encodings(jasmina5)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    kosta1_face_encoding,
    kosta2_face_encoding,
    kosta3_face_encoding,
    kosta4_face_encoding,
    kosta5_face_encoding,
    jasmina1_face_encoding,
    jasmina2_face_encoding,
    jasmina3_face_encoding,
    jasmina4_face_encoding,
    jasmina5_face_encoding
]

known_face_names = [
    "Kosta",
    "Kosta",
    "Kosta",
    "Kosta",
    "Kosta",
    "Jasmina",
    "Jasmina",
    "Jasmina",
    "Jasmina",
    "Jasmina"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

        if not np.array_equal(names, face_names):
            names = face_names;
            #say the names
            for name in names:
                speak.Speak("Yo " + name)

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()