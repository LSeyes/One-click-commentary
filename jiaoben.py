from selenium import webdriver
from selenium.webdriver.common.by import By
from tqdm import tqdm
wd = webdriver.Chrome()
wd.implicitly_wait(10)
import time
from selenium.webdriver.support.ui import Select

url = "http://222.171.146.55/"

wd.get(url)

id = wd.find_element(By.CSS_SELECTOR,'#input_username')
#id.send_keys('你的学号')
id.send_keys('')
#passwd.send_keys('你的密码')
passwd = wd.find_element(By.CSS_SELECTOR,'#input_password')
passwd.send_keys('')



#请自己输一下验证码，输完验证码不要点登录
# 输完验证码不要点登录
# 输完验证码不要点登录
# 输完验证码不要点登录
# 输完验证码不要点登录

time.sleep(8)
#自己输入验证码


loginbutton = wd.find_element(By.CSS_SELECTOR,'#loginButton')
loginbutton.click()


#教学评估目录按钮

menulist = wd.find_element(By.CSS_SELECTOR,'#menu-toggler')
menulist.click()
time.sleep(2)
jiaoxuelist = wd.find_element(By.XPATH,'//*[@id="12580300"]')
jiaoxuelist.click()
jiaoxuepinggu = wd.find_element(By.XPATH,'//*[@id="12580302"]')
jiaoxuepinggu.click()

#待评估课程
no_pinggu_list = wd.find_elements(By.CSS_SELECTOR,'tbody#jxpgtbody tr')
with tqdm(total=(len(no_pinggu_list))) as p_bar:
    p_bar.set_description('已完成')
    with tqdm(total=(len(no_pinggu_list))) as p_bar2:
        p_bar2.set_description('评估')
        for i in range(len(no_pinggu_list)):
            no_pinggu_list = wd.find_elements(By.CSS_SELECTOR, 'tbody#jxpgtbody tr')
            item = no_pinggu_list[i]
            x = item.find_element(By.CSS_SELECTOR,'button').text
            # print(x)
            p_bar.update(1)
            if x == '查看':
                continue

            pingu_button = item.find_element(By.CSS_SELECTOR,'td')
            pingu_button.click()

            time.sleep(2)
            buttonlist = wd.find_elements(By.CSS_SELECTOR,'tbody tr')
            buttonlist[2].find_element(By.CSS_SELECTOR, 'div span').click()
            buttonlist[4].find_element(By.CSS_SELECTOR, 'div span').click()
            buttonlist[6].find_element(By.CSS_SELECTOR, 'div span').click()
            buttonlist[8].find_element(By.CSS_SELECTOR, 'div span').click()
            time.sleep(1)
            wd.find_element(By.CSS_SELECTOR,'textarea').send_keys('无')

            #按提交
            wd.find_element(By.CSS_SELECTOR,'#buttonSubmit').click()

            wd.find_element(By.CSS_SELECTOR,'div.layui-layer-btn a').click()
            p_bar2.update(1)
