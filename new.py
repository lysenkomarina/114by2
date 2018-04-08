from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://114.by/")
assert "Расписание автобусов в Республике Беларусь" in driver.title
driver.close()