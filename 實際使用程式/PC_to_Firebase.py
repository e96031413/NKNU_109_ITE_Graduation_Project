'''
在PC端將資料（label、Score、Time、fileName）及圖片上傳至Firebase，
並顯示圖片公開連結、保存CSV檔（label、Score、Time、fileName）
'''

import os
import glob
import time
import pandas as pd
from firebase import firebase
from google.cloud import storage


# Upload data to Firebase
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="firebase_key.json   #This file is downloaded from FireBaseProject -> Settings -> serviceaccounts -> click the button to get your CREDENTIALS
db_url='https://test-e7b86.firebaseio.com'    
fdb=firebase.FirebaseApplication(db_url,None)

# Upload image to Firebase
client = storage.Client()
bucket = client.get_bucket('test-e7b86.appspot.com')

image_files = glob.glob("path/to/img/dir/*.jpg")



for images in image_files:
  imagePath = "path/to/image/" + fileName    # Replace "/home/e96031413" with your own path
  imageBlob = bucket.blob(fileName)
  imageBlob.upload_from_filename(imagePath)    # Upload image to firebase
  imageBlob.make_public()
  publicURL = imageBlob.public_url

df = pd.read_csv('bird_data.csv')

firebase_data =[{'label':df.Label,'Score':df.Score,'Time':df.Time,'fileName':df.fileName,'image_url':},]
for data in firebase_data:
    fdb.post('bird-data',data)
    time.sleep(3)