from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

# example 1
# driver.get("https://demoqa.com/upload-download")
# driver.find_element(By.ID, 'uploadFile').send_keys("C:/contohFile.pdf")

# example 2
driver.get("https://gofile.io/uploadFiles")
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[10]/div/div/div/div/div/div[1]/div/button').click()

time.sleep(3)

pyautogui.write(r"C:\contohFile.pdf")
pyautogui.press("enter")