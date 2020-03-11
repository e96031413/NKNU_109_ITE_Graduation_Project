import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"path/To/JSON.json"
# Instantiates a client
client = vision.ImageAnnotatorClient()


# The name of the image file to annotate
file_name = os.path.abspath('test.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)


'''
# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')

for label in labels:
    print(label.description)
'''
# Performs web detection on the image file

response = client.web_detection(image=image,max_results=3)
target = response.web_detection
print(target)


for item in target:
    print('description:',item.description)
    print('score:',item.score)
    print('\n')

'''
# Performs objects detection on the image file

response = client.object_localization(image=image)
target = response.localized_object_annotations
print(target)

for item in target:
    print(item.name)
    print(item.score)
'''