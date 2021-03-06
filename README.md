# NKNU_109_ITE_Graduation_Project

### 本文最後更新時間：5月4日11：20

### 0.[TensorFlow Lite Object Detection and Image Classification on Jetson Nano](https://github.com/e96031413/TensorFlow-Lite-Object-Detection-and-Image-Classification-on-Jetson-Nano)

[文章：NVIDIA Jetson Nano學習筆記（七）：即時影像偵測暨辨識系統(PiCamera+OpenCV+TensorFlow Lite+Firebase](https://medium.com/@yanweiliu/nvidia-jetson-nano-tensorflow-lite-object-detection-and-image-classification-with-picamera-opencv-firebase-3cffabf8d980)

[1] 載入Object Detection和Image Classification的TFLite Model。

[2] 透過OpenCV讀取frame進行Real-Time Object Detection。

[3] 如果偵測到指定Object(例如："bird"), 保存圖片。

[4] 針對該圖片進行Image Classification。

[5] 上傳該張圖片和Image Classification的結果(LabelName, ScoreValue, Time, Pubic-Access Image Url)至Firebase資料庫。

[6] 將資料(LabelName, ScoreValue, Time, Pubic-Access Image Url)透過附加模式保存成一個CSV檔案，避免被複寫。

[7] 當圖片和資料被上傳到Firebase後，刪除本地端圖片，避免SD卡的磁碟空間用盡。

---

### 目前所嘗試過可行的影像偵測方法：

### 1.[使用YOLOv3演算法進行水雉辨識](https://github.com/e96031413/My-Programming-Project/tree/master/YOLOv3%E6%B0%B4%E9%9B%89%E8%BE%A8%E8%AD%98)

從去年9月參加聯發科比賽,就一直使用的方法。

------

### 2.[Google Cloud使用筆記(六)：使用 Cloud AutoML Vision訓練影像辨識模型(Tensorflow Lite)](https://medium.com/@yanweiliu/google-cloud-automl-vision-model-training-d80fabc17dfe)

#### **想法：**

AutoML Vision是一個很方便的線上服務,可以在**線上進行Model訓練**,也**不用自己手動標記框框**,
就能自動訓練模型,目前模型準確度達75%,也可以**匯出成API**或是**Tensorflow Lite的Model**。

#### **3/3日將測試版本的Model上傳到GitHub上**



**搭配Python API**：讓Jetson Nano或是Raspberry Pi進行線上辨識,減輕硬體負擔



**[搭配React Native的API](https://github.com/shaqian/tflite-react-native/tree/master/example)**：可完成Android的辨識APP開發



3/4日完成5種水鳥的模型訓練(https://github.com/e96031413/NKNU_109_ITE_Graduation_Project/tree/master/TensorFlow%20Model/5%E7%A8%AE%E4%B8%8D%E5%90%8C%E6%B0%B4%E9%B3%A5)

* Black_Coot
* Gallinula_chloropus
* Green_winged_Teal
* Little_Grebe
* Pheasant_tailed_Jacana


**精確度 97.76%、喚回度86.18%**

參考NKNU_109_ITE_Graduation_Project/TensorFlow Model/5種不同水鳥/

------



### 3.[Google Cloud使用筆記(五)：使用 Google Vision API進行影像辨識](https://medium.com/@yanweiliu/google-cloud%E4%BD%BF%E7%94%A8%E7%AD%86%E8%A8%98-%E4%BA%94-%E4%BD%BF%E7%94%A8-google-vision-api%E9%80%B2%E8%A1%8C%E5%BD%B1%E5%83%8F%E8%BE%A8%E8%AD%98-51aabc2064ff)

#### **程式碼：**

**demo1.py**：[Vision API使用範例](https://github.com/e96031413/NKNU_109_ITE_Graduation_Project/blob/master/demo1.py)

#### **介紹：**

Google Vision API不需要訓練模型,可以直接辨識出圖片中的物件名稱。能傳回如下的JSON格式資訊：

**web detection在網路上搜尋相似圖片，並從這些搜尋結果中提取內容，回傳圖片更多相關資訊。**
web detection將會是我**主要的選擇**。

[web detection 官方線上 demo](https://cloud.google.com/vision#section-2)：線上版測試

[web detection python demo](https://gist.github.com/e96031413/300c91efe5671f8f29c0771116cc303d#file-google_cloud_vision_api-py)：實際的Python程式碼

[web detection回傳結果](https://gist.github.com/e96031413/147563e2bc4f947d0c6f2e8a9c564f8d)：回傳的JSON格式資訊



#### **Vision API功能簡介**

| 功能                                | 說明                                                         |
| ----------------------------------- | ------------------------------------------------------------ |
| Label Detection                     | 可以告訴你這圖片是什麼                                       |
| OCR (Optical Character Recognition) | 解析你圖片中的文字內容，告訴你圖片中哪裡有文字，甚至可以告訴你這是什麼語言。 |
| Logo Detection                      | 專門辨識公司logo用的                                         |
| Face Detection                      | 指出臉部的喜怒哀樂、特徵、位置、是否有戴眼鏡、是否模糊等。   |
| Landmark Detection                  | 如果這圖片包含著常見的地標，他可以告訴你是什麼地標。 同時提供對應地標的經度、緯度 |
| Crop hints                          | 可以幫助你裁剪照片，以符合你想要做的主題。                   |
| Explicit Content Detection          | 檢測圖片中是否有不適當的內容。 adult(成人)、spoof(詐騙)、medical(藥物)、violence(暴力) |
| Landmark                            | 地標偵測，圖片中的地點在哪裡                                 |

------

### 4.[Multiple Object Detectors Sample App](https://github.com/e96031413/multiple-object-detectors)

A quick guide to using multiple object detection models with always AI

可混合多個模型一起辨識的程式，不同模型的辨識結果(偵測框)以顏色區別表示

### 5.[Tensorflow_Lite_Demo](https://github.com/e96031413/NKNU_109_ITE_Graduation_Project/tree/master/Tensorflow_Lite_Demo)

2020/03/13更新：

[NVIDIA Jetson Nano學習筆記（四）：安裝與執行Tensorflow Lite Model官方範例](https://medium.com/@yanweiliu/tflite-on-jetson-nano-c480fdf9ac2)

成功在Jetson Nano上執行TF Lite的Model

### 6.[LocalDataToFirebase.py](https://github.com/e96031413/NKNU_109_ITE_Graduation_Project/blob/master/LocalDataToFirebase.py)

2020/03/18更新：

成功製作Firebase的測試資料，供後續React Native APP串接測試

### 7.[picamera_classification.py](https://github.com/e96031413/NKNU_109_ITE_Graduation_Project/blob/master/picamera_classification.py)

2020/03/21更新：

[NVIDIA Jetson Nano學習筆記（五）：即時影像分類系統(PiCamera+OpenCV+TensorFlow Lite+Firebase)](https://medium.com/@yanweiliu/nvidia-jetson-nano%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98-%E4%BA%94-%E5%8D%B3%E6%99%82%E5%BD%B1%E5%83%8F%E5%88%86%E9%A1%9E%E7%B3%BB%E7%B5%B1-picamera-opencv-tensorflow-lite-firebase-3aefbf5a1784)

**功能：**
    
(1)使用OpenCV讀取PiCamera鏡頭，並透過Pillow與NumPy將OpenCV格式轉換成Tensorflow Lite能讀取的格式

(2)目前只記錄Score > 0.7的辨識成果（label、Score、Time、fileName），用pandas輸出成CSV檔案(附加模式，避免覆蓋掉先前的辨識成果)，供後續資料分析

(3)用指定檔名保存辨識圖片(辨識出來的名稱與隨機數字作為檔名)

(4)已將辨識成果（label、Score、Time、fileName）以及辨識圖片上傳至Firebase資料庫，供後續React Native APP串接使用

**目前已知BUG：**

(1)暫時無法將辨識成果（label、Score、Time、fileName）文字加到辨識圖片中(cv2.putText)

(2)還沒處理UnKnown標籤

(3)鏡頭若搖晃太大力會有誤判情況產生(低解析度)

### 8.[實際使用程式](https://github.com/e96031413/NKNU_109_ITE_Graduation_Project/tree/master/%E5%AF%A6%E9%9A%9B%E4%BD%BF%E7%94%A8%E7%A8%8B%E5%BC%8F)

2020/03/24更新:

將功能從[picamera_classification.py](https://github.com/e96031413/NKNU_109_ITE_Graduation_Project/blob/master/picamera_classification.py)分開出來

1.[offline_picamera_classification.py](https://github.com/e96031413/NKNU_109_ITE_Graduation_Project/blob/master/%E5%AF%A6%E9%9A%9B%E4%BD%BF%E7%94%A8%E7%A8%8B%E5%BC%8F/offline_picamera_classification.py)

在Jetson Nano進行離線辨識，並且保存「拍攝照片」及「CSV檔案」。

2.[PC_to_Firebase.py](https://github.com/e96031413/NKNU_109_ITE_Graduation_Project/blob/master/%E5%AF%A6%E9%9A%9B%E4%BD%BF%E7%94%A8%E7%A8%8B%E5%BC%8F/PC_to_Firebase.py)

當SD卡中的內容取回(照片、CSV檔案)後，在PC端使用pandas讀取CSV資料，並透過Firebase的套件，分別將「拍攝照片」、「資料」上傳到Firebase。

3/4日完成5種水鳥的模型訓練(https://github.com/e96031413/NKNU_109_ITE_Graduation_Project/tree/master/TensorFlow%20Model/5%E7%A8%AE%E4%B8%8D%E5%90%8C%E6%B0%B4%E9%B3%A5)

### 9.[上傳9種水鳥的Model](https://github.com/e96031413/NKNU_109_ITE_Graduation_Project/tree/master/TensorFlow%20Model/9%E7%A8%AE%E4%B8%8D%E5%90%8C%E6%B0%B4%E9%B3%A5)

2020/03/31更新：

* Egretta_garzetta
* Black_Coot
* Gallinula_chloropus
* Fulica_atra
* Himantopus_himantopus
* Ixobrychus_sinensis
* Green_winged_Teal
* Little_Grebe
* Pheasant_tailed_Jacana


**精確度 94.49%、喚回度81.68%**

參考NKNU_109_ITE_Graduation_Project/TensorFlow Model/9種不同水鳥/

### 10.[使用GluonCV的Pre-trained SSD Model](https://gist.github.com/e96031413/9f785510d338041e19e343ab1be98831)

在Windows 10的作業系統，使用Pre-trained的SSD演算法Model，搭配GTX 750 Ti的GPU進行推論，花費約16秒的時間偵測一張圖片

以這樣的速度下來會發現，推論速度太慢，無法做到即時辨識。



### 10.[使用Pre-trained Object Detection TFLite Model](https://github.com/e96031413/NKNU_109_ITE_Graduation_Project/tree/master/TensorFlow%20Model/TFLite_Object_Dection_Model)

2020/04/15更新：

構想是：

先用[開源的Object Dection Model](https://tfhub.dev/s?deployment-format=lite&module-type=image-object-detection)進行物件偵測，產生出Bounding Boxes後，再透過Image Classification Model進行Bird Species判斷

2020/04/27更新：

該構想不可行。

根據網路上及自己實測的結果，同一個Camera只能在同個程式裡面被OpenCV的VideoCapture讀取一次，不能重複。

因此，每個Camera只能執行Object Detection或Image Classification其中一個任務而已。

參考:

(1)[Using two VideoCaptures in openCV to capture the same device](https://stackoverflow.com/questions/44737963/using-two-videocaptures-in-opencv-to-capture-the-same-device)

(2)[Multiple VideoCapture on one camera](https://stackoverflow.com/questions/22249692/multiple-videocapture-on-one-camera)

2020/04/27更新-老師提供的解決方案:
使用Object Detection，if object_name == 'bird'，拍攝圖片，並且保存到Local，接著讀取Local圖片，再透過Image Classification讀取圖片進行辨識

```
# Pseudocode of the concept

def prediction():
    
    Model_SETUP()

    Object_Dection()

    if labelName == "Bird":
        Image_Classification()
        
        if prob >0.7:
            save_img()
            img_to_firebase()
            result_to_firebase()
            save_to_csv()
```
2020/04/24更新:

[ObjectDetection_on_Nano.py](https://github.com/e96031413/NKNU_109_ITE_Graduation_Project/blob/master/ObjectDetection_on_Nano.py)

完成Object Detection的程式

目前FPS約在4.X

使用Google的quantized SSDLite-MobileNet-v2 object detection model

[NVIDIA Jetson Nano學習筆記（六）：即時影像偵測系統(PiCamera+OpenCV+TensorFlow Lite)](https://medium.com/@yanweiliu/tensorflow-lite-real-time-object-detection-with-pi-camera-on-nvidia-jetson-nano-4118e50eee15)
