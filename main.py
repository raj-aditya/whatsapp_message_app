
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#message body
message = "beta"
#title name of the person whom the message has to be sent
title_name = "Rahul Pat Jio"
#no of times the message has to be sent
message_times = 1
options = Options()
options.add_argument("--user-data-dir=chrome-data")
options.add_experimental_option("excludeSwitches", ["enable-automatic"])
options.add_experimental_option('useAutomationExtension', False)

# Replace below path with the absolute path/usr/bin/google-chrome /usr/share/man/man1/google-chrome.1.gz
# to chromedriver in your computer
driver = webdriver.Chrome('/snap/bin/chromium.chromedriver', options=options)

driver.get('https://web.whatsapp.com')
time.sleep(20)
driver.find_element_by_xpath("//*[@title='"+ title_name +"']").click()
for x in range(message_times):
  driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message)
  driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()
  print("Sent: " + str(x+1))

driver.close()

