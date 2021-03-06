from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://114.by/")
assert "Расписание автобусов в Республике Беларусь" in driver.title
place_from = driver.find_element_by_css_selector('[placeholder="введите откуда выезжаем"]')
place_from.clear()
place_from.send_keys("Минск")
first_from_place = driver.find_element_by_css_selector('.form-route [class="col-sm-12 col-md-4"]:nth-of-type(1) .list-group-item:nth-of-type(1) [href]')
first_from_place.click()
place_where = driver.find_element_by_css_selector('[placeholder="введите куда приезжаем"]')
place_where.clear()
place_where.send_keys("Лида") 
time.sleep(1000)
driver.close()
