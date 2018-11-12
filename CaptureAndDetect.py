import io
import os
import cv2
import SendEmail
import DocChrome
import ParseText

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Detects text using the Google Vision API
def DetectText(image_path):
    from google.cloud import vision
    client = vision.ImageAnnotatorClient();

    with io.open(image_path, 'rb') as image_file:
        content = image_file.read();

    image = vision.types.Image(content=content);
    response = client.text_detection(image=image);
    texts = response.text_annotations;

    for text in texts:

        #print('\n"{}"'.format(text.description))
        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])
        #print('bounds: {}'.format(','.join(vertices)))
    return texts[0].description;

# Captures the image and detects the commands using the Vision API
def GetCommands():
    img_counter = 0;
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Capture Window")

    while True:
        ret, frame = cam.read()
        cv2.imshow("Capture Window", frame)
        if not ret:
            break
        k = cv2.waitKey(1);

        if k%256 == 32:
            # 'SPACE' key is pressed
            img_name = "capt_image_frame.png"
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            break;

    cam.release();
    cv2.destroyAllWindows();
    tempCommand = DetectText(img_name);
    commands = tempCommand.split('\n');
    return commands;


