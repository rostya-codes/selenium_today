import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

url = 'https://www.instagram.com/'

# Указываем путь к браузеру Firefox
options = Options()
options.binary_location = '/usr/bin/firefox'
options.headless = True

# Указываем абсолютный путь к geckodriver
service = Service(executable_path='/home/rostya/projects/web/selenium_today/firefoxdriver/geckodriver')

print("Binary location:", options.binary_location)
print("Geckodriver path:", service.path)

# Создаём экземпляр браузера, используя Service
driver = webdriver.Firefox(service=service, options=options)

try:
    driver.get(url=url)
    driver.save_screenshot('i.png')
    time.sleep(5)
    # driver.get(url='https://stackoverflow.com/')
    # time.sleep(5)
    #
    # driver.refresh()
    # driver.get_screenshot_as_file('1.png')
    # driver.get('https://stackoverflow.com/')
    # time.sleep(5)
    # driver.save_screenshot('2.png')
    # time.sleep()
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
