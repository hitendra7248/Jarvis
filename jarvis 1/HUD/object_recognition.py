from imageai.Detection import ObjectDetection

#The script below creates an object of the object detection class.
obj_detect = ObjectDetection()

#The next step is to set the model type for object detection. Since we’ll be using the YOLO algorithm, you need to call the setModelTypeAsYOLOv3() method as shown in the script below:
obj_detect.setModelTypeAsYOLOv3()

#To load the model, first you need to call the setModelPath() method from your ObjectDetection class object and pass it the path where you downloaded the yolo.h5 model. Next, you need to call the loadModel() method to actually load the model. Look at the following script for reference:
obj_detect.setModelPath(r"archive\yolo.h5")
obj_detect.loadModel()

#The next step is to capture your webcam stream. To do so, execute the script below:
import cv2

URL = 'http://25.251.55.246:8080/video'
cam_feed = cv2.VideoCapture(URL)


#Next, you need to define height and width for the frame that will display the detected objects from your live feed. Execute the following script to do so, recognizing you can change the integer values near the end to match your desired dimensions:
cam_feed.set(cv2.CAP_PROP_FRAME_WIDTH, 650)
cam_feed.set(cv2.CAP_PROP_FRAME_HEIGHT, 750)

#The frame returned by the detectObjectsFromImage() method is then passed to the imshow() method of the OpenCV module which displays the current frame containing our detected objects. This is what shows each frame of your video on your screen in real-time. The process continues until you press the “q” or “ESC” key on your keyboard.
while True:    
    ret, img = cam_feed.read()   
    annotated_image, preds = obj_detect.detectObjectsFromImage(input_image=img,
                    input_type="array",
                      output_type="array",
                      display_percentage_probability=False,
                      display_object_name=True)

    cv2.imshow("", annotated_image)     
    
    if (cv2.waitKey(1) & 0xFF == ord("q")) or (cv2.waitKey(1)==27):
        break

cam_feed.release()
cv2.destroyAllWindows()

#The first step is to import the VideoObjectDetection class, like this:
from imageai.Detection import VideoObjectDetection

#The script below creates an object of the VideoObjectDetection class:
vid_obj_detect = VideoObjectDetection()

#Next, you have to set the model type for object detection from videos, just like you did in the last section.
vid_obj_detect.setModelTypeAsYOLOv3()

#The following script sets the path to the YOLO model and loads the model.
vid_obj_detect.setModelPath(r"C:/Datasets/yolo.h5")
vid_obj_detect.loadModel()

#Here you can see that the only change from the script we used to detect objects from videos is the presence of the camera_input attribute whose value is equal to the camera object that captures your webcam stream. Also, the detection_timeout attribute is set to 3 which means that the function detectObjectsFromVideo() will terminate after detecting objects for 3 seconds from your input camera stream.
detected_vid_obj = vid_obj_detect.detectObjectsFromVideo(
    camera_input=cam_feed,
    output_file_path = r"C:/Datasets/output_video",
    frames_per_second=15,
    log_progress=True,
    return_detected_frame = True,
    detection_timeout=3
)

print(detected_vid_obj)