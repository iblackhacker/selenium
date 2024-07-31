'''
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://www.naver.com")
import time

time.sleep(3)
driver.get("http://www.youtube.com")
time.sleep(3)
driver.back()
time.sleep(3)
'''

'''
driver.maximize_window() # 창 최대화
time.sleep(3)

driver.minimize_window() # 창 최소화

driver.set_window_size(500, 300) #윈도우창 크기 설정


driver.set_window_position(200, 200) #윈도우창 좌표 설정



from selenium import webdriver
import time
u=["https://www.naver.com/","https://www.google.com/", "https://www.youtube.com/" ]
d=[]
for i in range(3):
    driver=webdriver.Chrome()
    d.append(driver)
    d[i].get(u[i]) 
    time.sleep(2)

from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("http://www.youtube.com")
driver.set_window_size(200, 100)

for i in range(6):
    driver.set_window_position(i*100,i*100)
    time.sleep(1)


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags=CREATE_NO_WINDOW
driver=webdriver.Chrome(service=serv)

import time
u=["https://www.naver.com/","https://www.google.com/", "https://www.youtube.com/", "https://github.com/"]
d=[]
w=960
h=540
p=[(0,0),(w,0),(0,h),(w,h)]
for i in range (4):
    driver=webdriver.Chrome(service=serv)
    d.append(driver)
    d[i].get(u[i]) 
    d[i].set_window_size(960, 540)
    d[i].set_window_position(p[i][0], p[i][1])
    time.sleep(0.05)


2.get("https://www.naver.com/")
2.set_window_size(960, 540)
2.set_window_position(960,0)

3.get("https://www.google.com/")
3.set_window_size(960, 540)
3.set_window_position(0,540)

4.get("https://github.com/")
4.set_window_size(960, 540)
4.set_window_position(960, 540)

'''
#자동입력 연습
'''
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://sbasu.pythonanywhere.com/tastyFoodApp/")

p='//*[@id="homePageLinks"]/ul/li/a'
e=driver.find_element(by='xpath',value=p)
e.click()

p='//*[@id="id_firstName"]'
e=driver.find_element(by='xpath',value=p)
e.send_keys("Jeoungun")

p='//*[@id="id_lastName"]'
e=driver.find_element(by='xpath',value=p)
e.send_keys("Kim")

p='//*[@id="id_gender_0"]'
e=driver.find_element('xpath', p)
e.click()

p='//*[@id="id_username"]'
e=driver.find_element('xpath',p)
e.send_keys("김정은바보")

p='//*[@id="id_password"]'
e=driver.find_element('xpath',p)
e.send_keys("김정은의웅장한뱃살")

p='//*[@id="id_state"]'
e=driver.find_element('xpath', p)
e.send_keys("New York")

p='//*[@id="id_fee"]'
e=driver.find_element('xpath', p)
e.send_keys("$200 : Platinum")


p='//*[@id="id_date"]'
e=driver.find_element('xpath', p)
e.send_keys("06/12/2024")

p='/html/body/form/div/input'
e=driver.find_element('xpath', p)
e.click()

'''


#구글 검색창에 양지중학교 입력 후 엔터
'''
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://www.google.com")

p='//*[@id="APjFqb"]'
e=driver.find_element('xpath', p)
e.send_keys("양지중학교")

from selenium.webdriver.common.keys import Keys
e.send_keys(Keys.RETURN)#엔터 입력 코드 2줄
'''


#학교종이
import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://v4.schoolbell-e.com/ko/gate/home?return_uri=https:%2F%2Fschoolbell-e.com%2Fko%2Fmain%2Fhome")

p='/html/body/schoolbelle-root/div/app-gate/app-gate-home/div[1]/div[3]/div[1]/div/button[1]'
e=driver.find_element(by='xpath',value=p)
e.click()

time.sleep(2)

p='/html/body/schoolbelle-root/div/app-gate/app-gate-login/div/div[1]/div/form/div[1]/div[1]/phone-number-input/div/input'
e=driver.find_element('xpath',p)
e.send_keys("01046717205")

p='/html/body/schoolbelle-root/div/app-gate/app-gate-login/div/div[1]/div/form/div[2]/div[1]/input'
e=driver.find_element('xpath',p)
e.send_keys("18756ALM!!")


p='/html/body/schoolbelle-root/div/app-gate/app-gate-login/div/div[1]/div/form/div[3]/button'
e=driver.find_element(by='xpath',value=p)
e.click()

time.sleep(3)

p='/html/body/app-root/app-main/div[1]/app-main-home/div[2]/div[1]/div[1]/app-my-group-slides/div/ngu-carousel/div/div[1]/div/ngu-tile[1]/div/div[1]/div/div'
e=driver.find_element(by='xpath',value=p)
e.click()
'''
time.sleep(2)
#날짜 정보 추가
for i in range(5):
    p=f'/html/body/app-root/app-main/div[1]/app-main-group/div[2]/div[1]/div[2]/div/app-group-board/div/div/virtual-scroller/div[2]/div/div[{i+1}]/div/app-letter-item-short/div/div/div/div[2]/extended-letter-metadata/p/span'                                
    e=driver.find_element(by='xpath',value=p)
    print(e.text)
    file.write(e.text+'\n')
file.close()


time.sleep(2)
#상위 5개의 안내문 제목을 파일로 저장하기
file=open('학교종이.txt','w')
for i in range(5):
    p=f'/html/body/app-root/app-main/div[1]/app-main-group/div[2]/div[1]/div[2]/div/app-group-board/div/div/virtual-scroller/div[2]/div/div[{i+1}]/div/app-letter-item-short/div/div/div/div[2]/h6/app-translation-viewer/span'
    e=driver.find_element(by='xpath',value=p)
    print(e.text)
    file.write(e.text+'\n')
'''

info=[]
for i in range(5):
    temp=[]
    p=/html/body/app-root/app-main/div[1]/app-main-group/div[2]/div[1]/div[2]/div/app-group-board/div/div/virtual-scroller/div[2]/div/div[{i+1}]/div/app-letter-item-short/div/div/div/div[2]/extended-letter-metadata/p/span
    e=driver.find_element(by='xpath',value=p)
    temp.append(e.text)

    p=/html/body/app-root/app-main/div[1]/app-main-group/div[2]/div[1]/div[2]/div/app-group-board/div/div/virtual-scroller/div[2]/div/div[{i+1}]/div/app-letter-item-short/div/div/div/div[2]/h6/app-translation-viewer/span
    e=driver.find_element(by='xpath',value=p)
    temp.append(e.text)

    info.append(temp)


#파일에 날짜-제목 순으로 저장하기
file=open('학교종이.txt','w')
for i in range(5):
    b[i][0],b[i][1],'\n
file.close()


'''
e=driver.find_element(by='xpath',value=p)
    print(e.text)
    file.write(e.text+'\n')
file.close()
'''




#텍스트 파일로 저장하기
'''
text='안녕하세요'
file=open('테스트.txt','w')
file.write(text)
file.close()
'''
