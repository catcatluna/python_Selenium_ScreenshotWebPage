# 載入 Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 設立chrome driver的路徑
options = Options()
# 檔案如果放在C槽Users中 可以在路徑之前放上r 因為\U 在unicode中後面需要接數字, 系統判斷會產生錯誤訊息
# 請將此路徑換成你的本機路徑
options.chrome_executable_path = r"C:\Users\guagu\PycharmProjects\pythonProject_Selenium1\chromedriver.exe"

# 建立 Driver 物件實體
driver = webdriver.Chrome(options = options)

# 將網頁視窗放到最大化
driver.maximize_window()

# 目標網頁
driver.get("https://www.google.com/")
# 網頁截圖
driver.save_screenshot("google網頁.png")
# 目標網頁2
driver.get("https://www.yahoo.com/")
# 截圖
driver.save_screenshot("yahoo網頁.png")

# 完成任務關閉瀏覽器
driver.close()

# 因為瀏覽器可能會在完成指令後自動關閉 有兩種做法延長關閉時間
# 1 設定TIMER
# 2 保持開啟

# 1.
# import time
# time.sleep(5)

# 2.
# while(True):
#      pass