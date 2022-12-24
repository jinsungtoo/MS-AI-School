### 데이터 크롤링 코드 ###

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from multiprocessing import Pool
import time
import os
import urllib.request
import pandas as pd


def create_folder(directory):
    #폴더 생성
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("error : Creating directory ... " + directory)



# 검색 키워드 호출
key = pd.read_csv('./keyword.txt', encoding='utf-8', names=['keyword'])
keyword = []
[keyword.append(key['keyword'][x]) for x in range(len(key))]

def image_download(keywords):
    create_folder("./" + keywords + "/")

    # 크롬 드라이브 호출
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True) #강제로 꺼지지 않게 설정
    chromedriver = "./chromedriver.exe"
    driver = webdriver.Chrome(chromedriver, options=options)
    driver.implicitly_wait(3)

    # 검색
    print('검색 >> ', keywords)
    driver.get("https://www.google.co.kr/imghp?h1=ko")
    keyword = driver.find_element_by_xpath(
        '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    keyword.send_keys(keywords)
    keyword.send_keys(Keys.RETURN)

    # 스크롤 내리기 -> 결과 더보기 버튼 클릭
    print("스크롤 ..... ", keywords)
    elem = driver.find_element_by_tag_name('body')
    for i in range(60):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
    try:
        # 결과 더보기 버튼 클릭
        driver.find_element_by_xpath(
        '//*[@id="islmp"]/div/div/div/div[2]/div[1]/div[2]/div[2]/input').click()
        for i in range(60):
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.2)
    except:
        pass

    images = driver.find_elements_by_css_selector("img.rg_i.Q4LuWd")
    print(keywords + '찾은 이미지 개수 : ', + len(images))

    links = []
    for i in range(1, len(images)):
        try:
            # //*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img
            # //*[@id = "islrg"]/div[1]/div[40]/a[1]/div[1]/img
            driver.find_element_by_xpath(
                '//*[@id="islrg"]/div[1]/div[' + str(i) + ']/a[1]/div[1]/img').click()
            links.append(driver.find_element_by_xpath(
                '//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img').get_attribute(
                'src'))
            print(keywords + '링크 수집 중 ... number :  ' +
                  str(i) + '/' + str(len(images)))
        except:
            continue
    forbidden = 0
    for index, i in enumerate(links):
        try:
            url = i
            start = time.time()
            urllib.request.urlretrieve(
                url, "./" + keywords +"/" + str(index-forbidden) + ".jpg")
            print(str(index + 1) + "/" + str(len(links)) + " " + keywords +
                  " 다운로드 중 ------ Download time : " , str(time.time() - start)[:5] + '초')
        except:
            forbidden += 1
            continue


"""
실행
"""
if __name__ == '__main__':
    pool = Pool(processes=5) # 최대 3개의 창을 동시에 활용할 수 있도록 설정(멀티 프로세스)
    pool.map(image_download, keyword)
