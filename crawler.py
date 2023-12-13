# selenium의 webdriver를 사용하기 위한 import
from selenium import webdriver
from selenium.webdriver.common.by import By

# selenium으로 키를 조작하기 위한 import
from selenium.webdriver.common.keys import Keys

# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time

# 크롬드라이버 실행
driver = webdriver.Chrome() 

# 카카오 블로그 크롤링, 제목, 링크, 날짜 출력
def kakao_crawling():
    url = 'https://tech.kakao.com/blog/'
    #크롬 드라이버에 url 주소 넣고 실행
    driver.get(url)
    # 페이지가 완전히 로딩되도록 3초동안 기다림
    time.sleep(3)
    i = 1
    news = []
    while True:
        try:
            new = driver.find_element(By.XPATH, f"/html/body/div[2]/div/section[3]/div/div/div[1]/div/div/div[3]/div/div[1]/article[{i}]/div/h3/a")
            date = driver.find_element(By.XPATH, f"/html/body/div[2]/div/section[3]/div/div/div[1]/div/div/div[3]/div/div[1]/article[{i}]/div/div[1]/span[2]")    
            news.append([new.text, new.get_attribute('href'), date.text])
            i += 1
        except:
            break
    return news

kakao_news = kakao_crawling()
print(kakao_news)
