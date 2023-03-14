# python_Selenium_ScreenshotWebPage
[python]使用Selenium函式庫對網頁進行截圖  
## 前置動作
### chrome driver 瀏覽器驅動程式  
需要先確認chrome 版本 再下載對應的檔案  
[下載連結](https://chromedriver.chromium.org/downloads)  
下載後需要將exe檔的路徑記好 程式中需要替換自己的路徑位置

### Selenium 下載
``` 
pip install selenium
``` 

## Code說明
### 開啟網頁
``` 
# 只需要引入selenium函式庫中的 webdriver 對瀏覽器進行操作
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 下載chromedriver後 將路徑寫至此
PATH = Service(executable_path=r"C:/python_selenium/chromedriver.exe")
driver = webdriver.Chrome(service=PATH)
# 開啟網頁
driver.get("https://dcard.tw/f")
``` 

### 關閉網頁
``` 
driver.quit()
``` 

### 保持網頁開啟
``` 
while(True): 
     pass
``` 

### 網頁設定開啟時間
``` 
import time 
time.sleep(5)
``` 

## 資料參考來源
[Python Selenium 快速開始、網頁截圖 By 彭彭](https://youtu.be/M4zu9_HIUHI)
