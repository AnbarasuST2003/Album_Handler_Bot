from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
Firstname = "tamil"
Lastname = "mani"
Date = "22.11.2001"
driver= webdriver.Chrome(executable_path=r'C:\Users\HP\Downloads\chromedriver_win32\chromedriver.exe')
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
element=driver.find_element(By.XPATH,'//*[@id="post-body-3077692503353518311"]/div[1]/div/div/h2[2]/div[1]/div/div[2]/input')
element.send_keys(Firstname)
element=driver.find_element(By.XPATH,'//*[@id="post-body-3077692503353518311"]/div[1]/div/div/h2[2]/div[1]/div/div[5]/input')
element.send_keys(Lastname)
Radio_button=driver.find_element(By.XPATH,'//*[@id="sex-0"]')
Radio_button.click()
Radio_button=driver.find_element(By.XPATH,'//*[@id="exp-2"]')
Radio_button.click()
element=driver.find_element(By.XPATH,'//*[@id="datepicker"]')
element.send_keys(Date)
time.sleep(10)
Radio_button=driver.find_element(By.XPATH,'//*[@id="profession-1"]')
Radio_button.click()
Radio_button=driver.find_element(By.XPATH,'//*[@id="tool-0"]')
Radio_button.click()
element=Select(driver.find_element(By.ID,'continents'))
element.select_by_visible_text('Africa')
element=Select(driver.find_element(By.ID,'selenium_commands'))
element.select_by_visible_text('Switch Commands')
time.sleep(5)
element = driver.find_element(By.XPATH,'//button[@id="submit"]')
element.click()
time.sleep(20)
