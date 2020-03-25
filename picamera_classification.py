'''
連線版完整版程式，能在Jetson Nano上直接把資料（label、Score、Time、fileName）及圖片上傳至Firebase，
並顯示圖片公開連結、保存CSV檔（label、Score、Time、fileName）
'''


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import io
import os
import time
import random
import numpy as np
import cv2
import pandas as pd
from firebase import firebase
from google.cloud import storage

from PIL import Image
from tflite_runtime.interpreter import Interpreter

def gstreamer_pipeline(
    capture_width=224,
    capture_height=224,
    display_width=224,
    display_height=224,
    framerate=30,
    flip_method=0,
):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )



def load_labels(path):
  with open(path, 'r') as f:
    return {i: line.strip() for i, line in enumerate(f.readlines())}


def set_input_tensor(interpreter, image):
  tensor_index = interpreter.get_input_details()[0]['index']
  input_tensor = interpreter.tensor(tensor_index)()[0]
  input_tensor[:, :] = image


def classify_image(interpreter, image, top_k=1):
  """Returns a sorted array of classification results."""
  set_input_tensor(interpreter, image)
  interpreter.invoke()
  output_details = interpreter.get_output_details()[0]
  output = np.squeeze(interpreter.get_tensor(output_details['index']))

  # If the model is quantized (uint8 data), then dequantize the results
  if output_details['dtype'] == np.uint8:
    scale, zero_point = output_details['quantization']
    output = scale * (output - zero_point)

  ordered = np.argpartition(-output, top_k)
  return [(i, output[i]) for i in ordered[:top_k]]


def main():
  parser = argparse.ArgumentParser(
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument(
      '--model', help='File path of .tflite file.', required=True)
  parser.add_argument(
      '--labels', help='File path of labels file.', required=True)
  args = parser.parse_args()

  labels = load_labels(args.labels)

  interpreter = Interpreter(args.model)
  interpreter.allocate_tensors()
  _, height, width, _ = interpreter.get_input_details()[0]['shape']
  cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)

  if cap.isOpened():
    window_handle = cv2.namedWindow("CSI Camera", cv2.WINDOW_AUTOSIZE)
    # Window
    while cv2.getWindowProperty("CSI Camera", 0) >= 0:
      # cv2.imshow function should use "img";classify_image function should use "image". Because of the file type.
      ret_val, img = cap.read()
      cv2.imshow("CSI Camera", img)
      image = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
      start_time = time.time()
      results = classify_image(interpreter, image)
      elapsed_ms = (time.time() - start_time) * 1000
      label_id, prob = results[0]
      seconds = time.time()
      local_time=time.ctime(seconds)

      #font = cv2.FONT_HERSHEY_SIMPLEX
      #color = (0, 0, 255)
      if prob > 0.7:
        print("LabelName:",labels[label_id])
        print("ScoreValue:",prob)
        print("Time:",local_time)
        #img=cv2.putText(img, labels[label_id], (10, 10), font,1, color, 1) #LabelName
        #img=cv2.putText(img, prob, (10, 20), font,1, color, 1) #ScoreValue
        #img=cv2.putText(img, local_time, (10, 30), font, 1, color, 1) #Time

        # fileName: use label name + random number as our file name.
        fileName =labels[label_id] + str(random.randint(1,99999)) + '.jpg'

        # Write image to labelName.jpg
        cv2.imwrite(fileName,img)

        # Upload data to Firebase
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="firebase_key.json   #This file is downloaded from FireBaseProject -> Settings -> serviceaccounts -> click the button to get your CREDENTIALS
        db_url='https://test-e7b86.firebaseio.com'    
        fdb=firebase.FirebaseApplication(db_url,None)

        # Upload image to Firebase
        client = storage.Client()
        bucket = client.get_bucket('test-e7b86.appspot.com')

        imagePath = "/home/e96031413/" + fileName    # Replace "/home/e96031413" with your own path
        imageBlob = bucket.blob(fileName)

        imageBlob.upload_from_filename(imagePath)    # Upload image to firebase
        imageBlob.make_public()
        publicURL = imageBlob.public_url

        firebase_data =[{'label':labels[label_id],'Score':prob,'Time':local_time,'fileName':fileName,'image_url':publicURL},]
        for data in firebase_data:
          fdb.post('bird-data',data)
          time.sleep(3)

        # Save to CSV file with pandas
        pandas_data = {'Label':labels[label_id],'Score':prob,'Time':local_time,'fileName':fileName,'image_url':publicURL}
        df = pd.DataFrame(data=pandas_data,index=[0])
        df.to_csv('bird_data.csv',mode='a',encoding='utf8')  # Use append mode so that the csv file won't be replaced by new files

      # keyCode detects which key you press
      keyCode = cv2.waitKey(30) & 0xFF
      # Stop the program on the ESC key
      if keyCode == 27:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
  main()