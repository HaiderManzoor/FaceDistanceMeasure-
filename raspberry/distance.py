
import cv2 as cv
import time
import AiPhile

# variables
# distance from camera to object(face) measured
KNOWN_DISTANCE = 76.2  # centimeter
# width of face in the real world or Object Plane
KNOWN_WIDTH = 14.3  # centimeter
# Colors
GREEN = (0, 255, 0)
RED = (0, 0, 255)
WHITE = (255, 255, 255)
fonts = cv.FONT_HERSHEY_COMPLEX
cap = cv.VideoCapture(0)

# face detector object
face_detector = cv.CascadeClassifier("../haarcascade_frontalface_default.xml")


# focal length finder function
def focal_length(measured_distance, real_width, width_in_rf_image):
    """
    This Function Calculate the Focal Length(distance between lens to CMOS sensor), it is simple constant we can find by using
    MEASURED_DISTACE, REAL_WIDTH(Actual width of object) and WIDTH_OF_OBJECT_IN_IMAGE
    :param1 Measure_Distance(int): It is distance measured from object to the Camera while Capturing Reference image

    :param2 Real_Width(int): It is Actual width of object, in real world (like My face width is = 14.3 centimeters)
    :param3 Width_In_Image(int): It is object width in the frame /image in our case in the reference image(found by Face detector)
    :retrun focal_length(Float):"""
    focal_length_value = (width_in_rf_image * measured_distance) / real_width
    return focal_length_value


# distance estimation function
def distance_finder(focal_length, real_face_width, face_width_in_frame):
    """
    This Function simply Estimates the distance between object and camera using arguments(focal_length, Actual_object_width, Object_width_in_the_image)
    :param1 focal_length(float): return by the focal_length_Finder function

    :param2 Real_Width(int): It is Actual width of object, in real world (like My face width is = 5.7 Inches)
    :param3 object_Width_Frame(int): width of object in the image(frame in our case, using Video feed)
    :return Distance(float) : distance Estimated
    """
    distance = (real_face_width * focal_length) / face_width_in_frame
    return distance


# face detector function
def face_data(image):
    """
    This function Detect the face
    :param Takes image as argument.
    :returns face_width in the pixels
    """

    face_width = 0
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray_image, 1.3, 5)
    for (x, y, h, w) in faces:
        cv.rectangle(image, (x, y), (x + w, y + h), WHITE, 1)
        face_width = w

    return face_width


# reading reference image from directory
ref_image = cv.imread("../Ref_image.png")

ref_image_face_width = face_data(ref_image)
focal_length_found = focal_length(KNOWN_DISTANCE, KNOWN_WIDTH, ref_image_face_width)
print(focal_length_found)
cv.imshow("ref_image", ref_image)
# starting time here
starting_time = time.time()
frame_counter = 0
while True:
    frame_counter += 1
    _, frame = cap.read()

    # calling face_data function
    face_width_in_frame = face_data(frame)
    # finding the distance by calling function Distance
    if face_width_in_frame != 0:
        Distance = distance_finder(focal_length_found, KNOWN_WIDTH, face_width_in_frame)
        # Drwaing Text on the screen
        # cv.putText(
        #     frame, f"Distance = {round(Distance,2)} CM", (50, 50), fonts, 1, (WHITE), 2)
        AiPhile.textBGoutline(
            frame,
            f"Distance = {round(Distance,2)} CM",
            (30, 80),
            scaling=0.5,
            text_color=AiPhile.YELLOW,
        )

    fps = frame_counter / (time.time() - starting_time)
    AiPhile.textBGoutline(frame, f"FPS: {round(fps,2)}", (30, 40), scaling=0.5)
    cv.imshow("frame", frame)
    if cv.waitKey(1) == ord("q"):
        break
cap.release()
cv.destroyAllWindows()
