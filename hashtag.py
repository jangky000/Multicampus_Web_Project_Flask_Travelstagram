from bs4 import BeautifulSoup
import selenium.webdriver as webdriver	

# 검색할 태그명
tag = '강남'

# 인스타그램 태그 페이지 URL	
url = 'https://www.instagram.com/explore/tags/' + tag 

path = 'C:/chromedriver.exe'

# 크롬창을 띄우지 않는 옵션을 넣는다	
options = webdriver.ChromeOptions()	
options.add_argument('headless')	
options.add_argument('disable-gpu')	
driver = webdriver.Chrome( path, options=options)	

# 암시적으로 최대 5초간 기다린다
driver.implicitly_wait(1)

# url에 접근한다
driver.get(url)

# 게시물 개수 정보를 가져온다
totalCount = driver.find_element_by_class_name('g47SY').text 

poplinks=list()

# 인기 게시물의 링크를 가져옴
for i in range(3):
    for j in range(3):
        slcts = '#react-root > section > main > article > div.EZdmt > div > div > div:nth-child(%s) > div:nth-child(%s) > a' %(i+1, j+1)
        # print(slcts)
        poplinks.extend( [entry.get_attribute('href') for entry in driver.find_elements_by_css_selector(slcts) if driver.find_elements_by_css_selector(slcts) ] )
        driver.implicitly_wait(1)

# 게시물 개수를 출력한다
print("totalCount :", totalCount)	
print("poplinks :", poplinks)

# 하위 링크로 이동해서 태그 뽑기
for link in poplinks:
    driver.get(link)
    tags = list()
    slcts2 = '#react-root > section > main > div > div > article > div.eo2As > div.KlCQn.G14m-.EtaWk > ul > li:nth-child(1) > div > div > div > span > a'
    tags.extend( [entry.text for entry in driver.find_elements_by_css_selector(slcts2) if driver.find_elements_by_css_selector(slcts2) ] )
    print(tags)



# 열어둔 webdriver를 종료한다 
# (종료하지 않고 반복 실행하면 메모리 누수의 원인이 된다)
driver.quit()