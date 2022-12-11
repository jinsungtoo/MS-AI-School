from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

#엣지로 웹페이지(구글) 열기
Edge_web = webdriver.Edge()
Edge_web.implicitly_wait(10)
Edge_web.get("https://www.google.com")

#구글에서 micrososft를 검색
elem = Edge_web.find_element(By.NAME,'q')
elem.clear()
search = 'banana'
elem.send_keys(search)
elem.send_keys(Keys.RETURN)

#이미지 메뉴 검색
elem = Edge_web.find_element(By.XPATH,'//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[1]/div/div/span[1]').click
selenium_scroll_option(driver)
input()