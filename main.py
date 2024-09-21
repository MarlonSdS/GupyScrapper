from selenium import webdriver

driver = webdriver.Firefox()

url = "https://brisanet.gupy.io"
driver.get(url)

driver.quit()