# NKNU_109_ITE_Graduation_Project

### 本文最後更新時間：3月21日16：06

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

(3)

