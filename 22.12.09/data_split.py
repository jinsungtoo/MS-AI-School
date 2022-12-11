# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Edge
# driver.implicitly_wait(10)
#
# drive.get('https://www.google.com')
#
# elem = driver.find_element(By.NAME, 'q')
# elem.clear()
# search = 'dog'
# elem.send_keys(search)
# elem.send_keys(Keys.RETURN)

import os
import random
from collections import defaultdict

label_dict = defaultdict(int)

data_cnt_list = []

for idx in enumerate(os.listdir('.')):
    label_dict[v] = idx
    if os.path.isdir(v):
        data_cnt_list.append(len(os.listdir(v)))

test_data_cnt = int(sum(data_cnt_list)/len(data_cnt_list)*0.2)
df_list = defaultdict(list)
for i in os.listdir('.'):
    total_data = os.listdir(i)
    test_data = random.sample(total_data, test_data_cnt)
    train_data = [j for j in total_data if j not in test_data]
    train_df_list['file_name'] = train_data
    test_df_list