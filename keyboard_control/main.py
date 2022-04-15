from djitellopy import tello
from keypress import init, getKeyboardInput, get_key
from time import sleep
import cv2
import face_recognition
import numpy as np

daniielyan_img = face_recognition.load_image_file('/home/daniielyan/Desktop/Tello/images/daniielyan.jpg')
dan_face_encodings = face_recognition.face_encodings(daniielyan_img)[0]

known_face_encodings = [dan_face_encodings]
known_face_names = ['Tatul']

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

init()

me = tello.Tello()
me.connect()
me.stream_on()


while True:
    vals = getKeyboardInput(me)
    print(vals)
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    
    img = me.get_frame_read().frame
    
    img, ret = cv2.VideoCapture(0)
    small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(img, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(img, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', img)

    sleep(0.05)

