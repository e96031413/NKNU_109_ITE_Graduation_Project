# NKNU_109_ITE_Graduation_Project

### 最後更新時間：3月1日下午1點30分

### 目前所嘗試過可行的影像偵測方法：

------



#### 1.[使用YOLOv3演算法進行水雉辨識](https://github.com/e96031413/My-Programming-Project/tree/master/YOLOv3%E6%B0%B4%E9%9B%89%E8%BE%A8%E8%AD%98)

從去年9月參加聯發科比賽,就一直使用的方法。

#### 2.[Google Cloud使用筆記(六)：使用 Cloud AutoML Vision訓練影像辨識模型(Tensorflow Lite)](https://medium.com/@yanweiliu/google-cloud-automl-vision-model-training-d80fabc17dfe)

**想法：**

AutoML Vision是一個很方便的線上服務,可以在**線上進行Model訓練**,也**不用自己手動標記框框**,
就能自動訓練模型,目前模型準確度達75%,也可以**匯出成API**或是**Tensorflow Lite的Model**。

**搭配Python API**：讓Jetson Nano或是Raspberry Pi進行線上辨識,減輕硬體負擔
**[搭配React Native的API](https://github.com/shaqian/tflite-react-native/tree/master/example)**：可完成Android的辨識APP開發

#### 3.[Google Cloud使用筆記(五)：使用 Google Vision API進行影像辨識](https://medium.com/@yanweiliu/google-cloud%E4%BD%BF%E7%94%A8%E7%AD%86%E8%A8%98-%E4%BA%94-%E4%BD%BF%E7%94%A8-google-vision-api%E9%80%B2%E8%A1%8C%E5%BD%B1%E5%83%8F%E8%BE%A8%E8%AD%98-51aabc2064ff)

**想法：**

Google Vision API不需要訓練模型,可以直接辨識出圖片中的物件名稱。能傳回如下的JSON格式資訊：

**web detection在網路上搜尋相似圖片，並從這些搜尋結果中提取內容，回傳圖片更多相關資訊。**
web detection將會是我主要的選擇。
[web detection方法使用demo](https://gist.github.com/e96031413/300c91efe5671f8f29c0771116cc303d#file-google_cloud_vision_api-py)

`web_entities {
  entity_id: "/g/11fs7n3mgw"
  score: 1.1109451055526733
  description: "Jacana Ecological Education Park"
}
web_entities {
  entity_id: "/m/029xmf"
  score: 1.0777499675750732
  description: "Pheasant-tailed jacana"
}
web_entities {
  entity_id: "/m/015p6"
  score: 0.8730000257492065
  description: "Birds"
}
web_entities {
  entity_id: "/m/01bx84"
  score: 0.6162999868392944
  description: "Ring-necked Pheasant"
}
web_entities {
  entity_id: "/m/0hkf"
  score: 0.5040000081062317
  description: "Agriculture"
}
web_entities {
  entity_id: "/m/02mhj"
  score: 0.4456131160259247
  description: "Ecosystem"
}
web_entities {
  entity_id: "/g/120ylh5n"
  score: 0.4172999858856201
  description: "chick"
}
web_entities {
  entity_id: "/m/02r53yt"
  score: 0.41280001401901245
  description: "Satoyama"
}
web_entities {
  entity_id: "/m/01p1m6"
  score: 0.38260000944137573
  description: "Little egret"
}
web_entities {
  entity_id: "/m/0b3tck"
  score: 0.3276999890804291
  description: "Melanocharitidae"
}
full_matching_images {
  url: "http://5b0988e595225.cdn.sohucs.com/images/20171120/c00bb5a2afd14b5cb1b7db1be77af268.jpeg"
}
full_matching_images {
  url: "https://case.ntu.edu.tw/blog/wp-content/uploads/2014/07/%E5%9C%96%E7%89%874-1024x683.jpg"
}
full_matching_images {
  url: "http://nc.biodiv.tw/bbs/attachment.php?attachmentid=709000&d=1405604768"
}
full_matching_images {
  url: "https://i2.kknews.cc/SIG=l30caq/47170002pqnr2sons7sr.jpg"
}
full_matching_images {
  url: "https://pic3.zhimg.com/v2-1554a8ef1b8d26658fad866398680c9e_b.jpg"
}
full_matching_images {
  url: "https://i.pinimg.com/236x/99/3a/05/993a053a524ba8c318e591fdc5838cdc--birdwatching-pheasant.jpg"
}
full_matching_images {
  url: "https://ti2.kknews.cc/SIG=qphouq/39s6000075118s105051_s.jpg"
}
partial_matching_images {
  url: "http://5b0988e595225.cdn.sohucs.com/images/20190516/dec4bdf0ab4848088a1004b4c6806852.jpeg"
}
partial_matching_images {
  url: "https://ti2.kknews.cc/SIG=qphouq/39s6000075118s105051_240x240.jpg"
}
pages_with_matching_images {
  url: "https://www.pinterest.com/agavegal54/melanocharitidae-berrypeckers-longbills/"
  page_title: "10 Best Melanocharitidae-berrypeckers longbills images | Birds ..."
  full_matching_images {
    url: "https://i.pinimg.com/236x/99/3a/05/993a053a524ba8c318e591fdc5838cdc--birdwatching-pheasant.jpg"
  }
}
pages_with_matching_images {
  url: "https://www.pinterest.com/siggyhouse/birds-melanocharitidae-berrypickers/"
  page_title: "9 Best Birds-Melanocharitidae-Berrypickers images | Birds, Animals ..."
  full_matching_images {
    url: "https://i.pinimg.com/236x/99/3a/05/993a053a524ba8c318e591fdc5838cdc--birdwatching-pheasant.jpg"
  }
}
pages_with_matching_images {
  url: "https://case.ntu.edu.tw/blog/?p=18663"
  page_title: "\343\200\220<b>\347\224\237\346\205\213</b>\344\277\235\350\202\262\343\200\221\345\217\260\345\215\227\346\260\264\351\233\211\347\232\204<b>\345\276\251\350\202\262</b>\346\225\205\344\272\213| CASE\345\240\261\347\247\221\345\255\270"
  full_matching_images {
    url: "https://case.ntu.edu.tw/blog/wp-content/uploads/2014/07/%E5%9C%96%E7%89%874-1024x683.jpg"
  }
}
pages_with_matching_images {
  url: "https://kknews.cc/agriculture/kr2ypvv.html"
  page_title: "\351\207\214\345\261\261\345\200\241\350\255\260\357\274\214<b>\347\224\237\346\205\213</b>\346\260\270\347\272\214\344\270\215\345\217\252\346\230\257\345\257\253\345\234\250\347\264\231\344\270\212\347\232\204\345\205\254\347\264\204- \346\257\217\346\227\245\351\240\255\346\242\235"
  full_matching_images {
    url: "https://i2.kknews.cc/SIG=l30caq/47170002pqnr2sons7sr.jpg"
  }
}
pages_with_matching_images {
  url: "https://kknews.cc/zh-hk/agriculture/kr2ypvv.html"
  page_title: "\351\207\214\345\261\261\345\200\241\350\255\260\357\274\214<b>\347\224\237\346\205\213</b>\346\260\270\347\272\214\344\270\215\345\217\252\346\230\257\345\257\253\345\234\250\347\264\231\344\270\212\347\232\204\345\205\254\347\264\204- \346\257\217\346\227\245\351\240\255\346\242\235"
  full_matching_images {
    url: "https://i2.kknews.cc/SIG=l30caq/47170002pqnr2sons7sr.jpg"
  }
}
pages_with_matching_images {
  url: "http://nc.biodiv.tw/bbs/showthread.php?t=53146"
  page_title: "\345\217\260\345\215\227\346\260\264\351\233\211\347\232\204<b>\345\276\251\350\202\262</b>\346\225\205\344\272\213--\346\202\274\347\277\201\346\246\256\347\202\253\351\263\245\345\217\213- \350\207\252\347\204\266\346\224\235\345\275\261\344\270\255\345\277\203Nature Campus"
  full_matching_images {
    url: "http://nc.biodiv.tw/bbs/attachment.php?attachmentid=709000&d=1405604768"
  }
}
pages_with_matching_images {
  url: "http://nc.biodiv.tw/bbs/showthread.php?t=53146&langid=1"
  page_title: "\345\217\260\345\215\227\346\260\264\351\233\211\347\232\204<b>\345\276\251\350\202\262</b>\346\225\205\344\272\213--\346\202\274\347\277\201\346\246\256\347\202\253\351\263\245\345\217\213- \350\207\252\347\204\266\346\224\235\345\275\261\344\270\255\345\277\203Nature Campus"
  full_matching_images {
    url: "http://nc.biodiv.tw/bbs/attachment.php?attachmentid=709000&d=1405604768"
  }
}
pages_with_matching_images {
  url: "https://kknews.cc/news/ky66lo8.html"
  page_title: "<b>\347\224\237\346\205\213</b>\350\276\262\350\200\225\347\232\204\347\233\243\346\270\254\351\263\245\357\274\232\344\275\240\347\232\204\350\200\225\345\234\260\346\234\211\346\262\222\346\234\211\350\242\253\346\261\241\346\237\223\357\274\214\347\231\275\351\267\272\351\267\245\347\237\245\351\201\223\347\255\224\346\241\210\357\274\201 - \346\257\217\346\227\245 ..."
  partial_matching_images {
    url: "https://ti2.kknews.cc/SIG=qphouq/39s6000075118s105051_240x240.jpg"
  }
}
pages_with_matching_images {
  url: "https://kknews.cc/travel/m6y9qz.html"
  page_title: "\347\221\244\347\221\244\345\217\260\347\201\243\347\234\213\346\277\225\345\234\260\342\200\224\342\200\224\347\254\254\344\270\200\345\244\251\357\274\232\347\224\260\350\243\241\346\234\211\350\205\263\345\215\260- \346\257\217\346\227\245\351\240\255\346\242\235"
  full_matching_images {
    url: "https://ti2.kknews.cc/SIG=qphouq/39s6000075118s105051_s.jpg"
  }
}
pages_with_matching_images {
  url: "https://kknews.cc/agriculture/8knnnn.html"
  page_title: "\345\215\232\347\211\251\351\244\250\350\243\241\345\273\272\344\272\206\345\200\213\343\200\214\350\217\234\345\270\202\345\240\264\343\200\215 - \346\257\217\346\227\245\351\240\255\346\242\235"
}
visually_similar_images {
  url: "https://imagelab.nownews.com/?w=696&q=70&src=https://www.nownews.com/wp-content/uploads/2019/09/1568285744-9ae87f3c40e3cd602918ff439211d94d-696x466.jpg"
}
visually_similar_images {
  url: "http://2.bp.blogspot.com/-jOdH71pI6vo/U7Egpynyo9I/AAAAAAAAGOA/6lb72dxtMBQ/s1600/%E6%B0%B4%E9%9B%89%E5%BE%A9%E8%82%B2%E6%9C%89%E6%88%90x+6.30..png"
}
visually_similar_images {
  url: "https://p1-news.hfcdn.com/p1-news/ODY2MjY3bmV3cw,,/c63545c1c55cdd58.jpg"
}
visually_similar_images {
  url: "http://img.chinatimes.com/newsphoto/2018-04-25/656/B25A00_P_03_02.jpg"
}
visually_similar_images {
  url: "https://case.ntu.edu.tw/blog/wp-content/uploads/2014/07/%E5%9C%96%E7%89%875.jpg"
}
visually_similar_images {
  url: "https://www.siraya-nsa.gov.tw/WebUploadFile/Att02/20003205.jpg"
}
visually_similar_images {
  url: "http://40.78.29.106/images/NewsImage/0325%E8%A8%B1%E5%8E%9D%E6%B8%AF%E6%BF%95%E5%9C%B0%E7%94%9F%E6%85%8B%E5%BE%A9%E8%82%B2%E5%B7%A5%E7%A8%8B%E5%8B%95%E5%9C%9F_190325_0007.jpg"
}
visually_similar_images {
  url: "http://img8.tnn.tw/news/news/20100820142716k8F6.jpg"
}
best_guess_labels {
  label: "\347\224\237\346\205\213 \345\276\251 \350\202\262"
  language_code: "zh-TW"
}`


**Vision API功能簡介**

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