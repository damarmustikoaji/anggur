from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')

try:
    driver = webdriver.Chrome(chrome_options=options)
except Exception as e:
    driver = webdriver.Chrome(executable_path='../driver/chromedriver', chrome_options=options)

driver.set_window_size(1280, 800)
driver.get('https://google.com')

print "driver.title : "+driver.title
driver.save_screenshot('image.png')

driver.close()
