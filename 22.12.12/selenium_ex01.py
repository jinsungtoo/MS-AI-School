from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import urllib.request

"""
폴더 구성
"""
def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("error : Creating directory ... " + directory)


"""
키워드 입력, chromedriver 실행
"""
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) #강제로 꺼지지 않게 설정

keywords = "사과"
chromedriver_path = "./chromedriver.exe"

driver = webdriver.Chrome(chromedriver_path, options=options)
driver.implicitly_wait(3)

#####
##### 키워드 입력 selenium 실행
driver.get("https://www.google.co.kr/imghp?h1=ko")

## 첫 번째 방법 : xpath 이용
# input ->/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input
# button -> /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button
# keyword = driver.find_element_by_xpath(
#     '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
# keyword.send_keys(keywords)
# driver.find_element_by_xpath(
#     '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button').click()

## 두 번째 방법 : name 이용
elem = driver.find_element_by_name("q")
elem.send_keys(keywords)
elem.send_keys(Keys.RETURN) #다음 화면으로 넘어가기

##### 스크롤 #####
print(keywords + '스크롤 중 ......')
elem = driver.find_element_by_tag_name('body')
for i in range(60):
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2) #스크롤이 너무 빠르게 내려가면 봇이 잡아내기 때문에 sleep을 걸어둠.

try:
    # //*[@id="islmp"]/div/div/div/div[2]/div[1]/div[2]/div[2]/input
    driver.find_element_by_xpath(
        '//*[@id="islmp"]/div/div/div/div[2]/div[1]/div[2]/div[2]/input').click()
    for i in range(60):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
except :
    pass

links = []
images = driver.find_elements_by_css_selector("img.rg_i.Q4LuWd")

for image in images:
    if image.get_attribute('src') != None:
        links.append(image.get_attribute('src'))

print(keywords + "찾은 이미지 개수 : ", len(links))
time.sleep(2)

"""
데이터 다운로드
"""
create_folder('./'+ keywords +'_img_download')
for index, i in enumerate(links):
    url = i
    start = time.time()
    urllib.request.urlretrieve(
        url, "./" + keywords + "_img_download/" + keywords + "_" +str(index) + ".jpg")
    print(str(index) + "/" + str(len(links)) + " " + keywords +
          "다운로드 시간 -----: ", str(time.time() - start)[:5] + '초')

print(keywords + "다운로드 완료 !!")