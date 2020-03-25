'''
在PC端將資料（label、Score、Time、fileName）及圖片上傳至Firebase，
並顯示圖片公開連結、保存CSV檔（label、Score、Time、fileName）
'''

import os
import time
import re
import pandas as pd
import json
from firebase import firebase
from google.cloud import storage

# Connect to Firebase
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="test-e7b86-firebase-adminsdk-mx71i-44949f41e3.json"
db_url="https://test-e7b86.firebaseio.com"
fdb=firebase.FirebaseApplication(db_url,None)
client = storage.Client()
bucket = client.get_bucket('test-e7b86.appspot.com')

# Find jpg in the folder

fileName=''

for file in os.listdir("C:/Users/Administrator/Desktop/test/"):
    fileName = fileName + file + " "

jpgRegex = re.compile(r"\w+\.jpg")
newfileName = jpgRegex.findall(fileName)


# Upload image to Firebase

for i in newfileName:
    imagePath = "C:/Users/Administrator/Desktop/test/" + i    # Replace it with your own path
    imageBlob = bucket.blob(i)
    imageBlob.upload_from_filename(imagePath)    # Upload image to firebase
    imageBlob.make_public()
    print('圖片上傳成功!')
    

# Read data from csv and convert it to json
df = pd.read_csv('bird_data.csv').to_json()  # dataframe to JSON
df = json.loads(df)  # Convert to real JSON

# Upload data to Firebase
firebase_data =[{'label':df['Label'],'Score':df['Score'],'Time':df['Time'],'fileName':df['fileName'],'image_url': df['image_url']}]

for data in firebase_data:
    fdb.post('bird-data',data)
    print('資料上傳成功!')
    time.sleep(3)