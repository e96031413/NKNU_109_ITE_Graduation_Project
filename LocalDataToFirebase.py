'''
Firebase是可以即時讀取的資料庫，主要以JSON格式為主。除了透過程式操作外，也能在Firebase的網頁界面上進行資料操作(上傳、讀取、修改、刪除)
'''

###程式1###


#引入模組
from firebase import firebase
import time

#產生資料
new_data = [
{'Label': 'Black_Coot','Score':0.69,'Time':
'Tue Mar 16 11:45:00 2020','FileName':'Black_Coot.jpg'},
{'Label': 'Gallinula_chloropus','Score':0.1,'Time':
'Tue Mar 17 11:45:00 2020','FileName':'Gallinula_chloropus.jpg'},
{'Label': 'Green_winged_Teal','Score':0.05,'Time':
'Tue Mar 18 11:45:00 2020','FileName':'Green_winged_Teal.jpg'},
{'Label': 'Little_Grebe','Score':0.02,'Time':
'Tue Mar 19 11:45:00 2020','FileName':'Little_Grebe.jpg'},
{'Label': 'Pheasant_tailed_Jacana','Score':0.01,'Time':
'Tue Mar 20 11:45:00 2020','FileName':'Pheasant_tailed_Jacana.jpg'},
]

#連接資料庫(由於設定任何人都能存取，所以不需要設定其他的API Key)
db_url = 'https://test-XXXXX.firebaseio.com'                    #XXXXX = e7b86
fdb = firebase.FirebaseApplication(db_url, None)

#在user下建立5筆資料(來自new_data)(.post新增)
for data in new_data:          
    fdb.post('/bird-data', data)   
    time.sleep(3)
#在user下查詢新增的資料(.get讀取)
users = fdb.get('/bird-data', None)  #None全部讀取，1代表讀取第一筆，以此類推
print("資料庫中找到以下的使用者")
for key in users:
    print(users[key]['Label'])
    print(users[key]['Score'])
    print(users[key]['Time'])
    print(users[key]['FileName'])

#整理：使用到的方法Method
#result = fdb.post('/user', user)  #建立(C)
#result = fdb.get('/user',None)    #讀取(R)
#result = fdb.delete('/user',None) #刪除(D)
